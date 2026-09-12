#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FabroGym — F3-07 / B6
Auditoría preventiva de privacidad ajustada a la guía específica de FabroGym.

Ejecución recomendada desde la raíz del repositorio:

    python 07_Datos/scripts/verificar_privacidad_publica.py

Genera:

    07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md

Criterio principal:
- la capa pública debe permanecer sin datos personales directos;
- la capa restringida cifrada puede estar representada por contenedores
  expresamente documentados/autorizados;
- un contenedor restringido conocido NO se considera por sí solo una
  publicación accidental de sus contenidos;
- la contraseña/clave nunca debe quedar en Git;
- el cifrado y la autorización final requieren confirmación humana.

Códigos de salida:
- 0: no se encontraron hallazgos automáticos bloqueantes;
- 2: se encontraron hallazgos automáticos que deben corregirse antes del cierre.

La ausencia de hallazgos automáticos NO sustituye la revisión humana F3-07/B6.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import csv
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
DATOS_ROOT = REPO_ROOT / "07_Datos"
OUT = DATOS_ROOT / "resultados" / "REVISION_PRIVACIDAD_PUBLICA.md"
OUT.parent.mkdir(parents=True, exist_ok=True)

EXCLUDED_DIRS = {
    ".git", ".venv", "venv", "__pycache__", "node_modules", ".idea", ".vscode",
}

MEDIA_EXTENSIONS = {
    ".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg",
    ".mp4", ".mov", ".avi", ".mkv", ".webm", ".wmv",
}

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".heic", ".tif", ".tiff",
}

ARCHIVE_EXTENSIONS = {
    ".zip", ".rar", ".7z", ".tar", ".gz", ".tgz", ".bz2", ".xz",
}

ALLOWED_PUBLIC_MEDIA = {
    "05_MVP/video_demo.mp4": "Video demostrativo del MVP.",
    "09_Defensa/video_defensa.mp4": "Grabación de la defensa final.",
    "10_Autoria/grabaciones/Vd_01.mp4": "Grabación de sesión de trabajo del equipo.",
    "10_Autoria/grabaciones/Vd_02.mp4": "Grabación de sesión de trabajo del equipo.",
}

# ---------------------------------------------------------------------------
# Excepciones documentadas de la capa restringida
# ---------------------------------------------------------------------------
# Estas rutas NO se consideran hallazgo bloqueante por su sola presencia.
# El auditor NO abre los .7z y NO intenta conocer la contraseña.
# El cifrado/protección debe confirmarse manualmente antes del tag final.
AUTHORIZED_RESTRICTED = {
    "02_Evidencias/00_Restringido/evidencias_restringidas.7z": {
        "kind": "encrypted_container",
        "reason": (
            "Contenedor de evidencia restringida previsto por el proyecto y "
            "versionado mediante Git LFS. Debe permanecer cifrado/protegido y "
            "la clave no debe almacenarse en el repositorio."
        ),
    },
    "02_Evidencias/00_Restringido/fichas_tecnicas.csv": {
        "kind": "technical_inventory",
        "reason": (
            "Inventario técnico de evidencia (códigos, duración, códec, tamaño y SHA-256). "
            "La guía específica de FabroGym indica conservar este formato."
        ),
    },
    "10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z": {
        "kind": "encrypted_container",
        "reason": (
            "Contenedor de originales A11 para preservar EXIF. Solo es admisible "
            "si está cifrado/protegido y la clave permanece fuera del repositorio."
        ),
    },
}

# Rutas que siguen siendo bloqueantes salvo que coincidan EXACTAMENTE con una
# excepción declarada arriba.
RESTRICTED_PATH_RULES = [
    (
        "PRIVACIDAD_PENDIENTE_PUBLICA",
        re.compile(r"PENDIENTE[_ -]?PRIVACIDAD|NO[_ -]?SUBIR[_ -]?A[_ -]?GIT", re.I),
        "ruta marcada explícitamente como pendiente de privacidad/no publicable",
    ),
    (
        "ORIGINAL_CUESTIONARIO_PUBLICO",
        re.compile(r"Fotos?[_ -]?Original(?:es)?[_ -]?(?:del[_ -]?)?Cuestionario", re.I),
        "nombre compatible con fotografías originales del cuestionario fuera de un contenedor autorizado",
    ),
    (
        "CONSENTIMIENTO_ORIGINAL_PUBLICO",
        re.compile(r"consentimiento.*(?:original|firmad)", re.I),
        "nombre compatible con consentimiento original/firmado",
    ),
    (
        "TRANSCRIPCION_SIN_ANONIMIZAR",
        re.compile(r"transcripci[oó]n.*sin.*anonim", re.I),
        "nombre compatible con transcripción sin anonimizar",
    ),
    (
        "IDENTIFICADOR_DIRECTO_EN_RUTA",
        re.compile(r"(^|[/_. -])(c[eé]dula|dni|pasaporte)([/_. -]|$)", re.I),
        "nombre compatible con identificador personal directo",
    ),
]

IDENTIFIABLE_HEADER_TOKENS = [
    "nombre", "name", "apellido", "surname",
    "correo", "email", "e-mail",
    "telefono", "teléfono", "celular", "phone", "mobile",
    "cedula", "cédula", "dni", "pasaporte",
    "direccion", "dirección", "address",
    "documento_identidad", "documento de identidad", "id_number",
    "participant_name", "participant name",
]

EMAIL_RE = re.compile(r"(?<![\w.+-])[\w.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![\w.-])")
EC_PHONE_RE = re.compile(r"(?<!\d)(?:\+593|593|0)?9\d{8}(?!\d)")
GENERIC_10_DIGIT_RE = re.compile(r"(?<![A-Za-z0-9])\d{10}(?![A-Za-z0-9])")
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")

findings: list[dict[str, str]] = []
warnings: list[dict[str, str]] = []
infos: list[dict[str, str]] = []
_seen_findings: set[tuple[str, str]] = set()
_seen_warnings: set[tuple[str, str]] = set()
_seen_infos: set[tuple[str, str]] = set()

def relpath(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()

def add_finding(code: str, path: str, detail: str) -> None:
    key = (code, path)
    if key not in _seen_findings:
        _seen_findings.add(key)
        findings.append({"code": code, "path": path, "detail": detail})

def add_warning(code: str, path: str, detail: str) -> None:
    key = (code, path)
    if key not in _seen_warnings:
        _seen_warnings.add(key)
        warnings.append({"code": code, "path": path, "detail": detail})

def add_info(code: str, path: str, detail: str) -> None:
    key = (code, path)
    if key not in _seen_infos:
        _seen_infos.add(key)
        infos.append({"code": code, "path": path, "detail": detail})

def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)

def public_files() -> list[Path]:
    out = []
    for path in REPO_ROOT.rglob("*"):
        if path.is_file() and not should_skip(path):
            out.append(path)
    return sorted(out, key=lambda p: relpath(p).casefold())

def read_lfs_pointer(path: Path) -> dict[str, str] | None:
    try:
        if path.stat().st_size > 4096:
            return None
        raw = path.read_bytes()
    except OSError:
        return None
    if not raw.startswith(b"version https://git-lfs.github.com/spec/v1"):
        return None
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        return None
    result = {}
    for line in text.splitlines():
        if line.startswith("oid "):
            result["oid"] = line[4:].strip()
        elif line.startswith("size "):
            result["size"] = line[5:].strip()
    return result

def header_matches_sensitive_token(header: str) -> bool:
    h = header.casefold()
    return any(
        re.search(rf"(?<!\w){re.escape(token.casefold())}(?!\w)", h)
        for token in IDENTIFIABLE_HEADER_TOKENS
    )

def count_regex_in_column(rows, header, regex) -> int:
    count = 0
    for row in rows:
        value = (row.get(header) or "").strip()
        if value and regex.search(value):
            count += 1
    return count

# ---------------------------------------------------------------------------
# 1. Escaneo general
# ---------------------------------------------------------------------------
all_files = public_files()
files_scanned = len(all_files)
allowed_media_found = []
archives_seen = []
authorized_present = []

for path in all_files:
    rel = relpath(path)
    suffix = path.suffix.casefold()
    authorized = rel in AUTHORIZED_RESTRICTED

    if authorized:
        meta = AUTHORIZED_RESTRICTED[rel]
        authorized_present.append(rel)
        add_info("RESTRINGIDO_DOCUMENTADO", rel, meta["reason"])

        if meta["kind"] == "encrypted_container":
            lfs = read_lfs_pointer(path)
            if lfs:
                add_info(
                    "LFS_RESTRINGIDO_ESPERADO",
                    rel,
                    f"puntero Git LFS documentado (size={lfs.get('size','desconocido')} bytes; {lfs.get('oid','oid desconocido')})",
                )
            add_warning(
                "CONFIRMAR_CIFRADO_MANUAL",
                rel,
                "confirmar antes del tag final que el contenedor está cifrado/protegido y que la contraseña/clave no aparece en Git, README, commits ni artefactos públicos",
            )
        # Una excepción autorizada no pasa por las reglas genéricas de bloqueo.
        continue

    # Si aparece otro archivo dentro de 00_Restringido, debe revisarse.
    if rel.startswith("02_Evidencias/00_Restringido/"):
        add_finding(
            "RESTRINGIDO_NO_DOCUMENTADO",
            rel,
            "archivo adicional dentro de 00_Restringido que no está incluido en la lista de excepciones documentadas",
        )

    matched_restricted_rule = False
    for code, regex, detail in RESTRICTED_PATH_RULES:
        if regex.search(rel):
            matched_restricted_rule = True
            add_finding(code, rel, detail)

    if suffix in MEDIA_EXTENSIONS:
        if rel in ALLOWED_PUBLIC_MEDIA:
            allowed_media_found.append((rel, ALLOWED_PUBLIC_MEDIA[rel]))
        else:
            add_finding(
                "MULTIMEDIA_NO_CLASIFICADA",
                rel,
                "archivo audiovisual no clasificado; revisar si contiene participantes o datos identificables",
            )

    if suffix in ARCHIVE_EXTENSIONS:
        archives_seen.append(rel)
        low = rel.casefold()
        suspicious = (
            matched_restricted_rule
            or "original" in low
            or "restring" in low
            or "consent" in low
            or ("cuestionario" in low and "foto" in low)
        )
        if suspicious:
            add_finding(
                "ARCHIVO_COMPRIMIDO_RESTRINGIDO_NO_AUTORIZADO",
                rel,
                "archivo comprimido potencialmente restringido fuera de la lista de contenedores documentados",
            )

    lfs = read_lfs_pointer(path)
    if lfs and (matched_restricted_rule or "restring" in rel.casefold()):
        add_finding(
            "LFS_RESTRINGIDO_NO_AUTORIZADO",
            rel,
            f"puntero Git LFS hacia material potencialmente restringido no documentado (size={lfs.get('size','desconocido')} bytes)",
        )

# Verificar presencia de los dos artefactos que la guía/proyecto espera en 00_Restringido.
for required in (
    "02_Evidencias/00_Restringido/evidencias_restringidas.7z",
    "02_Evidencias/00_Restringido/fichas_tecnicas.csv",
):
    if required not in authorized_present:
        add_warning(
            "RESTRINGIDO_ESPERADO_AUSENTE",
            required,
            "artefacto documentado de la capa restringida no encontrado en el árbol inspeccionado",
        )

# ---------------------------------------------------------------------------
# 2. CSV públicos de 07_Datos
# ---------------------------------------------------------------------------
csv_scanned = 0
csv_read_errors = 0

for folder_name in ("datos_crudos", "datos_procesados"):
    folder = DATOS_ROOT / folder_name
    if not folder.exists():
        add_warning("CARPETA_DATOS_AUSENTE", relpath(folder), "la carpeta esperada no existe")
        continue

    for path in sorted(folder.rglob("*.csv"), key=lambda p: relpath(p).casefold()):
        csv_scanned += 1
        rel = relpath(path)
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as fh:
                reader = csv.DictReader(fh)
                rows = list(reader)
                headers = reader.fieldnames or []
        except Exception as exc:
            csv_read_errors += 1
            add_warning("CSV_NO_LEIBLE", rel, f"no fue posible analizar el CSV: {type(exc).__name__}")
            continue

        if not rows or not headers:
            continue

        for header in headers:
            if header is None:
                continue

            if header_matches_sensitive_token(header):
                nonempty = sum(1 for row in rows if (row.get(header) or "").strip())
                if nonempty:
                    add_finding(
                        "COLUMNA_IDENTIFICABLE",
                        rel,
                        f"columna={header!r}; valores_no_vacios={nonempty}",
                    )

            email_count = count_regex_in_column(rows, header, EMAIL_RE)
            if email_count:
                add_finding(
                    "EMAIL_EN_DATOS_PUBLICOS",
                    rel,
                    f"columna={header!r}; filas_con_email={email_count}",
                )

            phone_count = count_regex_in_column(rows, header, EC_PHONE_RE)
            if phone_count:
                add_finding(
                    "TELEFONO_EN_DATOS_PUBLICOS",
                    rel,
                    f"columna={header!r}; filas_con_telefono_probable={phone_count}",
                )

            if header_matches_sensitive_token(header):
                id_count = count_regex_in_column(rows, header, GENERIC_10_DIGIT_RE)
                if id_count:
                    add_finding(
                        "IDENTIFICADOR_NUMERICO_EN_DATOS_PUBLICOS",
                        rel,
                        f"columna={header!r}; filas_con_identificador_probable={id_count}",
                    )

# ---------------------------------------------------------------------------
# 3. A6 / EXIF
# ---------------------------------------------------------------------------
exif_inventory = REPO_ROOT / "10_Autoria" / "exif_inventario.csv"
a6_records = 0
a6_valid_records = 0
a6_privacy_pending = 0
a6_invalid_details = []

if not exif_inventory.exists():
    add_finding(
        "A6_INVENTARIO_EXIF_AUSENTE",
        relpath(exif_inventory),
        "no existe el inventario requerido para documentar fecha/dispositivo/hash",
    )
else:
    try:
        with exif_inventory.open("r", encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.DictReader(fh))
    except Exception as exc:
        rows = []
        add_finding(
            "A6_INVENTARIO_EXIF_NO_LEIBLE",
            relpath(exif_inventory),
            f"no fue posible leer el inventario: {type(exc).__name__}",
        )

    a6_rows = [
        row for row in rows
        if (row.get("Tipo_evidencia") or "").strip() == "F3-01_APLICACION_CUESTIONARIO"
    ]
    a6_records = len(a6_rows)

    for idx, row in enumerate(a6_rows, start=1):
        date_ok = bool((row.get("Fecha_captura_EXIF") or "").strip())
        source_date_ok = bool((row.get("Fuente_fecha_EXIF") or "").strip())
        device_ok = bool((row.get("Dispositivo_EXIF") or "").strip())
        state_ok = (row.get("Estado_EXIF") or "").strip().upper() == "OK"
        sha = (row.get("SHA256") or "").strip()
        sha_ok = bool(SHA256_RE.fullmatch(sha))

        if date_ok and source_date_ok and device_ok and state_ok and sha_ok:
            a6_valid_records += 1
        else:
            missing = []
            if not date_ok: missing.append("Fecha_captura_EXIF")
            if not source_date_ok: missing.append("Fuente_fecha_EXIF")
            if not device_ok: missing.append("Dispositivo_EXIF")
            if not state_ok: missing.append("Estado_EXIF!=OK")
            if not sha_ok: missing.append("SHA256 inválido")
            a6_invalid_details.append(f"registro {idx}: {', '.join(missing)}")

        privacy_state = (row.get("Estado_privacidad") or "").strip().upper()
        if any(token in privacy_state for token in ("VERIFICAR", "PENDIENTE", "REVISAR")):
            a6_privacy_pending += 1

    if a6_records < 5:
        add_finding(
            "A6_FOTOS_INSUFICIENTES",
            relpath(exif_inventory),
            f"solo se encontraron {a6_records} registros F3-01; se requieren al menos 5",
        )
    elif a6_valid_records < 5:
        add_finding(
            "A6_EXIF_INSUFICIENTE",
            relpath(exif_inventory),
            f"solo {a6_valid_records} de {a6_records} registros F3-01 tienen metadatos completos y SHA-256 válido",
        )
    else:
        add_info(
            "A6_EXIF_OK",
            relpath(exif_inventory),
            f"{a6_valid_records} registros F3-01 documentan fecha EXIF, dispositivo y SHA-256 válidos",
        )

    if a6_privacy_pending:
        add_warning(
            "A6_PRIVACIDAD_MANUAL_PENDIENTE",
            relpath(exif_inventory),
            f"{a6_privacy_pending} registros F3-01 requieren confirmación manual de privacidad/publicación",
        )

questionnaire_photo_dir = REPO_ROOT / "02_Evidencias" / "Cuestionario" / "Fotos_Aplicacion"
questionnaire_public_photos = []
if questionnaire_photo_dir.exists():
    questionnaire_public_photos = sorted(
        [p for p in questionnaire_photo_dir.iterdir()
         if p.is_file() and p.suffix.casefold() in IMAGE_EXTENSIONS],
        key=lambda p: p.name.casefold(),
    )
if len(questionnaire_public_photos) < 5:
    add_warning(
        "A6_COPIAS_PUBLICAS_INSUFICIENTES",
        relpath(questionnaire_photo_dir),
        f"se encontraron {len(questionnaire_public_photos)} fotografías públicas del cuestionario",
    )

# ---------------------------------------------------------------------------
# 4. Piezas para revisión visual/manual
# ---------------------------------------------------------------------------
manual_consent_pdfs = sorted(
    (REPO_ROOT / "02_Evidencias" / "Consentimientos").glob("*Censurado*.pdf")
) if (REPO_ROOT / "02_Evidencias" / "Consentimientos").exists() else []

manual_acts = sorted(
    (REPO_ROOT / "02_Evidencias" / "Validacion_walkthrough").glob("*Acta*.pdf")
) if (REPO_ROOT / "02_Evidencias" / "Validacion_walkthrough").exists() else []

team_photo_dir = REPO_ROOT / "10_Autoria" / "fotos_equipo"
team_public_photos = sorted(
    [p for p in team_photo_dir.rglob("*")
     if p.is_file() and p.suffix.casefold() in IMAGE_EXTENSIONS],
    key=lambda p: relpath(p).casefold(),
) if team_photo_dir.exists() else []

manual_visual_total = (
    len(manual_consent_pdfs)
    + len(manual_acts)
    + len(questionnaire_public_photos)
    + len(team_public_photos)
)

# ---------------------------------------------------------------------------
# 5. Reporte
# ---------------------------------------------------------------------------
finding_counts = Counter(item["code"] for item in findings)
warning_counts = Counter(item["code"] for item in warnings)
status = "NO APTO PARA CIERRE AUTOMÁTICO" if findings else "SIN HALLAZGOS AUTOMÁTICOS BLOQUEANTES"

lines = [
    "# Revisión automática de privacidad — F3-07 / B6",
    "",
    f"**Estado automático:** **{status}**.",
    "",
    "## Criterio aplicado",
    "",
    "- `07_Datos/` y los artefactos de publicación deben permanecer sin datos personales directos.",
    "- La capa restringida cifrada se trata de forma separada.",
    "- La presencia de un contenedor restringido expresamente documentado no constituye por sí sola un hallazgo bloqueante.",
    "- El auditor no abre archivos cifrados ni conoce contraseñas; su cifrado/protección debe confirmarse manualmente.",
    "",
    "## Alcance de la auditoría",
    "",
    f"- Archivos inspeccionados por nombre/extensión: **{files_scanned}**.",
    f"- CSV inspeccionados en `07_Datos/datos_crudos` y `datos_procesados`: **{csv_scanned}**.",
    f"- CSV no legibles: **{csv_read_errors}**.",
    f"- Hallazgos automáticos bloqueantes: **{len(findings)}**.",
    f"- Advertencias / comprobaciones humanas: **{len(warnings)}**.",
    "",
    "## Capa restringida documentada",
    "",
]

if authorized_present:
    for rel in sorted(authorized_present):
        reason = AUTHORIZED_RESTRICTED[rel]["reason"]
        lines.append(f"- `{rel}` — **DOCUMENTADO** — {reason}")
else:
    lines.append("- No se detectaron los artefactos restringidos documentados.")

lines += [""]

if findings:
    lines += ["## Hallazgos automáticos que deben corregirse", ""]
    for item in sorted(findings, key=lambda x: (x["code"], x["path"].casefold())):
        lines.append(f"- **{item['code']}** — `{item['path']}` — {item['detail']}")
    lines.append("")
else:
    lines += [
        "## Resultado automático",
        "",
        "No se detectaron hallazgos automáticos bloqueantes con las reglas aplicadas.",
        "",
    ]

if warnings:
    lines += ["## Advertencias y verificaciones manuales pendientes", ""]
    for item in sorted(warnings, key=lambda x: (x["code"], x["path"].casefold())):
        lines.append(f"- **{item['code']}** — `{item['path']}` — {item['detail']}")
    lines.append("")

if infos:
    lines += ["## Verificaciones informativas", ""]
    for item in sorted(infos, key=lambda x: (x["code"], x["path"].casefold())):
        lines.append(f"- **{item['code']}** — `{item['path']}` — {item['detail']}")
    lines.append("")

lines += [
    "## Verificación técnica A6 — fotografías y EXIF",
    "",
    f"- Registros F3-01 en `10_Autoria/exif_inventario.csv`: **{a6_records}**.",
    f"- Registros EXIF técnicamente válidos: **{a6_valid_records}**.",
    f"- Copias fotográficas en `02_Evidencias/Cuestionario/Fotos_Aplicacion/`: **{len(questionnaire_public_photos)}**.",
    f"- Resultado técnico A6: **{'CUMPLE' if a6_valid_records >= 5 else 'NO CUMPLE'}**.",
    "",
    "## Revisión visual/manual requerida",
    "",
    f"- Consentimientos censurados: **{len(manual_consent_pdfs)}**.",
    f"- Actas WALK: **{len(manual_acts)}**.",
    f"- Fotografías públicas del cuestionario: **{len(questionnaire_public_photos)}**.",
    f"- Fotografías del equipo/autoria: **{len(team_public_photos)}**.",
    f"- Total de piezas visuales a revisar: **{manual_visual_total}**.",
    "",
    "### Confirmaciones humanas antes del tag final",
    "",
    "- [ ] `02_Evidencias/00_Restringido/evidencias_restringidas.7z` está cifrado/protegido.",
    "- [ ] La contraseña/clave del contenedor restringido NO aparece en GitHub, README, commits ni artefactos públicos.",
    "- [ ] Si `A11 Fotos_Originales_Cuestionario.7z` permanece versionado, está cifrado/protegido y su clave está fuera del repositorio.",
    "- [ ] Las cinco fotografías públicas del cuestionario están autorizadas o enmascaradas de forma suficiente.",
    "- [ ] Los consentimientos censurados y actas públicas no exponen firmas, cédulas, teléfonos, correos ni otros identificadores.",
    "",
    "## Interpretación del código de salida",
    "",
    "- `0`: no existen hallazgos automáticos bloqueantes; todavía deben cerrarse las confirmaciones humanas anteriores.",
    "- `2`: existe al menos un hallazgo automático que debe corregirse antes del release/tag final.",
]

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("FabroGym — auditoría de privacidad F3-07/B6")
print(f"Raíz: {REPO_ROOT}")
print(f"Archivos inspeccionados: {files_scanned}")
print(f"CSV inspeccionados: {csv_scanned}")
print(f"Hallazgos bloqueantes: {len(findings)}")
if finding_counts:
    for code, count in sorted(finding_counts.items()):
        print(f"  - {code}: {count}")
print(f"Advertencias/manual: {len(warnings)}")
if warning_counts:
    for code, count in sorted(warning_counts.items()):
        print(f"  - {code}: {count}")
print(f"A6 EXIF válidos: {a6_valid_records}/{a6_records}")
print(f"Reporte: {OUT}")

sys.exit(2 if findings else 0)
