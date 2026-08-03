#!/usr/bin/env python3
"""Ejecuta el flujo completo únicamente DESPUÉS del prerregistro OSF."""
from pathlib import Path
from detector_ambiguedad import run as run_detector
from preparar_consenso import run as run_consensus
from validar_entradas import validate
from analizar_resultados import run as run_analysis

ROOT=Path(__file__).resolve().parents[1]

def main():
    pending=ROOT/"PENDIENTE_osf_registration.md"
    osf=ROOT/"osf_registration.pdf"
    if pending.exists() or not osf.exists():
        raise SystemExit("Ejecución bloqueada: falta osf_registration.pdf real o permanece el marcador PENDIENTE.")
    eval_file=ROOT/"resultados"/"evaluaciones_expertos.csv"
    if not eval_file.exists():
        raise SystemExit("Falta resultados/evaluaciones_expertos.csv completado.")
    corpus=ROOT/"fuentes"/"requisitos_fabrogym_v1.5.8.csv"
    validate(corpus,eval_file,min_evaluators=3)
    run_detector(corpus,ROOT/"resultados"/"salida_detector.csv")
    run_consensus(eval_file,ROOT/"resultados"/"consenso_experto.csv")
    run_analysis(ROOT/"resultados"/"salida_detector.csv",eval_file,ROOT/"resultados"/"consenso_experto.csv",ROOT/"resultados")
    print("Análisis completado. Revise resultados/ y resultados/figuras/.")

if __name__=="__main__": main()
