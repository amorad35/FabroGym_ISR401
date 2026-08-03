#!/usr/bin/env python3
"""Validaciones estructurales y de privacidad básica para el paquete abierto."""
from pathlib import Path
import csv, json, re, sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]
warnings=[]

def load_csv(name):
    with (ROOT/name).open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))

survey=load_csv("respuestas_cuestionario.csv")
if len(survey)!=32:
    errors.append(f"respuestas_cuestionario.csv: se esperaban 32 filas y hay {len(survey)}")
ids=[r["id_respuesta"] for r in survey]
if len(ids)!=len(set(ids)):
    errors.append("IDs de encuesta duplicados")
if ids and (ids[0]!="ENC-CLI-001" or ids[-1]!="ENC-CLI-032"):
    warnings.append("El rango de IDs no coincide con ENC-CLI-001..032")

matrix=load_csv("matriz_trazabilidad.csv")
mids=[r["ID"] for r in matrix]
if len(matrix)!=44:
    errors.append(f"matriz: se esperaban 44 filas y hay {len(matrix)}")
if len(mids)!=len(set(mids)):
    errors.append("La matriz contiene identificadores duplicados")

corpus=json.loads((ROOT/"corpus_requisitos.json").read_text(encoding="utf-8"))
if corpus["counts"]["total"]!=44:
    errors.append("corpus_requisitos.json no registra 44 elementos")

# Detección conservadora de posibles números de cédula ecuatoriana en archivos públicos.
cedula=re.compile(r"(?<!\d)\d{10}(?!\d)")
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".csv",".json",".md",".txt",".cff"}:
        text=path.read_text(encoding="utf-8-sig",errors="ignore")
        hits=cedula.findall(text)
        # Se excluyen años/IDs técnicos; cualquier hallazgo de 10 dígitos se revisa manualmente.
        if hits:
            warnings.append(f"Revisar posible secuencia de 10 dígitos en {path.relative_to(ROOT)}")

print("VALIDACIÓN DEL PAQUETE")
for w in warnings:
    print("ADVERTENCIA:",w)
for e in errors:
    print("ERROR:",e)
if errors:
    sys.exit(1)
print("Estado: estructura válida; revisión manual de privacidad todavía obligatoria.")
