#!/usr/bin/env python3
"""Genera órdenes aleatorizados reproducibles para las matrices de evaluación."""
from __future__ import annotations
import argparse, csv, random
from pathlib import Path

def run(corpus: Path, output: Path, evaluators: int, seed: int) -> None:
    with corpus.open(encoding="utf-8-sig",newline="") as f:
        ids=[r["rf_id"] for r in csv.DictReader(f)]
    if len(ids)!=25 or len(set(ids))!=25:
        raise ValueError("El corpus debe contener exactamente 25 RF únicos.")
    rows=[]
    for n in range(1,evaluators+1):
        order=ids.copy(); random.Random(seed+n).shuffle(order)
        for pos,rf in enumerate(order,1):
            rows.append({"evaluador_id":f"EXP-{n:02d}","rf_id":rf,"orden_presentacion":pos,"ambiguo_0_no_1_si":"","smells_seleccionados":"","confianza_1_5":"","observacion":""})
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--corpus",type=Path,default=Path("fuentes/requisitos_fabrogym_v1.5.8.csv"))
    ap.add_argument("--output",type=Path,default=Path("instrumentos/03_Matriz_Evaluacion_Expertos.csv"))
    ap.add_argument("--evaluadores",type=int,default=3)
    ap.add_argument("--semilla",type=int,default=401)
    a=ap.parse_args(); run(a.corpus,a.output,a.evaluadores,a.semilla)
