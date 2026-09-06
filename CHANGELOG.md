# Changelog

Todos los cambios relevantes del proyecto FabroGym se documentan aquí siguiendo la estructura de Keep a Changelog.

## [2B-v2.0-uml-secuencia-saneado] - 2026-09-05

### Cambiado
- Se sustituyeron en la fuente UML canónica y en el mirror de compilación los 19 diagramas de secuencia por las exportaciones saneadas desde Visual Paradigm, con nombres y rótulos internos RF normalizados.
- Se actualizó `FabroGym_Diagramas_UML.vpp` con la fuente editable saneada y se eliminaron del árbol activo los 19 nombres históricos de secuencia.
- Se actualizaron las rutas y leyendas del anexo UML de la ERS/SRS v2.0 y se retiró el bloqueo temporal de identificadores internos.

## [2B-v2.0-normalizacion-ids] - 2026-09-04

### Cambiado
- Se consolidó `01_ERS/ERS_SRS_2B_v2.0.*` como única ERS/SRS académica vigente y se subordinó 2.1/2.2 al historial interno no vigente.
- Se normalizaron 25 RF, 19 RNF preexistentes y 4 RD a numeración continua; se añadieron cuatro RNF propuestos exigidos para recomendación, equidad, monitoreo y riesgo.
- Se sincronizaron catálogo, matriz, priorización y consumidores directos sin modificar el método analítico ni los datos crudos.
- Se verificaron 54 PNG UML byte a byte y se incorporaron sus tres fuentes editables originales; los 19 raster de secuencia conservan IDs visuales históricos documentados mediante el mapa de migración.
- Se sincronizó `01_ERS/modelado_final/` como mirror byte a byte de los 54 PNG canónicos de `03_Modelado/Diagramas_UML/`, se corrigió la ruta de la matriz y se documentaron sus 105 filas (97 trazas migradas y 8 planes de verificación).
- Se corrigió el estado del depósito Zenodo: versión 2.0.0 publicada, DOI 10.5281/zenodo.22237884.

## [2B-v2.0-predeposit] - 2026-09-01

### Añadido
- ERS/SRS 2B v2.0 consolidada.
- Catálogo terminal de requisitos y matriz de trazabilidad 2B normalizada.
- Análisis empírico reproducible con entrada única `run_all.py`.
- Resultados finales descriptivos para encuesta, walkthroughs, saturación, explicabilidad y member checking.
- Cuatro RNF de explicabilidad terminales derivados de evidencia y member checking.
- Manuscrito final para Requirements Engineering usando plantilla Springer Nature.
- Paquete `07_Publicacion/dataset_zenodo/` preparado para depósito posterior a Fase 6.
- Documentación FAIR, anonimización, ética y scripts de cierre/release.

### Cambiado
- El estado del repositorio deja de describirse como pre-OSF: el registro OSF v1.4 fue publicado el 29-08-2026 (10.17605/OSF.IO/62YSC).
- Se conserva la cronología real: los seis WALK son previos al registro y se tratan como evidencia formativa/pre-registro.
- La IA/recomendador permanece como componente propuesto, no implementado en el MVP.
- El cuestionario n=70 se usa descriptivamente y no se convierte en una escala de explicabilidad.

### Corregido
- IDs duplicados de requisitos y discrepancias de trazabilidad.
- Referencias obsoletas a análisis inferenciales no soportados por los instrumentos reales.
- Estado de member checking: actividad documentada con MC-P01..03, sin inventar una grabación inexistente.

### Pendiente externo para el cierre definitivo
- Firmas reales que correspondan en A13/Adenda; no retrofechar.
- DOI Zenodo después de Fase 6.
- SWHID de Software Heritage después del commit final.
- Reporte F-UJI con DOI Zenodo; no se declara puntaje antes de ejecutarlo.
- Regeneración final de `checksums.sha256` contra multimedia real y paquete Zenodo definitivo.

## [2B-preOSF-v1.4] - 2026-08-28
### Cambiado
- Protocolo de prerregistro OSF v1.4 y aclaración de la secuencia temporal real de los walkthroughs.
- Walkthroughs descritos como validaciones generales y evidencia previa/formativa.
- Análisis de explicabilidad limitado a fragmentos con relación verificable y trazable.

## [2B-preOSF-v1.3] - 2026-08-28
### Añadido
- Instrumentos de sistematización de explicabilidad y scripts reproducibles iniciales.
### Corregido
- Eliminación de rondas artificiales, Likert inexistente y análisis inferenciales no sustentados.

## [2A-v1.0] - 2026-07-29
### Añadido
- Estructura pública de ERS, evidencias, modelado, trazabilidad, MVP, experimento y publicación.

## [1B-v2.0] - 2026-06-27
### Añadido
- RF/RNF formalizados, mockups, UML, MoSCoW y trazabilidad parcial.

## [1A-v1.0] - 2026-05-31
### Añadido
- Planificación, stakeholders, elicitación inicial y primeras evidencias de campo.
