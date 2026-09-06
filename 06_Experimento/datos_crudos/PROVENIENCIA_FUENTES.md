# Proveniencia de la capa de entrada

## Regla de separación

`datos_crudos/` funciona como la **capa de entrada inmutable** del pipeline: los scripts leen desde aquí y no escriben en esta carpeta.

No todos los archivos de esta capa proceden directamente de un instrumento aplicado a participantes. La carpeta también contiene matrices analíticas humanas ya congeladas (por ejemplo, codificación temática y member checking) que actúan como insumos fuente del análisis reproducible. Esta distinción se documenta para no presentar como “dato crudo de instrumento” lo que en realidad es una matriz fuente producida por el equipo.

Los resultados creados por código se escriben únicamente en `datos_procesados/` y `resultados/`.

## Fuentes de recolección y evidencia primaria

- `encuesta_clientes_anonimizada.csv`: conjunto analítico público anonimizado del cuestionario, con **70 respuestas** y corte congelado hasta **31/08/2026 23:58:25**. Las respuestas posteriores al corte no forman parte del conjunto analítico versionado.
- `sesiones_multimedia_desde_ficha_v3_1.csv`: extracto de la ficha técnica de evidencia multimedia. Conserva los 16 códigos de sesión y los nombres, duraciones y SHA-256 utilizados por el pipeline. La ficha técnica completa se conserva en `02_Evidencias/fichas_tecnicas.csv`.

## Matrices fuente congeladas para análisis

Los siguientes archivos son insumos analíticos producidos o consolidados antes de ejecutar `run_all.py`; el pipeline los consume como fuente y no los reescribe dentro de `datos_crudos/`:

- `codificacion_walkthroughs.csv`: matriz de codificación humana del corpus WALK.
- `diccionario_codigos_walkthroughs.csv`: libro de códigos utilizado para interpretar la codificación.
- `comparacion_perfiles_walkthroughs_fuente.csv`: matriz fuente de presencia/conteo por categoría para perfiles técnico y no técnico.
- `curva_codigos_nuevos_walkthroughs_fuente.csv`: fuente de códigos nuevos por sesión para la curva de saturación.
- `estabilizacion_categorias_axiales_fuente.csv`: fuente de categorías axiales nuevas por sesión.
- `fragmentos_pertinentes_explicabilidad.csv`: subconjunto fuente de fragmentos pertinentes para explicabilidad.
- `candidatos_RNF_explicabilidad_member_checked.csv`: candidatos RNF consolidados después del member checking.
- `member_checking_estructurado.csv`: decisiones estructuradas documentadas del member checking.

## Evidencia sensible y zona pública

Los archivos de esta capa no sustituyen la evidencia restringida. Audios, videos, consentimientos íntegros, firmas y otros datos identificables permanecen en la zona restringida correspondiente. La capa pública conserva únicamente datos anonimizados, seudonimizados o matrices derivadas sin identificadores directos.

No se generan entrevistas, respuestas, hashes, grabaciones ni decisiones nuevas dentro de esta carpeta.
