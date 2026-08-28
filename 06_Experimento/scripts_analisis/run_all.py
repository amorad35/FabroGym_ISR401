#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse
from pathlib import Path
from analizar_walkthroughs import procesar as procesar_walkthroughs
from analizar_rnf import procesar as procesar_rnf
from analizar_member_checking import procesar as procesar_mc

def main():
    p=argparse.ArgumentParser(description='Ejecuta los análisis disponibles del Enfoque 3 de FabroGym.')
    p.add_argument('--salida',required=True,type=Path)
    p.add_argument('--codificacion',type=Path)
    p.add_argument('--rnf',type=Path)
    p.add_argument('--member-checking',type=Path)
    p.add_argument('--total-dimensiones',type=int,default=None)
    a=p.parse_args()
    if not any([a.codificacion,a.rnf,a.member_checking]): p.error('Indique al menos una entrada real disponible.')
    a.salida.mkdir(parents=True,exist_ok=True)
    if a.codificacion: procesar_walkthroughs(a.codificacion,a.salida)
    if a.rnf: procesar_rnf(a.rnf,a.salida,a.total_dimensiones)
    if a.member_checking: procesar_mc(a.member_checking,a.salida)
    print('Procesamiento completado con las entradas disponibles.')
if __name__=='__main__': main()
