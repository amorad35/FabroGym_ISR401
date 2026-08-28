#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse, csv
from pathlib import Path

CODIFICACION_COLUMNS = [
    'ID_Registro','Codigo_Sesion','Codigo_Participante','Perfil','Fuente_Evidencia',
    'Ubicacion_Evidencia','Fragmento_Anonimizado','Necesidad_Explicabilidad',
    'Dimension','Candidato_RNF_Relacionado','Observaciones'
]
RNF_COLUMNS = ['ID','Enunciado_RNF','Fuente','Perfil','Dimension','Criterio_Aceptacion','Observaciones']
MC_COLUMNS = ['ID','Resultado','Observaciones']
PERFILES = {'T','NT','Tecnico','Técnico','No tecnico','No técnico','No_verificable','No verificable',''}
MC_RESULTADOS = {'Confirmado','Ajustado','No confirmado',''}

def read_rows(path: Path):
    if not path.exists():
        raise FileNotFoundError(f'No existe el archivo: {path}')
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)

def validate_columns(path: Path, required):
    fields, rows = read_rows(path)
    missing = [c for c in required if c not in fields]
    if missing:
        raise ValueError(f'{path.name}: faltan columnas: {", ".join(missing)}')
    return rows

def validar_codificacion(path: Path):
    rows = validate_columns(path, CODIFICACION_COLUMNS)
    ids = set()
    for n,row in enumerate(rows, start=2):
        rid=(row.get('ID_Registro') or '').strip()
        if rid:
            if rid in ids: raise ValueError(f'{path.name}: ID_Registro duplicado {rid!r} en fila {n}')
            ids.add(rid)
        perfil=(row.get('Perfil') or '').strip()
        if perfil not in PERFILES:
            raise ValueError(f'{path.name}: perfil no reconocido {perfil!r} en fila {n}')
    return rows

def validar_rnf(path: Path):
    rows = validate_columns(path, RNF_COLUMNS)
    ids=set()
    for n,row in enumerate(rows, start=2):
        rid=(row.get('ID') or '').strip()
        if rid:
            if rid in ids: raise ValueError(f'{path.name}: ID duplicado {rid!r} en fila {n}')
            ids.add(rid)
        perfil=(row.get('Perfil') or '').strip()
        if perfil not in PERFILES:
            raise ValueError(f'{path.name}: perfil no reconocido {perfil!r} en fila {n}')
    return rows

def validar_member_checking(path: Path):
    rows = validate_columns(path, MC_COLUMNS)
    for n,row in enumerate(rows, start=2):
        result=(row.get('Resultado') or '').strip()
        if result not in MC_RESULTADOS:
            raise ValueError(f'{path.name}: resultado no reconocido {result!r} en fila {n}')
    return rows

def main():
    p=argparse.ArgumentParser(description='Valida matrices del Enfoque 3 de FabroGym.')
    p.add_argument('--codificacion', type=Path)
    p.add_argument('--rnf', type=Path)
    p.add_argument('--member-checking', type=Path)
    a=p.parse_args()
    if not any([a.codificacion,a.rnf,a.member_checking]): p.error('Indique al menos un archivo.')
    if a.codificacion: print(f'Codificación válida: {len(validar_codificacion(a.codificacion))} filas.')
    if a.rnf: print(f'Matriz RNF válida: {len(validar_rnf(a.rnf))} filas.')
    if a.member_checking: print(f'Member checking válido: {len(validar_member_checking(a.member_checking))} filas.')
if __name__ == '__main__': main()
