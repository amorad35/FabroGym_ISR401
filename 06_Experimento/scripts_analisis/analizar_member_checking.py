#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse, csv
from collections import Counter
from pathlib import Path
from validar_entradas import validar_member_checking

def procesar(entrada: Path, salida: Path):
    rows=validar_member_checking(entrada)
    salida.mkdir(parents=True,exist_ok=True)
    if not rows:
        print('La matriz de member checking no contiene decisiones. No se generan resultados empíricos.')
        return
    c=Counter((r.get('Resultado') or '').strip() for r in rows if (r.get('Resultado') or '').strip())
    with (salida/'resumen_member_checking.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['Resultado','Conteo'])
        for result in ['Confirmado','Ajustado','No confirmado']:
            w.writerow([result,c.get(result,0)])
    print(f'Decisiones de member checking procesadas: {sum(c.values())}')

def main():
    p=argparse.ArgumentParser(description='Resume decisiones reales de member checking.')
    p.add_argument('--entrada',required=True,type=Path); p.add_argument('--salida',required=True,type=Path)
    a=p.parse_args(); procesar(a.entrada,a.salida)
if __name__=='__main__': main()
