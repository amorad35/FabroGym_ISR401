# FabroGym — Ingeniería de Requerimientos (ISR-401)

Repositorio académico del proyecto **FabroGym**, desarrollado en la Universidad Técnica Estatal de Quevedo (UTEQ) para la Entrega 4 (2B / Defensa Final) de Ingeniería de Requerimientos.

## Estado 2B

FabroGym documenta la ingeniería de requisitos de un sistema de gestión de gimnasio local. El componente empírico usa el **Enfoque 3: explicabilidad como Requisito No Funcional (RNF)** para estudiar necesidades de explicación asociadas a un **componente de recomendación de rutinas propuesto**. El recomendador/IA **no se presenta como implementado** en el MVP.

| Componente | Estado de cierre |
|---|---|
| ERS/SRS | `01_ERS/ERS_SRS_2B_v2.0.pdf` y fuente LaTeX |
| Trazabilidad | 25 RF, 23 RNF y 4 RD + 97 trazas históricas + 8 planes de verificación IA |
| MVP | cobertura C3 verificada: **16/19 RF Must (84,21 %)** |
| **Paquete de datos y análisis canónico** | **`07_Datos/` — ejecución oficial con `python scripts/run_all.py`** |
| Manuscrito | `07_Publicacion/manuscrito_final.pdf` + `.tex` |
| Zenodo | **PUBLICADO**, versión 2.0.0 — DOI `10.5281/zenodo.22237884` |
| OSF | **PUBLICADO** — DOI `10.17605/OSF.IO/62YSC` |
| Software Heritage | **SNAPSHOT ARCHIVADO** — `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e` |
| F-UJI / FAIR | **EJECUTADO** — **88 %**, FAIR **moderate**, F-UJI 4.0.0 / métrica 0.8 |

> **Regla de unicidad B1:** para la Entrega Final 2B existe un único paquete canónico ejecutable de datos y análisis: `07_Datos/`. Los archivos conservados en `06_Experimento/` documentan el protocolo, la procedencia y el desarrollo histórico del estudio; **no constituyen una segunda cadena canónica de ejecución**. Los artefactos de `07_Publicacion/` documentan la publicación/replicación histórica y tampoco sustituyen a `07_Datos/` para B1.

> **Nota de preservación:** Software Heritage muestra actualmente una revisión anterior del repositorio. Después del commit/tag final se debe ejecutar **Save again**.

## Evidencia FAIR y preservación

### F-UJI

El DOI `10.5281/zenodo.22237884` fue evaluado el 11 de septiembre de 2026:

- Resultado global: **88 %**
- FAIR level: **moderate**
- Findable: **7/7 — advanced**
- Accessible: **6/7 — moderate**
- Interoperable: **4/6 — moderate**
- Reusable: **6/6 — moderate**
- Evidencia: `fair_assessment.pdf`

### Software Heritage

- Snapshot SWHID: `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e`
- Revision archivada: `swh:1:rev:56ae64739c8dfcb93de77b9085afaf74b029e5fd`
- Directory SWHID: `swh:1:dir:864d5a537b9e2fa6931f7f2b3ad23a06275432fa`

## Equipo

### Equipo actual de cierre

| Integrante | Usuario Git |
|---|---|
| Erick Jhair Mera Arias | `Emeraxs` |
| Alex José Mora Duarte | `amorad35` |
| Mery Helenmey Ponce Rivera | `Mery-003` |

### Participación histórica preservada

Las contribuciones históricas de Erick Adalberto Alvia Villegas y David Octavio Vaca Romero permanecen en el historial Git y en los artefactos donde corresponden. No se eliminan ni se reasignan.

## Compilar el ERS/SRS

### Compilador

- `pdflatex` (distribución TeX Live o MiKTeX compatible con los paquetes utilizados por el documento).

### Archivo principal

- `01_ERS/ERS_SRS_2B_v2.0.tex`

### Dependencias versionadas

- `01_ERS/referencias.bib`
- `01_ERS/figuras_2B/`
- `01_ERS/modelado_final/`
- `03_Modelado/Diagramas_UML/` como ubicación canónica del modelado UML

### Directorio de ejecución

Desde la raíz del repositorio:

```bash
cd 01_ERS
```

### Orden exacta de compilación

Ejecutar tres veces:

```bash
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
```

### PDF esperado

- `01_ERS/ERS_SRS_2B_v2.0.pdf`

## Reproducir el análisis — cadena oficial B1

Desde la raíz del repositorio:

```bash
cd 07_Datos
python -m pip install -r scripts/requirements.txt
python scripts/run_all.py
```

Esta es la **única cadena canónica de reproducción para la Entrega 4 (2B)**. No se debe ejecutar `06_Experimento/scripts_analisis/run_all.py` como cadena oficial de B1.

## Relación con `06_Experimento/`

`06_Experimento/` conserva el protocolo, el prerregistro OSF, instrumentos, matrices y scripts históricos que documentan la procedencia del estudio. Se mantienen por trazabilidad y no-retroceso, pero la cadena consolidada y evaluable se encuentra únicamente en `07_Datos/`.

## Paquete FAIR

Zenodo 2.0.0: https://doi.org/10.5281/zenodo.22237884. La evaluación F-UJI real se conserva como `fair_assessment.pdf`. Consulte también `FAIR_CHECKLIST.md` y `CITATION.cff`.

## Licencias

- Código del MVP y scripts: **MIT**.
- Documentación y dataset anonimizado: **CC BY 4.0**.
- Evidencia identificable: sujeta a las reglas de la capa restringida/cifrada definidas en `08_Etica/`.
