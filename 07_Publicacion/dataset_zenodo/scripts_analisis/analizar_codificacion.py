#!/usr/bin/env python3
"""Recalcula frecuencias de códigos y la curva descriptiva de códigos acumulados."""
from pathlib import Path
from collections import Counter
import csv
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"resultados"
FIG=OUT/"figuras"
OUT.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)

def load(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))

rows=load(ROOT/"codificacion_tematica.csv")
thematic=[r for r in rows if r["Tipo_codigo"]=="CODIGO_TEMATICO"]
counts=Counter(r["Codigo"] for r in thematic)

with (OUT/"frecuencias_codigos.csv").open("w",encoding="utf-8-sig",newline="") as f:
    w=csv.writer(f); w.writerow(["codigo","frecuencia_fragmentos","entrevistas"])
    for code,n in counts.most_common():
        interviews=sorted({r["Transcripcion"] for r in thematic if r["Codigo"]==code})
        w.writerow([code,n,";".join(interviews)])

labels=[k for k,_ in counts.most_common()]
values=[n for _,n in counts.most_common()]
plt.figure(figsize=(10,7))
plt.barh(labels[::-1],values[::-1])
plt.xlabel("Fragmentos codificados")
plt.title("Frecuencia de códigos temáticos")
plt.tight_layout()
plt.savefig(FIG/"frecuencias_codigos.png",dpi=200,bbox_inches="tight")
plt.close()

curve=load(OUT/"curva_saturacion.csv")
x=[r["entrevista"] for r in curve]
new=[int(r["codigos_tematicos_nuevos"]) for r in curve]
cum=[int(r["codigos_tematicos_acumulados"]) for r in curve]
plt.figure(figsize=(9,5.5))
plt.plot(x,cum,marker="o",label="Códigos acumulados")
plt.bar(x,new,alpha=0.35,label="Códigos nuevos")
plt.ylabel("Número de códigos")
plt.xlabel("Entrevista")
plt.title("Curva descriptiva de códigos (no demuestra saturación teórica)")
plt.xticks(rotation=35,ha="right")
plt.legend()
plt.tight_layout()
plt.savefig(FIG/"curva_saturacion.png",dpi=200,bbox_inches="tight")
plt.close()

print(f"Codificación analizada: {len(rows)} fragmentos; {len(counts)} códigos temáticos.")
