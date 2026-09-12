# FAIR_CHECKLIST — FabroGym 2B

Este archivo documenta el estado FAIR verificable del cierre con evidencia real obtenida el **11 de septiembre de 2026**.

## Estado actual

| Área FAIR | Comprobación | Evidencia | Estado |
|---|---|---|---|
| F | Identificador persistente | Zenodo v2.0.0 — DOI `10.5281/zenodo.22237884` | VERIFICADO |
| F | Título, descripción, autores y palabras clave | metadatos Zenodo + `CITATION.cff` | VERIFICADO |
| F | Citación legible por máquina | `CITATION.cff` v1.2.0 con DOI, OSF y SWHID | VERIFICADO |
| F | Descubribilidad | GitHub + OSF + Zenodo + Software Heritage | VERIFICADO |
| A | Datos públicos anonimizados | paquete publicado | DISPONIBLE |
| A | Evidencia restringida excluida | política pública/restringida | DISPONIBLE |
| A | Licencias explícitas | CC BY 4.0 datos/documentación; MIT código | DISPONIBLE |
| I | Formatos abiertos y estructurados | CSV, JSON, TXT, MD, SVG | DISPONIBLE |
| I | Identificadores estables | ENTR, WALK, MC, RF, RNF y RD | DISPONIBLE |
| I | Diccionario de datos | `07_Datos/diccionario_datos.csv` | DISPONIBLE |
| R | Proveniencia | `07_Datos/datos_crudos/PROVENIENCIA_FUENTES.md` + OSF | DISPONIBLE |
| R | Reproducibilidad | `07_Datos/scripts/run_all.py` + `requirements.txt` | VERIFICADA |
| R | Versionado | Zenodo 2.0.0 + Git + CHANGELOG + checksums | DISPONIBLE |
| R | Evaluación FAIR externa | `fair_assessment.pdf` — F-UJI 4.0.0, métrica 0.8 | **VERIFICADO: 88 %, FAIR moderate** |
| R | Preservación del software | Software Heritage snapshot `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e` | **VERIFICADO COMO SNAPSHOT ARCHIVADO** |

## Resultado F-UJI

**Recurso evaluado:** *Replication package for Explainability Requirements for Fitness Routine Recommendations: A Field Case Study in Ecuador*  
**PID:** `10.5281/zenodo.22237884`  
**Fecha:** 2026-09-11  
**F-UJI:** 4.0.0 · **Métrica:** 0.8  
**Resultado global:** **88 % — FAIR level: moderate**

| Dimensión | Puntaje | Nivel |
|---|---:|---|
| Findable | 7/7 | advanced |
| Accessible | 6/7 | moderate |
| Interoperable | 4/6 | moderate |
| Reusable | 6/6 | moderate |

La evidencia se conserva sin alteraciones como `fair_assessment.pdf`.

## Software Heritage

- Origin: `https://github.com/amorad35/FabroGym_ISR401`
- Snapshot SWHID: `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e`
- Revision archivada: `swh:1:rev:56ae64739c8dfcb93de77b9085afaf74b029e5fd`
- Directory SWHID: `swh:1:dir:864d5a537b9e2fa6931f7f2b3ad23a06275432fa`
- Permalink: `https://archive.softwareheritage.org/swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e;origin=https://github.com/amorad35/FabroGym_ISR401`

### Advertencia de cierre

El snapshot archivado muestra como revisión `56ae64739c8dfcb93de77b9085afaf74b029e5fd`. Sin embargo, el `main` actual ya contiene commits posteriores, incluido `d4e34c1cf763728a6938b0fc99f9f76f20a0f095`. Por ello, el SWHID es **real y verificable**, pero todavía no debe describirse como la versión final congelada. Después del último commit y del tag final debe ejecutarse **Save again** y registrarse el SWHID definitivo si cambia.

## Pendientes estrictos

1. Subir cualquier artefacto final aún pendiente (MVP responsive y/o video si todavía faltan).
2. Ejecutar clon limpio y generar `10_Autoria/verificacion_previa.pdf`.
3. Regenerar `checksums.sha256` al final.
4. Hacer commit final y tag anotado.
5. Ejecutar Software Heritage → **Save again** sobre el estado congelado.
