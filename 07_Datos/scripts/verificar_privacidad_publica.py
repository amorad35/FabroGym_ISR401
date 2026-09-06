#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FabroGym F3-07 — auditoría preventiva de privacidad.

Ejecutar desde cualquier ubicación:
    python 07_Datos/scripts/verificar_privacidad_publica.py

Genera:
    07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md

No imprime ni copia valores personales; solo reporta rutas, columnas y conteos.
"""
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "07_Datos" / "resultados" / "REVISION_PRIVACIDAD_PUBLICA.md"
OUT.parent.mkdir(parents=True, exist_ok=True)

MEDIA = {".mp3",".wav",".m4a",".aac",".flac",".mp4",".mov",".avi",".mkv",".webm"}
NAME_PATTERNS = [
    re.compile(r"consentimiento[_ -]original", re.I),
    re.compile(r"consentimiento[_ -]firmad", re.I),
    re.compile(r"\bcedula\b|\bc[eé]dula\b", re.I),
    re.compile(r"transcripcion[_ -]sin[_ -]anonim", re.I),
    re.compile(r"datos[_ -]identificables", re.I),
]
TOKENS = [
    "nombre","name","correo","email","telefono","teléfono","phone",
    "cedula","cédula","direccion","dirección","address",
    "documento_identidad","id_number"
]

findings = []
files_scanned = 0
csv_scanned = 0

for p in ROOT.rglob("*"):
    if not p.is_file() or ".git" in p.parts:
        continue
    files_scanned += 1
    rel = p.relative_to(ROOT).as_posix()
    if p.suffix.lower() in MEDIA:
        findings.append(("ARCHIVO_MULTIMEDIA", rel, "archivo audiovisual presente en el árbol público"))
    if any(rx.search(rel) for rx in NAME_PATTERNS):
        findings.append(("NOMBRE_RESTRINGIDO", rel, "nombre compatible con evidencia original/restringida"))

for folder_name in ("datos_crudos","datos_procesados"):
    folder = ROOT / "07_Datos" / folder_name
    if not folder.exists():
        continue
    for p in sorted(folder.glob("*.csv")):
        csv_scanned += 1
        try:
            with p.open("r", encoding="utf-8-sig", newline="") as f:
                rows = list(csv.DictReader(f))
        except Exception:
            continue
        if not rows:
            continue
        for h in rows[0].keys():
            hn = h.casefold()
            if any(tok in hn for tok in TOKENS):
                nonempty = sum(1 for r in rows if (r.get(h) or "").strip())
                if nonempty:
                    findings.append((
                        "COLUMNA_IDENTIFICABLE",
                        p.relative_to(ROOT).as_posix(),
                        f"columna={h}; valores_no_vacios={nonempty}"
                    ))

manual_pdfs = (
    list((ROOT/"02_Evidencias/Consentimientos").glob("*Censurado*.pdf"))
    if (ROOT/"02_Evidencias/Consentimientos").exists() else []
)
manual_acts = (
    list((ROOT/"02_Evidencias/Validacion_walkthrough").glob("*Acta*.pdf"))
    if (ROOT/"02_Evidencias/Validacion_walkthrough").exists() else []
)

lines = [
    "# Revisión automática de privacidad — F3-07",
    "",
    f"- Archivos del árbol público inspeccionados por nombre/extensión: **{files_scanned}**.",
    f"- CSV de `07_Datos/datos_crudos` y `datos_procesados` inspeccionados: **{csv_scanned}**.",
    f"- Hallazgos automáticos: **{len(findings)}**.",
    f"- PDFs censurados/actas que requieren revisión visual adicional: **{len(manual_pdfs) + len(manual_acts)}**.",
    "",
]
if findings:
    lines += ["## Hallazgos", ""]
    for kind, path, detail in findings:
        lines.append(f"- **{kind}** — `{path}` — {detail}")
else:
    lines += [
        "## Resultado",
        "",
        "No se detectaron, mediante estas reglas automáticas, archivos audiovisuales reales, "
        "nombres de archivos reservados para evidencia restringida ni columnas potencialmente "
        "identificables con valores no vacíos dentro de los CSV públicos de `07_Datos`.",
    ]

lines += [
    "",
    "## Revisión manual obligatoria",
    "",
    "Este resultado no inspecciona visualmente el contenido de PDFs, imágenes o fotografías. "
    "Las copias censuradas, actas enmascaradas y fotografías F3-01 deben revisarse antes del release.",
    "",
    "La confirmación del cifrado y acceso de la capa restringida se realiza fuera de GitHub.",
]
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"Archivos inspeccionados: {files_scanned}")
print(f"CSV inspeccionados: {csv_scanned}")
print(f"Hallazgos: {len(findings)}")
print(f"Reporte: {OUT}")

sys.exit(2 if findings else 0)
