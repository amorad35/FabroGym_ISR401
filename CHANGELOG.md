# Changelog

Todos los cambios relevantes del proyecto FabroGym se documentan aquí siguiendo la estructura de Keep a Changelog.

## [2B-v2.0-cierre-canonico] - 2026-09-12

### Corregido — A5
- Se eliminaron del paquete local las copias divergentes `ERS_SRS_2B_v2.2.pdf` y `ERS_SRS_2B_v2.2.tex`.
- La única ERS/SRS académica vigente queda en `01_ERS/ERS_SRS_2B_v2.0.*`.
- `07_Publicacion/dataset_zenodo/srs/README.md` funciona únicamente como referencia documental hacia la ERS/SRS canónica.

### Consolidado — B1
- Se declara `07_Datos/` como **único paquete canónico, ejecutable y evaluable** de datos y análisis para la Entrega 4 (2B).
- El orquestador oficial es `07_Datos/scripts/run_all.py`.
- Las dependencias oficiales están en `07_Datos/scripts/requirements.txt`.
- Se actualiza `README.md` para eliminar la referencia de ejecución oficial a `06_Experimento/scripts_analisis/run_all.py`.
- `06_Experimento/` y `06_Experimento/scripts_analisis/` se conservan exclusivamente como procedencia/historial metodológico y no como segunda cadena canónica.
- `07_Publicacion/` queda identificado como paquete de publicación/replicación histórica y no sustituye a `07_Datos/`.

### Integridad
- No se modifican los datos crudos, CSV analíticos, tablas, figuras ni valores de resultados para esta normalización documental.
- No se elimina la evidencia histórica necesaria para trazabilidad.

## [2B-v2.0-cierre-fair-swh] - 2026-09-11

### Añadido
- Evaluación F-UJI real sobre el DOI Zenodo `10.5281/zenodo.22237884`.
- Evidencia `fair_assessment.pdf`.
- Snapshot verificable en Software Heritage: `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e`.
- Actualización de `README.md`, `FAIR_CHECKLIST.md` y `CITATION.cff` con identificadores y resultados reales.

### Verificado
- F-UJI 4.0.0 / métrica 0.8: **88 %**, FAIR **moderate**.
- Findable 7/7 (advanced), Accessible 6/7 (moderate), Interoperable 4/6 (moderate), Reusable 6/6 (moderate).

### Advertencia de preservación
- El SWHID existente conserva un estado anterior del repositorio.
- Se debe ejecutar **Save again** después del commit/tag final.

## [2B-v2.0-uml-secuencia-saneado] - 2026-09-05

### Cambiado
- Se sustituyeron los 19 diagramas de secuencia por exportaciones saneadas desde Visual Paradigm y se sincronizó la ERS/SRS v2.0.

## [2B-v2.0-normalizacion-ids] - 2026-09-04

### Cambiado
- Se consolidó `01_ERS/ERS_SRS_2B_v2.0.*` como única ERS/SRS vigente.
- Se normalizaron 25 RF, 23 RNF y 4 RD; se sincronizaron catálogo, matriz y modelado.
- Zenodo quedó publicado como versión 2.0.0 con DOI `10.5281/zenodo.22237884`.

## [2B-v2.0-predeposit] - 2026-09-01

### Añadido
- ERS/SRS 2B v2.0, análisis reproducible, resultados finales, RNF de explicabilidad, manuscrito y paquete de datos.

## [2B-preOSF-v1.4] - 2026-08-28

### Cambiado
- Prerregistro OSF v1.4 y aclaración de la cronología de walkthroughs.

## [2B-preOSF-v1.3] - 2026-08-28

### Añadido
- Instrumentos de explicabilidad y scripts reproducibles iniciales.

## [2A-v1.0] - 2026-07-29

### Añadido
- Estructura pública de ERS, evidencias, modelado, trazabilidad, MVP, experimento y publicación.

## [1B-v2.0] - 2026-06-27

### Añadido
- RF/RNF formalizados, mockups, UML, MoSCoW y trazabilidad parcial.

## [1A-v1.0] - 2026-05-31

### Añadido
- Planificación, stakeholders, elicitación inicial y primeras evidencias de campo.
