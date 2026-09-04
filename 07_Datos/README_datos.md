# Paquete canónico de datos de FabroGym

`07_Datos/` reúne los insumos públicos anonimizados, la cadena de análisis y sus productos reproducibles para la Entrega 4 (2B). No contiene audios, videos, consentimientos, firmas ni otros materiales restringidos.

## Estructura

```text
07_Datos/
├── datos_crudos/          # Insumos públicos copiados sin alterar
├── datos_procesados/      # CSV generados por el pipeline
├── scripts/               # Cadena de análisis y dependencias
├── resultados/            # Tablas, figuras y resúmenes generados
├── diccionario_datos.csv  # Diccionario de columnas reales
├── README_datos.md
├── LICENSE-DATA.txt
├── checksums_datos.sha256
├── desviaciones.md
└── registro_deposito.md
```

## Procedencia

Los insumos de `datos_crudos/` proceden de `06_Experimento/datos_crudos/` y se copiaron sin cambiar nombres, codificación ni valores. Los scripts proceden de `06_Experimento/scripts_analisis/`. El archivo `datos_crudos/PROVENIENCIA_FUENTES.md` documenta las fuentes inmediatas.

## Requisitos y preparación

Se requiere Python 3. La reproducción fue verificada específicamente con Python 3.12.13 y las versiones aceptadas por `scripts/requirements.txt`; para repetir exactamente esta prueba, use esa versión de Python.

Desde la raíz de `07_Datos/`, instale las dependencias:

```bash
python -m pip install -r scripts/requirements.txt
```

## Ejecución reproducible

Desde la raíz de `07_Datos/`, la cadena completa se ejecuta con una sola orden:

```bash
python scripts/run_all.py
```

No se requieren pasos manuales intermedios. El proceso valida los insumos y vuelve a generar:

- `datos_procesados/`: diez CSV derivados;
- `resultados/tablas/`: tablas CSV del análisis;
- `resultados/figuras/`: figuras equivalentes en PNG y SVG;
- `resultados/resumen_resultados.json` y `resultados/RESUMEN_FASE2.md`.

El pipeline también produce copias auxiliares de las desviaciones (`osf_deviations.md` y `osf_deviations.pdf`) en su raíz de ejecución. Para el paquete canónico se conserva la versión exigida con el nombre `desviaciones.md`.

## Privacidad y redistribución

Este paquete incluye únicamente matrices, respuestas y transcripciones WALK públicas anonimizadas o seudonimizadas. Los códigos `ENTR-*`, `WALK-*` y `MC-P*` no deben sustituirse por identidades reales. El material identificable o restringido no se redistribuye. Consulte `LICENSE-DATA.txt`.

## Relación con Zenodo

El depósito de datos actualmente publicado es FabroGym versión 2.0.0, DOI específico [10.5281/zenodo.22237884](https://doi.org/10.5281/zenodo.22237884), publicado el 1 de septiembre de 2026. `07_Datos/` reorganiza y reutiliza artefactos versionados del repositorio; no se afirma que sea idéntico byte a byte al depósito 2.0.0. Una eventual versión correctiva de Zenodo se evaluará posteriormente en la Fase 6; este procedimiento no crea ni modifica depósitos remotos.

## Limitaciones

- El cuestionario no contiene perfil técnico/no técnico ni una escala Likert de explicabilidad; sus resultados son descriptivos y no se reinterpretan como medición de explicabilidad.
- La saturación estricta de códigos no alcanza el umbral del 5 %; la estabilización axial se informa como evidencia complementaria.
- Los SHA-256 declarados para multimedia identifican archivos restringidos ausentes de este paquete; no se vuelve a validar aquí su correspondencia física.
- El member checking dispone de evidencia documental pública, pero no de grabación audiovisual.
