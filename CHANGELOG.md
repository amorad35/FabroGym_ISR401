# Changelog

Todos los cambios relevantes del proyecto FabroGym se documentan aquí siguiendo la estructura de Keep a Changelog.

## [2B-v2.0-cierre-fair-swh] - 2026-09-11

### Añadido
- Evaluación F-UJI real sobre el DOI Zenodo `10.5281/zenodo.22237884`.
- Evidencia `fair_assessment.pdf`.
- Snapshot verificable en Software Heritage: `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e`.
- Actualización de `README.md`, `FAIR_CHECKLIST.md` y `CITATION.cff` con identificadores y resultados reales.

### Verificado
- F-UJI 4.0.0 / métrica 0.8: **88 %**, FAIR **moderate**.
- Findable 7/7 (advanced), Accessible 6/7 (moderate), Interoperable 4/6 (moderate), Reusable 6/6 (moderate).
- Software Heritage muestra la revisión `swh:1:rev:56ae64739c8dfcb93de77b9085afaf74b029e5fd` y directory `swh:1:dir:864d5a537b9e2fa6931f7f2b3ad23a06275432fa`.

### Advertencia de preservación
- El `main` de GitHub ya contiene commits posteriores a la revisión archivada, incluido `d4e34c1cf763728a6938b0fc99f9f76f20a0f095`.
- El SWHID actual es válido como evidencia de archivado, pero se debe ejecutar **Save again** después del commit/tag final.

### Pendiente para congelamiento final
- Subir cualquier artefacto final aún pendiente (MVP responsive y/o video, si faltan).
- Ejecutar clon limpio y generar `10_Autoria/verificacion_previa.pdf`.
- Regenerar `checksums.sha256` después de todos los cambios.
- Hacer commit final y crear/push del tag anotado.
- Ejecutar Software Heritage → **Save again** y registrar el SWHID del estado final si cambia.

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
