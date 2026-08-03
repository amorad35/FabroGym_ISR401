#!/usr/bin/env python3
"""Prueba técnica con datos ficticios. No ejecuta ni etiqueta el corpus real."""
from __future__ import annotations
import csv, tempfile
from pathlib import Path
from detector_ambiguedad import run as run_detector
from preparar_consenso import run as run_consensus
from analizar_resultados import run as run_analysis

SYNTH=[
    ("SYN-01","El sistema mostrará el reporte en menos de 2 segundos."),
    ("SYN-02","El sistema será fácil e intuitivo."),
    ("SYN-03","El sistema registrará el pago y generará el comprobante."),
    ("SYN-04","El sistema deberá procesar algunos registros rápidamente."),
    ("SYN-05","El sistema almacenará el código interno del usuario."),
    ("SYN-06","El sistema podrá enviar avisos cuando sea posible."),
]
LABELS={"SYN-01":0,"SYN-02":1,"SYN-03":1,"SYN-04":1,"SYN-05":0,"SYN-06":1}

def main():
    with tempfile.TemporaryDirectory(prefix="fabrogym_sintetico_") as td:
        d=Path(td); corpus=d/"corpus.csv"; ev=d/"evaluaciones.csv"; det=d/"detector.csv"; con=d/"consenso.csv"; out=d/"resultados"
        with corpus.open("w",encoding="utf-8-sig",newline="") as f:
            w=csv.DictWriter(f,fieldnames=["rf_id","descripcion"]); w.writeheader(); [w.writerow({"rf_id":i,"descripcion":t}) for i,t in SYNTH]
        with ev.open("w",encoding="utf-8-sig",newline="") as f:
            fields=["evaluador_id","rf_id","orden_presentacion","ambiguo_0_no_1_si","smells_seleccionados","confianza_1_5","observacion"]
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
            for e in range(1,4):
                for pos,(rid,_) in enumerate(SYNTH,1):
                    w.writerow({"evaluador_id":f"EXP-{e:02d}","rf_id":rid,"orden_presentacion":pos,"ambiguo_0_no_1_si":LABELS[rid],"smells_seleccionados":"","confianza_1_5":4,"observacion":"dato sintético"})
        run_detector(corpus,det); run_consensus(ev,con); run_analysis(det,ev,con,out)
        required=["metricas_detector.csv","matriz_confusion.csv","prueba_mcnemar.csv","kappa_pares.csv","kappa_fleiss.csv","desacuerdos.csv"]
        missing=[x for x in required if not (out/x).exists()]
        if missing: raise SystemExit(f"Prueba sintética incompleta: {missing}")
        print("Prueba sintética correcta. El entorno y los scripts funcionan sin usar el corpus real.")

if __name__=="__main__": main()
