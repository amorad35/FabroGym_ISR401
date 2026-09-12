#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FabroGym — F3-07 / B6
Auditoría preventiva de privacidad de la capa pública del repositorio.

Ejecución recomendada desde la raíz del repositorio:

    python 07_Datos/scripts/verificar_privacidad_publica.py

También puede ejecutarse desde cualquier otra ubicación.

Genera:

    07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md

Objetivos:
- detectar archivos potencialmente restringidos publicados por error;
- detectar multimedia no clasificada en el árbol público;
- detectar archivos comprimidos que puedan contener originales restringidos;
- detectar punteros Git LFS hacia material restringido;
- revisar columnas/valores potencialmente identificables en los CSV públicos;
- comprobar documentalmente el requisito técnico A6 mediante exif_inventario.csv;
- separar la verificación automática de la revisión visual/manual de privacidad.

Privacidad del propio auditor:
- nunca imprime valores personales encontrados;
- solo reporta ruta, columna, tipo de hallazgo y conteos;
- no abre ni extrae archivos comprimidos;
- no inspecciona visualmente PDFs, imágenes ni videos.

Códigos de salida:
- 0: no se encontraron hallazgos automáticos bloqueantes;
- 2: se encontraron hallazgos automáticos que deben corregirse antes del cierre.

La ausencia de hallazgos automáticos NO sustituye la revisión humana requerida por F3-07/B6.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import csv
import re
import sys


# -----------------------------------------------------------------------------
# Rutas principales
# -----------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
DATOS_ROOT = REPO_ROOT / "07_Datos"
OUT = DATOS_ROOT / "resultados" / "REVISION_PRIVACIDAD_PUBLICA.md"
OUT.parent.mkdir(parents=True, exist_ok=True)


# -----------------------------------------------------------------------------
# Configuración de escaneo
# -----------------------------------------------------------------------------

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode",
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

# Multimedia pública conocida y documentada que NO corresponde a evidencia
# primaria de participantes. Si se añade nueva multimedia al repositorio debe
# clasificarse explícitamente aquí o retirarse de la capa pública.
ALLOWED_PUBLIC_MEDIA = {
    "05_MVP/video_demo.mp4": "Video demostrativo del MVP.",
    "09_Defensa/video_defensa.mp4": "Grabación de la defensa final.",
    "10_Autoria/grabaciones/Vd_01.mp4": "Grabación de sesión de trabajo del equipo para evidencia de autoría.",
    "10_Autoria/grabaciones/Vd_02.mp4": "Grabación de sesión de trabajo del equipo para evidencia de autoría.",
}

# Patrones de rutas/nombres que no deberían contener material real dentro del
# repositorio público. Las coincidencias se evalúan sobre la ruta relativa.
RESTRICTED_PATH_RULES = [
    (
        "RUTA_RESTRINGIDA_PUBLICA",
        re.compile(r"(^|/)00[_ -]?Restringido(/|$)", re.I),
        "ruta declarada como restringida presente dentro del árbol público",
    ),
    (
        "PRIVACIDAD_PENDIENTE_PUBLICA",
        re.compile(r"PENDIENTE[_ -]?PRIVACIDAD|NO[_ -]?SUBIR[_ -]?A[_ -]?GIT", re.I),
        "ruta marcada explícitamente como pendiente de privacidad/no publicable",
    ),
    (
        "ORIGINAL_CUESTIONARIO_PUBLICO",
        re.compile(r"Fotos?[_ -]?Original(?:es)?[_ -]?(?:del[_ -]?)?Cuestionario", re.I),
        "nombre compatible con fotografías originales del cuestionario",
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

# Términos que indican columnas potencialmente identificables. La coincidencia
# usa límites de palabra para evitar falsos positivos en preguntas como
# "No incluya nombres ni datos de salud".
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

# Reglas mínimas recomendadas para evitar reintroducir material restringido.
# Solo generan advertencia; no modifican .gitignore automáticamente.
RECOMMENDED_GITIGNORE_MARKERS = [
    "00_Restringido",
    "PENDIENTE_PRIVACIDAD_NO_SUBIR_A_GIT",
    "Fotos_Originales_Cuestionario",
]


# -----------------------------------------------------------------------------
# Estructuras auxiliares
# -----------------------------------------------------------------------------

findings: list[dict[str, str]] = []
warnings: list[dict[str, str]] = []
infos: list[dict[str, str]] = []
_seen_findings: set[tuple[str, str]] = set()
_seen_warnings: set[tuple[str, str]] = set()


def relpath(path: Path) -> str:
    """Devuelve una ruta relativa POSIX respecto de la raíz del repositorio."""
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def add_finding(code: str, path: str, detail: str) -> None:
    key = (code, path)
    if key in _seen_findings:
        return
    _seen_findings.add(key)
    findings.append({"code": code, "path": path, "detail": detail})


def add_warning(code: str, path: str, detail: str) -> None:
    key = (code, path)
    if key in _seen_warnings:
        return
    _seen_warnings.add(key)
    warnings.append({"code": code, "path": path, "detail": detail})


def add_info(code: str, path: str, detail: str) -> None:
    infos.append({"code": code, "path": path, "detail": detail})


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def public_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or should_skip(path):
            continue
        files.append(path)
    return sorted(files, key=lambda p: relpath(p).casefold())


def read_lfs_pointer(path: Path) -> dict[str, str] | None:
    """Detecta un puntero Git LFS sin descargar su contenido real."""
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

    result: dict[str, str] = {}
    for line in text.splitlines():
        if line.startswith("oid "):
            result["oid"] = line[4:].strip()
        elif line.startswith("size "):
            result["size"] = line[5:].strip()
    return result


def header_matches_sensitive_token(header: str) -> bool:
    h = header.casefold()
    for token in IDENTIFIABLE_HEADER_TOKENS:
        t = token.casefold()
        if re.search(rf"(?<!\w){re.escape(t)}(?!\w)", h):
            return True
    return False


def count_regex_in_column(rows: list[dict[str, str]], header: str, regex: re.Pattern[str]) -> int:
    count = 0
    for row in rows:
        value = (row.get(header) or "").strip()
        if value and regex.search(value):
            count += 1
    return count


# -----------------------------------------------------------------------------
# 1. Escaneo del árbol público
# -----------------------------------------------------------------------------

all_files = public_files()
files_scanned = len(all_files)
allowed_media_found: list[tuple[str, str]] = []
archives_seen: list[str] = []

for path in all_files:
    rel = relpath(path)
    suffix = path.suffix.casefold()

    # Detectar patrones incompatibles con una capa pública.
    matched_restricted_rule = False
    for code, regex, detail in RESTRICTED_PATH_RULES:
        if regex.search(rel):
            matched_restricted_rule = True
            add_finding(code, rel, detail)

    # Detectar multimedia real no clasificada.
    if suffix in MEDIA_EXTENSIONS:
        if rel in ALLOWED_PUBLIC_MEDIA:
            allowed_media_found.append((rel, ALLOWED_PUBLIC_MEDIA[rel]))
        else:
            add_finding(
                "MULTIMEDIA_NO_CLASIFICADA",
                rel,
                "archivo audiovisual no incluido en la lista pública documentada; revisar si contiene participantes o datos identificables",
            )

    # Detectar archivos comprimidos. No se extraen por seguridad/privacidad.
    if suffix in ARCHIVE_EXTENSIONS:
        archives_seen.append(rel)
        archive_name = rel.casefold()
        suspicious_archive = (
            matched_restricted_rule
            or "original" in archive_name
            or "restring" in archive_name
            or "consent" in archive_name
            or "cuestionario" in archive_name and "foto" in archive_name
        )
        if suspicious_archive:
            add_finding(
                "ARCHIVO_COMPRIMIDO_RESTRINGIDO",
                rel,
                "archivo comprimido con nombre/ruta compatible con material restringido; su contenido no se abrió automáticamente",
            )

    # Detectar punteros Git LFS hacia material restringido.
    lfs = read_lfs_pointer(path)
    if lfs and matched_restricted_rule:
        size = lfs.get("size", "desconocido")
        oid = lfs.get("oid", "desconocido")
        add_finding(
            "LFS_RESTRINGIDO_PUBLICADO",
            rel,
            f"puntero Git LFS hacia material restringido (size={size} bytes; {oid})",
        )


# -----------------------------------------------------------------------------
# 2. Escaneo de CSV públicos de 07_Datos
# -----------------------------------------------------------------------------

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
        except Exception as exc:  # El detalle técnico no incluye datos personales.
            csv_read_errors += 1
            add_warning("CSV_NO_LEIBLE", rel, f"no fue posible analizar el CSV: {type(exc).__name__}")
            continue

        if not rows or not headers:
            continue

        for header in headers:
            if header is None:
                continue

            # 2.1 Columnas explícitamente identificables con valores no vacíos.
            if header_matches_sensitive_token(header):
                nonempty = sum(1 for row in rows if (row.get(header) or "").strip())
                if nonempty:
                    add_finding(
                        "COLUMNA_IDENTIFICABLE",
                        rel,
                        f"columna={header!r}; valores_no_vacios={nonempty}",
                    )

            # 2.2 Patrones de contacto dentro de valores, sin imprimir el contenido.
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

            # Solo se usa como alerta cuando la propia cabecera sugiere un ID.
            # Esto evita confundir cantidades, fechas u otros números con cédulas.
            if header_matches_sensitive_token(header):
                id_count = count_regex_in_column(rows, header, GENERIC_10_DIGIT_RE)
                if id_count:
                    add_finding(
                        "IDENTIFICADOR_NUMERICO_EN_DATOS_PUBLICOS",
                        rel,
                        f"columna={header!r}; filas_con_identificador_probable={id_count}",
                    )


# -----------------------------------------------------------------------------
# 3. Verificación documental A6 / EXIF
# -----------------------------------------------------------------------------

exif_inventory = REPO_ROOT / "10_Autoria" / "exif_inventario.csv"
a6_records = 0
a6_valid_records = 0
a6_privacy_pending = 0
a6_invalid_details: list[str] = []

if not exif_inventory.exists():
    add_finding(
        "A6_INVENTARIO_EXIF_AUSENTE",
        relpath(exif_inventory),
        "no existe el inventario requerido para documentar fecha/dispositivo/hash de las fotografías",
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
            if not date_ok:
                missing.append("Fecha_captura_EXIF")
            if not source_date_ok:
                missing.append("Fuente_fecha_EXIF")
            if not device_ok:
                missing.append("Dispositivo_EXIF")
            if not state_ok:
                missing.append("Estado_EXIF!=OK")
            if not sha_ok:
                missing.append("SHA256 inválido")
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
            f"solo {a6_valid_records} de {a6_records} registros F3-01 tienen fecha, fuente EXIF, dispositivo, Estado_EXIF=OK y SHA-256 válido",
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
            f"{a6_privacy_pending} registros F3-01 mantienen un estado de privacidad que exige revisión/confirmación manual; esto no invalida el EXIF técnico, pero sí debe cerrarse en F3-07/B6",
        )


# Fotografías públicas del cuestionario: se cuenta su presencia, pero este script
# no afirma que tengan EXIF ni que estén autorizadas para publicación.
questionnaire_photo_dir = REPO_ROOT / "02_Evidencias" / "Cuestionario" / "Fotos_Aplicacion"
questionnaire_public_photos = []
if questionnaire_photo_dir.exists():
    questionnaire_public_photos = sorted(
        [p for p in questionnaire_photo_dir.iterdir() if p.is_file() and p.suffix.casefold() in IMAGE_EXTENSIONS],
        key=lambda p: p.name.casefold(),
    )

if len(questionnaire_public_photos) < 5:
    add_warning(
        "A6_COPIAS_PUBLICAS_INSUFICIENTES",
        relpath(questionnaire_photo_dir),
        f"se encontraron {len(questionnaire_public_photos)} fotografías públicas del cuestionario; revisar la evidencia final",
    )


# -----------------------------------------------------------------------------
# 4. Evidencia que requiere revisión visual/manual
# -----------------------------------------------------------------------------

manual_consent_pdfs = sorted(
    (REPO_ROOT / "02_Evidencias" / "Consentimientos").glob("*Censurado*.pdf")
) if (REPO_ROOT / "02_Evidencias" / "Consentimientos").exists() else []

manual_acts = sorted(
    (REPO_ROOT / "02_Evidencias" / "Validacion_walkthrough").glob("*Acta*.pdf")
) if (REPO_ROOT / "02_Evidencias" / "Validacion_walkthrough").exists() else []

team_photo_dir = REPO_ROOT / "10_Autoria" / "fotos_equipo"
team_public_photos = sorted(
    [p for p in team_photo_dir.rglob("*") if p.is_file() and p.suffix.casefold() in IMAGE_EXTENSIONS],
    key=lambda p: relpath(p).casefold(),
) if team_photo_dir.exists() else []

manual_visual_total = (
    len(manual_consent_pdfs)
    + len(manual_acts)
    + len(questionnaire_public_photos)
    + len(team_public_photos)
)


# -----------------------------------------------------------------------------
# 5. Barreras preventivas de .gitignore
# -----------------------------------------------------------------------------

gitignore = REPO_ROOT / ".gitignore"
if not gitignore.exists():
    add_warning("GITIGNORE_AUSENTE", ".gitignore", "no existe una barrera preventiva para archivos locales/restringidos")
else:
    text = gitignore.read_text(encoding="utf-8", errors="replace")
    missing_markers = [marker for marker in RECOMMENDED_GITIGNORE_MARKERS if marker not in text]
    if missing_markers:
        add_warning(
            "GITIGNORE_SIN_REGLAS_PRIVACIDAD",
            ".gitignore",
            "faltan marcadores/reglas preventivas para: " + ", ".join(missing_markers),
        )


# -----------------------------------------------------------------------------
# 6. Construcción del reporte Markdown
# -----------------------------------------------------------------------------

finding_counts = Counter(item["code"] for item in findings)
warning_counts = Counter(item["code"] for item in warnings)

status = "NO APTO PARA CIERRE AUTOMÁTICO" if findings else "SIN HALLAZGOS AUTOMÁTICOS BLOQUEANTES"

lines: list[str] = [
    "# Revisión automática de privacidad — F3-07 / B6",
    "",
    f"**Estado automático:** **{status}**.",
    "",
    "## Alcance de la auditoría",
    "",
    f"- Archivos del árbol público inspeccionados por nombre/extensión: **{files_scanned}**.",
    f"- CSV inspeccionados en `07_Datos/datos_crudos` y `datos_procesados`: **{csv_scanned}**.",
    f"- CSV no legibles durante el análisis: **{csv_read_errors}**.",
    f"- Hallazgos automáticos bloqueantes: **{len(findings)}**.",
    f"- Advertencias/documentación pendiente: **{len(warnings)}**.",
    f"- Archivos comprimidos detectados en el árbol: **{len(archives_seen)}**.",
    "",
]

if findings:
    lines += ["## Hallazgos automáticos que deben corregirse", ""]
    for item in sorted(findings, key=lambda x: (x["code"], x["path"].casefold())):
        lines.append(f"- **{item['code']}** — `{item['path']}` — {item['detail']}")
    lines.append("")
else:
    lines += [
        "## Resultado automático",
        "",
        "No se detectaron, mediante estas reglas automáticas, archivos restringidos publicados por error, "
        "multimedia no clasificada ni columnas/valores potencialmente identificables con contenido no vacío "
        "dentro de los CSV públicos analizados.",
        "",
    ]

if warnings:
    lines += ["## Advertencias y verificaciones manuales pendientes", ""]
    for item in sorted(warnings, key=lambda x: (x["code"], x["path"].casefold())):
        lines.append(f"- **{item['code']}** — `{item['path']}` — {item['detail']}")
    lines.append("")

lines += [
    "## Verificación técnica A6 — fotografías del cuestionario y EXIF",
    "",
    f"- Registros `F3-01_APLICACION_CUESTIONARIO` en `10_Autoria/exif_inventario.csv`: **{a6_records}**.",
    f"- Registros con fecha EXIF, fuente EXIF, dispositivo, `Estado_EXIF=OK` y SHA-256 válido: **{a6_valid_records}**.",
    f"- Copias fotográficas presentes en `02_Evidencias/Cuestionario/Fotos_Aplicacion/`: **{len(questionnaire_public_photos)}**.",
]

if a6_valid_records >= 5:
    lines.append("- **Resultado técnico A6:** **CUMPLE** el mínimo documental de cinco registros con metadatos EXIF válidos.")
else:
    lines.append("- **Resultado técnico A6:** **NO CUMPLE** todavía el mínimo documental de cinco registros EXIF válidos.")

if a6_invalid_details:
    lines.append("- Incidencias de metadatos: " + "; ".join(a6_invalid_details) + ".")

lines += [
    "",
    "> La comprobación técnica A6 no equivale a autorización de publicación. La clasificación [P]/[R] y el consentimiento "
    "de fotografías identificables pertenecen al cierre manual de F3-07/B6.",
    "",
    "## Multimedia pública clasificada",
    "",
]

if allowed_media_found:
    for path, reason in sorted(allowed_media_found):
        lines.append(f"- `{path}` — {reason}")
else:
    lines.append("- No se detectó multimedia incluida en la lista pública documentada.")

lines += [
    "",
    "## Revisión visual/manual requerida",
    "",
    f"- Consentimientos censurados: **{len(manual_consent_pdfs)}**.",
    f"- Actas de walkthrough: **{len(manual_acts)}**.",
    f"- Fotografías públicas de aplicación del cuestionario: **{len(questionnaire_public_photos)}**.",
    f"- Fotografías públicas del equipo/autoria: **{len(team_public_photos)}**.",
    f"- Total de piezas que requieren o pueden requerir revisión visual según su naturaleza: **{manual_visual_total}**.",
    "",
    "Este auditor no inspecciona visualmente el contenido de PDFs, imágenes o videos. Debe confirmarse manualmente que "
    "las copias censuradas/enmascaradas no revelen firmas, nombres, cédulas, teléfonos, correos, respuestas individuales "
    "u otros identificadores no autorizados.",
    "",
    "La confirmación del cifrado, custodia y acceso de la capa restringida [R] se realiza fuera de GitHub y no puede "
    "ser demostrada por este script.",
    "",
    "## Interpretación del código de salida",
    "",
    "- `0`: no hay hallazgos automáticos bloqueantes; aún deben cerrarse las revisiones humanas aplicables.",
    "- `2`: existe al menos un hallazgo automático que debe corregirse antes del release/tag final.",
]

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


# -----------------------------------------------------------------------------
# 7. Resumen por consola
# -----------------------------------------------------------------------------

print("FabroGym — auditoría de privacidad F3-07/B6")
print(f"Raíz: {REPO_ROOT}")
print(f"Archivos inspeccionados: {files_scanned}")
print(f"CSV inspeccionados: {csv_scanned}")
print(f"Hallazgos bloqueantes: {len(findings)}")
if finding_counts:
    for code, count in sorted(finding_counts.items()):
        print(f"  - {code}: {count}")
print(f"Advertencias: {len(warnings)}")
if warning_counts:
    for code, count in sorted(warning_counts.items()):
        print(f"  - {code}: {count}")
print(f"A6 EXIF válidos: {a6_valid_records}/{a6_records}")
print(f"Reporte: {OUT}")

sys.exit(2 if findings else 0)
