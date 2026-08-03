#!/usr/bin/env python3
"""Consolida evaluaciones expertas y calcula mayoría simple por RF."""
from __future__ import annotations
import argparse, csv
from pathlib import Path

def run(input_csv: Path, output_csv: Path) -> None:
    with input_csv.open(encoding="utf-8-sig", newline="") as f:
        rows=list(csv.DictReader(f))
    evaluators=sorted({r["evaluador_id"].strip() for r in rows})
    by={}
    for r in rows:
        label=r.get("ambiguo_0_no_1_si","").strip()
        if label not in {"0","1"}:
            raise ValueError(f"Etiqueta inválida para {r.get('evaluador_id')} / {r.get('rf_id')}")
        by.setdefault(r["rf_id"],[]).append(int(label))
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8-sig", newline="") as f:
        fields=["rf_id","n_evaluadores","votos_ambiguo","votos_no_ambiguo","consenso_ambiguo_0_1","regla_consenso","observacion_adjudicacion"]
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for rf_id, labels in sorted(by.items()):
            if len(labels)!=len(evaluators):
                raise ValueError(f"{rf_id} tiene {len(labels)} evaluaciones; se esperaban {len(evaluators)}.")
            pos=sum(labels); neg=len(labels)-pos
            consensus="" if pos==neg else int(pos>neg)
            w.writerow({"rf_id":rf_id,"n_evaluadores":len(labels),"votos_ambiguo":pos,"votos_no_ambiguo":neg,"consenso_ambiguo_0_1":consensus,"regla_consenso":"mayoría simple","observacion_adjudicacion":"ADJUDICAR" if consensus=="" else ""})

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--input",type=Path,default=Path("resultados/evaluaciones_expertos.csv")); ap.add_argument("--output",type=Path,default=Path("resultados/consenso_experto.csv")); a=ap.parse_args(); run(a.input,a.output)
