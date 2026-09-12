# Paquete canónico de datos de FabroGym

`07_Datos/` es el **único paquete canónico, ejecutable y evaluable de datos y análisis para la Entrega 4 (2B)**.

Reúne los insumos públicos anonimizados, la cadena consolidada de análisis y sus productos reproducibles. La existencia de datos o scripts históricos en `06_Experimento/` documenta procedencia y evolución metodológica, pero **no constituye una segunda cadena canónica**.

## Regla de unicidad B1

Para la evaluación final:

```text
Paquete canónico:        07_Datos/
Orquestador oficial:     07_Datos/scripts/run_all.py
Dependencias oficiales:  07_Datos/scripts/requirements.txt
Datos crudos oficiales:  07_Datos/datos_crudos/
Salidas oficiales:       07_Datos/datos_procesados/ y 07_Datos/resultados/
```

`06_Experimento/` se conserva como fuente metodológica/histórica. `07_Publicacion/` conserva artefactos de publicación y depósitos históricos. Ninguna de esas carpetas sustituye a `07_Datos/` para B1.

## Estructura

```text
07_Datos/
├── datos_crudos/
├── datos_procesados/
├── scripts/
├── resultados/
├── diccionario_datos.csv
├── README_datos.md
├── LICENSE-DATA.txt
├── checksums_datos.sha256
├── desviaciones.md
└── registro_deposito.md
```

## Procedencia

Los insumos de `datos_crudos/` proceden de evidencia y matrices previamente versionadas, incluida la documentación metodológica de `06_Experimento/`. Los scripts consolidados derivan de la cadena desarrollada durante el proyecto.

`datos_crudos/PROVENIENCIA_FUENTES.md` documenta la fuente inmediata de cada familia de insumos.

Esta procedencia **no convierte `06_Experimento/` en un segundo paquete activo**.

## Corte analítico del cuestionario

La muestra analítica oficial del cuestionario está formada por **70 respuestas**. El archivo canónico es:

```text
datos_crudos/encuesta_clientes_anonimizada.csv
```

El corte utilizado por el proyecto quedó congelado hasta **31/08/2026 23:58:25**. Las respuestas posteriores no se incorporan retroactivamente.

## Separación entre entrada y productos

- `datos_crudos/`: insumos fuente congelados;
- `datos_procesados/`: salidas generadas por `scripts/run_all.py`;
- `resultados/`: tablas, figuras y resúmenes reproducibles.

## Requisitos

Se requiere Python 3. La reproducción fue verificada con Python 3.12.13 y las dependencias declaradas en:

```text
scripts/requirements.txt
```

Instalación:

```bash
python -m pip install -r scripts/requirements.txt
```

## Ejecución reproducible — única orden oficial

Desde la raíz de `07_Datos/`:

```bash
python scripts/run_all.py
```

No se requieren pasos manuales intermedios.

El pipeline regenera:

- `datos_procesados/`;
- tablas de resultados;
- figuras;
- resúmenes analíticos;
- artefactos de desviaciones definidos por la cadena.

## Privacidad

Este paquete incluye únicamente datos públicos anonimizados o seudonimizados aptos para el análisis reproducible. La evidencia identificable/restringida se gobierna mediante la política de `08_Etica/` y no forma parte de los datos crudos públicos de B1.

## Relación con Zenodo

El depósito Zenodo 2.0.0 (DOI `10.5281/zenodo.22237884`) es un registro histórico publicado. `07_Datos/` es el paquete canónico de la **entrega académica vigente** y no se afirma que sea idéntico byte a byte a ese depósito histórico.

## Limitaciones

- El cuestionario no contiene perfil técnico/no técnico ni una escala Likert de explicabilidad.
- La saturación estricta de códigos no alcanza el umbral del 5 %.
- Los SHA-256 de multimedia restringida documentan evidencia que no forma parte de la capa pública de datos.
- El member checking dispone de evidencia documental pública, pero no de grabación audiovisual.

## Estado B1

**CANÓNICO / EJECUTABLE / EVALUABLE: `07_Datos/`**

No existe otra carpeta que deba utilizarse como cadena oficial para reproducir los resultados de la Entrega Final.
