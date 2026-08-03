#!/usr/bin/env python3
"""Detector transparente de posibles smells en requisitos en español.

La salida es una preclasificación para revisión humana. No afirma por sí sola
que un requisito sea incorrecto o ambiguo.
"""
from __future__ import annotations
import argparse, csv, json, re
from pathlib import Path
from typing import Iterable

VERSION = "1.0.0"

RULES = {
    "SM-01": [r"\b(rápid[oa]s?|adecuad[oa]s?|suficiente(?:s)?|algunos?|varios?|muchos?|pocos?|frecuentemente|regularmente|periódicamente|pronto)\b"],
    "SM-02": [r"\b(fácil(?:mente)?|intuitiv[oa]s?|amigable(?:s)?|sencill[oa]s?|conveniente(?:s)?|óptim[oa]s?)\b"],
    "SM-03": [r"\b(este|esta|estos|estas|dicho|dicha|ello|el mismo|la misma|lo anterior)\b"],
    "SM-05": [r"\b(podrá|podrían|debería|deberían|se recomienda|cuando sea posible|en lo posible)\b"],
    "SM-06": [r"\b(etc\.?|entre otros|y similares|u otros)\b", r"y/o"],
    "SM-07": [r"\b(será|serán|deberá ser|deberán ser)\s+\w+(?:ado|ada|ados|adas|ido|ida|idos|idas)\b"],
    "SM-08": [r"\b(si aplica|según corresponda|cuando corresponda)\b"],
}

def normalize(text: str) -> str:
    return " ".join(text.lower().split())

def detect(text: str) -> tuple[list[str], dict[str, list[str]]]:
    t = normalize(text)
    details: dict[str, list[str]] = {}
    for code, patterns in RULES.items():
        matches=[]
        for p in patterns:
            matches += [m.group(0) for m in re.finditer(p, t, flags=re.I)]
        if matches:
            details[code]=sorted(set(matches))
    # Compound requirement heuristic: multiple conjunctions plus multiple verbs.
    conj = len(re.findall(r"\b(?:y|o)\b", t))
    verbs = len(re.findall(r"\b(?:permitirá|registrará|mostrará|generará|calculará|validará|actualizará|autorizará|denegará|listará|administrará|activará|renovará|buscará|consultará|alertará|resolverá|creará|asignará|cerrará|conciliará|gestionará)\b", t))
    if conj >= 3 or verbs >= 2:
        details["SM-04"]=[f"conjunciones={conj}", f"verbos_principales={verbs}"]
    return sorted(details), details

def run(input_csv: Path, output_csv: Path) -> None:
    with input_csv.open(encoding="utf-8-sig", newline="") as f:
        rows=list(csv.DictReader(f))
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8-sig", newline="") as f:
        fields=["rf_id","texto","detector_ambiguo_0_1","smells_detectados","detalle_reglas","version_detector","commit_fuente"]
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for r in rows:
            codes, details=detect(r["descripcion"])
            w.writerow({
                "rf_id":r["rf_id"], "texto":r["descripcion"],
                "detector_ambiguo_0_1":1 if codes else 0,
                "smells_detectados":";".join(codes),
                "detalle_reglas":json.dumps(details, ensure_ascii=False),
                "version_detector":VERSION, "commit_fuente":"COMPLETAR_CON_COMMIT_PRERREGISTRADO",
            })

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, default=Path("fuentes/requisitos_fabrogym_v1.5.8.csv"))
    ap.add_argument("--output", type=Path, default=Path("resultados/salida_detector.csv"))
    args=ap.parse_args(); run(args.input,args.output)
