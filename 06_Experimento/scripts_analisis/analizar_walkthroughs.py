#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse, csv
from collections import Counter
from pathlib import Path
from validar_entradas import validar_codificacion

def norm_profile(v):
    v=(v or '').strip().lower()
    if v in {'t','tecnico','técnico'}: return 'Técnico'
    if v in {'nt','no tecnico','no técnico'}: return 'No técnico'
    if not v or v in {'no_verificable','no verificable'}: return 'No verificable'
    return v

def write_counter(path, header1, counter):
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w=csv.writer(f); w.writerow([header1,'Conteo'])
        for key,count in sorted(counter.items(), key=lambda x:(str(x[0]),x[1])):
            w.writerow([key,count])

def procesar(entrada: Path, salida: Path):
    rows=validar_codificacion(entrada)
    salida.mkdir(parents=True, exist_ok=True)
    if not rows:
        print('La matriz de codificación no contiene datos. No se generan resultados empíricos.')
        return
    perfiles=Counter(); necesidades=Counter(); dimensiones=Counter(); perfil_dimension=Counter()
    processed=[]
    for r in rows:
        perfil=norm_profile(r.get('Perfil'))
        necesidad=(r.get('Necesidad_Explicabilidad') or '').strip()
        dimension=(r.get('Dimension') or '').strip()
        if perfil: perfiles[perfil]+=1
        if necesidad: necesidades[necesidad]+=1
        if dimension:
            dimensiones[dimension]+=1
            perfil_dimension[(perfil,dimension)]+=1
        rr=dict(r); rr['Perfil_Normalizado']=perfil; processed.append(rr)
    if rows:
        fields=list(rows[0].keys())+['Perfil_Normalizado']
    else:
        fields=['ID_Registro','Codigo_Sesion','Codigo_Participante','Perfil','Fuente_Evidencia','Ubicacion_Evidencia','Fragmento_Anonimizado','Necesidad_Explicabilidad','Dimension','Candidato_RNF_Relacionado','Observaciones','Perfil_Normalizado']
    with (salida/'codificacion_walkthroughs_procesada.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(processed)
    write_counter(salida/'resumen_necesidades.csv','Necesidad_Explicabilidad',necesidades)
    write_counter(salida/'resumen_dimensiones.csv','Dimension',dimensiones)
    with (salida/'resumen_necesidades_por_perfil.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['Perfil','Unidades_Codificadas'])
        for k,v in sorted(perfiles.items()): w.writerow([k,v])
    with (salida/'resumen_perfil_dimension.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['Perfil','Dimension','Conteo'])
        for (perfil,dim),v in sorted(perfil_dimension.items()): w.writerow([perfil,dim,v])
    print(f'Unidades codificadas procesadas: {len(rows)}')

def main():
    p=argparse.ArgumentParser(description='Resume la codificación de walkthroughs de FabroGym.')
    p.add_argument('--entrada',required=True,type=Path); p.add_argument('--salida',required=True,type=Path)
    a=p.parse_args(); procesar(a.entrada,a.salida)
if __name__=='__main__': main()
