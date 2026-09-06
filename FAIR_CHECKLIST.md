# FAIR_CHECKLIST — FabroGym 2B

Este archivo documenta el estado FAIR verificable del cierre. **No es un puntaje F-UJI** y no declara porcentajes mientras la evaluación externa no haya sido ejecutada y conservada como evidencia.

## Estado actual

| Área FAIR | Comprobación | Evidencia | Estado |
|---|---|---|---|
| F | Identificador persistente | Zenodo v2.0.0 — DOI `10.5281/zenodo.22237884` | VERIFICADO |
| F | Título, descripción, autores y palabras clave | metadatos del depósito + `CITATION.cff` | DISPONIBLE |
| F | Citación legible por máquina | `CITATION.cff` v1.2.0 con DOI Zenodo | DISPONIBLE |
| F | Descubribilidad | GitHub + OSF + Zenodo | DISPONIBLE |
| A | Datos públicos sin evidencia identificable | paquete anonimizado | DISPONIBLE, sujeto a revisión final de privacidad |
| A | Evidencia restringida excluida | política de zonas públicas/restringidas + licencias | DISPONIBLE |
| A | Licencias explícitas | CC BY 4.0 para datos/documentación; MIT para código | DISPONIBLE |
| I | Formatos abiertos y estructurados | CSV, JSON, TXT, MD, SVG | DISPONIBLE |
| I | Identificadores estables | ENTR, WALK, MC, RF, RNF y RD | DISPONIBLE |
| I | Diccionario de datos | `07_Datos/diccionario_datos.csv` | DISPONIBLE |
| R | Proveniencia | `07_Datos/datos_crudos/PROVENIENCIA_FUENTES.md` + desviaciones OSF | DISPONIBLE |
| R | Reproducibilidad | `07_Datos/scripts/run_all.py` + `requirements.txt` | VERIFICADA |
| R | Versionado | Zenodo 2.0.0 + Git + CHANGELOG + manifiestos/checksums | DISPONIBLE |
| R | Evaluación FAIR externa | F-UJI sobre DOI Zenodo | PENDIENTE_DE_EJECUCION |
| R | Preservación del software | Software Heritage SWHID del estado final | PENDIENTE_FASE6 |

## Relación entre Zenodo y el repositorio

El depósito Zenodo **ya está publicado** como versión 2.0.0 con DOI específico:

`10.5281/zenodo.22237884`

La carpeta `07_Publicacion/dataset_zenodo/` se conserva como snapshot histórico del paquete publicado. Las correcciones posteriores del repositorio, incluida la normalización terminal de identificadores, no se presentan como si fueran byte a byte idénticas a ese snapshot.

Si al cierre se publica una versión correctiva en Zenodo, se deberá registrar de forma explícita la nueva versión y su identificador correspondiente, sin sobrescribir la procedencia de la versión 2.0.0.

## Pasos FAIR todavía pendientes

1. Finalizar el estado de entrega del repositorio.
2. Archivar el estado final del software en Software Heritage y registrar el SWHID real.
3. Ejecutar F-UJI contra el DOI Zenodo que corresponda al paquete evaluado.
4. Guardar la evidencia exportada de F-UJI en el repositorio.
5. Registrar únicamente el puntaje realmente obtenido.
6. Si el resultado no alcanza el umbral académico exigido, corregir metadatos y repetir la evaluación.

Nunca se inventan DOI, SWHID ni puntajes FAIR.
