#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse, csv
from collections import Counter
from pathlib import Path
from validar_entradas import validar_rnf

def norm_profile(v):
    v=(v or '').strip().lower()
    if v in {'t','tecnico','técnico'}: return 'Técnico'
    if v in {'nt','no tecnico','no técnico'}: return 'No técnico'
    if not v or v in {'no_verificable','no verificable'}: return 'No verificable'
    return v

def procesar(entrada: Path, salida: Path, total_dimensiones: int | None = None):
    rows=validar_rnf(entrada)
    salida.mkdir(parents=True,exist_ok=True)
    if not rows:
        print('La matriz de candidatos RNF no contiene datos. No se generan resultados empíricos.')
        return
    perfil=Counter(); dim=Counter(); verificables=[]
    for r in rows:
        perfil[norm_profile(r.get('Perfil'))]+=1
        d=(r.get('Dimension') or '').strip()
        if d: dim[d]+=1
        verificable=all((r.get(c) or '').strip() for c in ['Enunciado_RNF','Fuente','Criterio_Aceptacion'])
        if verificable: verificables.append(r)
    with (salida/'resumen_candidatos_rnf.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['Metrica','Valor'])
        w.writerow(['Candidatos_registrados',len(rows)])
        w.writerow(['Candidatos_verificables',len(verificables)])
        w.writerow(['Dimensiones_con_al_menos_un_candidato_verificable',len({(r.get('Dimension') or '').strip() for r in verificables if (r.get('Dimension') or '').strip()})])
    with (salida/'candidatos_por_perfil.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['Perfil','Conteo']); [w.writerow([k,v]) for k,v in sorted(perfil.items())]
    with (salida/'candidatos_por_dimension.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['Dimension','Conteo']); [w.writerow([k,v]) for k,v in sorted(dim.items())]
    coverage_path=salida/'cobertura_dimensiones.csv'
    with coverage_path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['Metrica','Valor','Estado'])
        covered=len({(r.get('Dimension') or '').strip() for r in verificables if (r.get('Dimension') or '').strip()})
        if total_dimensiones and total_dimensiones>0:
            w.writerow(['Dimensiones_cubiertas',covered,'Calculable'])
            w.writerow(['Total_dimensiones_evaluadas',total_dimensiones,'Calculable'])
            w.writerow(['Proporcion_cobertura',covered/total_dimensiones,'Calculable'])
        else:
            w.writerow(['Dimensiones_cubiertas',covered,'Descriptivo'])
            w.writerow(['Proporcion_cobertura','','No calculable: no se proporcionó un denominador verificable'])
    print(f'Candidatos RNF procesados: {len(rows)}')

def main():
    p=argparse.ArgumentParser(description='Resume candidatos RNF de explicabilidad.')
    p.add_argument('--entrada',required=True,type=Path); p.add_argument('--salida',required=True,type=Path)
    p.add_argument('--total-dimensiones',type=int,default=None,help='Denominador verificable; omitir si no está establecido.')
    a=p.parse_args(); procesar(a.entrada,a.salida,a.total_dimensiones)
if __name__=='__main__': main()
