#!/usr/bin/env python3
"""Recalcula frecuencias descriptivas del cuestionario FabroGym."""
from pathlib import Path
from collections import Counter
import csv, json
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "respuestas_cuestionario.csv"
OUT = ROOT / "resultados"
FIG = OUT / "figuras"
OUT.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)

with INPUT.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

N = len(rows)
if N != 32:
    raise ValueError(f"Se esperaban 32 respuestas; se encontraron {N}.")

categorical = [
    "frecuencia_asistencia","antiguedad_gimnasio","consulta_membresia",
    "dificultad_vencimiento","espera_confirmacion_pago","medio_preferido_avisos",
    "facilidad_inscripcion_actualizacion","claridad_planes_precios",
    "satisfaccion_atencion","registro_ingreso","consulta_cambio_rutina",
    "informacion_futuro_sistema","dificultades_compra_productos",
    "prioridad_mejora","importancia_privacidad"
]

summary = {}
with (OUT/"frecuencias_encuesta.csv").open("w",encoding="utf-8-sig",newline="") as f:
    w=csv.writer(f)
    w.writerow(["variable","opcion","frecuencia","porcentaje"])
    for var in categorical:
        c=Counter(r[var] for r in rows)
        summary[var]=[]
        for opt,n in c.most_common():
            pct=round(n/N*100,2)
            w.writerow([var,opt,n,pct])
            summary[var].append({"opcion":opt,"n":n,"porcentaje":pct})

(OUT/"resumen_encuesta.json").write_text(
    json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8"
)

def chart(var,title,filename):
    c=Counter(r[var] for r in rows)
    labels=[x for x,_ in c.most_common()]
    values=[n for _,n in c.most_common()]
    plt.figure(figsize=(9,5.5))
    plt.barh(labels[::-1],values[::-1])
    plt.xlabel(f"Frecuencia (n = {N})")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(FIG/filename,dpi=200,bbox_inches="tight")
    plt.close()

chart("prioridad_mejora","Prioridad de mejora señalada por las personas encuestadas","prioridades_mejora.png")
chart("medio_preferido_avisos","Medio preferido para avisos de vencimiento","medios_avisos.png")
chart("importancia_privacidad","Importancia atribuida a la privacidad de los datos","importancia_privacidad.png")
chart("consulta_membresia","Medio actual de consulta del estado de membresía","consulta_membresia.png")

print(f"Encuesta analizada: n={N}.")
