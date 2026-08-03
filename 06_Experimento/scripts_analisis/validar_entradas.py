#!/usr/bin/env python3
"""Valida estructura, cobertura y dominios de los CSV antes del análisis."""
from __future__ import annotations
import csv
from pathlib import Path

REQUIRED_EVAL = {"evaluador_id","rf_id","orden_presentacion","ambiguo_0_no_1_si","smells_seleccionados","confianza_1_5","observacion"}

def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def validate(corpus: Path, evaluations: Path, min_evaluators: int = 3) -> None:
    crows=read_csv(corpus); erows=read_csv(evaluations)
    ids=[r["rf_id"].strip() for r in crows]
    if len(ids)!=25 or len(set(ids))!=25:
        raise ValueError(f"El corpus debe contener 25 RF únicos; se encontraron {len(ids)} filas y {len(set(ids))} IDs únicos.")
    if not erows:
        raise ValueError("La matriz de evaluaciones está vacía.")
    missing=REQUIRED_EVAL-set(erows[0])
    if missing:
        raise ValueError(f"Faltan columnas en evaluaciones: {sorted(missing)}")
    corpus_ids=set(ids); evaluators=sorted({r["evaluador_id"].strip() for r in erows if r["evaluador_id"].strip()})
    if len(evaluators)<min_evaluators:
        raise ValueError(f"Se requieren al menos {min_evaluators} evaluadores; se encontraron {len(evaluators)}.")
    for r in erows:
        if r["rf_id"].strip() not in corpus_ids:
            raise ValueError(f"RF desconocido en evaluaciones: {r['rf_id']}")
        if r["ambiguo_0_no_1_si"].strip() not in {"0","1"}:
            raise ValueError(f"Etiqueta inválida o vacía para {r['evaluador_id']} / {r['rf_id']}")
        conf=r["confianza_1_5"].strip()
        if conf and conf not in {"1","2","3","4","5"}:
            raise ValueError(f"Confianza inválida para {r['evaluador_id']} / {r['rf_id']}")
    for ev in evaluators:
        rows=[r for r in erows if r["evaluador_id"].strip()==ev]
        seen={r["rf_id"].strip() for r in rows}
        if seen!=corpus_ids:
            raise ValueError(f"{ev} no cubre exactamente los 25 RF: cubre {len(seen)}.")
        if len(rows)!=25:
            raise ValueError(f"{ev} tiene {len(rows)} filas; se esperaban 25.")

if __name__=="__main__":
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("--corpus",type=Path,default=Path("fuentes/requisitos_fabrogym_v1.5.8.csv"))
    ap.add_argument("--evaluaciones",type=Path,default=Path("resultados/evaluaciones_expertos.csv"))
    args=ap.parse_args(); validate(args.corpus,args.evaluaciones); print("Validación correcta.")
