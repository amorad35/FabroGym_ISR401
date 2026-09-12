# FabroGym — Ingeniería de Requerimientos (ISR-401)

Repositorio académico del proyecto **FabroGym**, desarrollado en la Universidad Técnica Estatal de Quevedo (UTEQ) para la Entrega 4 (2B / Defensa Final) de Ingeniería de Requerimientos.

## Estado 2B

FabroGym documenta la ingeniería de requisitos de un sistema de gestión de gimnasio local. El componente empírico usa el **Enfoque 3: explicabilidad como Requisito No Funcional (RNF)** para estudiar necesidades de explicación asociadas a un **componente de recomendación de rutinas propuesto**. El recomendador/IA **no se presenta como implementado** en el MVP.

| Componente | Estado de cierre |
|---|---|
| ERS/SRS | `01_ERS/ERS_SRS_2B_v2.0.pdf` y fuente LaTeX |
| Trazabilidad | 25 RF, 23 RNF y 4 RD + 97 trazas históricas + 8 planes de verificación IA |
| MVP | cobertura C3 verificada: **16/19 RF Must (84,21 %)** |
| Análisis empírico | reproducible desde `06_Experimento/scripts_analisis/run_all.py` |
| Manuscrito | `07_Publicacion/manuscrito_final.pdf` + `.tex` |
| Zenodo | **PUBLICADO**, versión 2.0.0 — DOI `10.5281/zenodo.22237884` |
| OSF | **PUBLICADO** — DOI `10.17605/OSF.IO/62YSC` |
| Software Heritage | **SNAPSHOT ARCHIVADO** — `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e` |
| F-UJI / FAIR | **EJECUTADO** — **88 %**, FAIR **moderate**, F-UJI 4.0.0 / métrica 0.8 |

> **Nota de preservación:** Software Heritage muestra actualmente la revisión `swh:1:rev:56ae64739c8dfcb93de77b9085afaf74b029e5fd`. El `main` de GitHub contiene commits posteriores, por lo que se debe ejecutar **Save again** después del commit/tag final.

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
- Permalink: https://archive.softwareheritage.org/swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e;origin=https://github.com/amorad35/FabroGym_ISR401

## Equipo y ORCID

| Integrante | Rol principal | ORCID |
|---|---|---|
| Erick Adalberto Alvia Villegas | Analista líder / entrevistador | 0009-0001-3777-470X |
| Erick Jhair Mera Arias | Documentador / responsable de encuestas | 0009-0001-0068-1796 |
| Alex José Mora Duarte | Modelador / apoyo de análisis | 0009-0000-2494-2842 |
| Mery Helenmey Ponce Rivera | Verificador / calidad de requisitos | 0009-0006-6041-9198 |
| David Octavio Vaca Romero | Apoyo documental / evidencias | 0009-0000-4457-3095 |

## Compilar el ERS/SRS

Desde `01_ERS/`, ejecutar tres veces:

```bash
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
```

## Reproducir el análisis

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r 06_Experimento/scripts_analisis/requirements.txt
python 06_Experimento/scripts_analisis/run_all.py
```

## Paquete FAIR

Zenodo 2.0.0: https://doi.org/10.5281/zenodo.22237884. La evaluación F-UJI real se conserva como `fair_assessment.pdf`. Consulte también `FAIR_CHECKLIST.md` y `CITATION.cff`.

## Licencias

- Código del MVP y scripts: **MIT**.
- Documentación y dataset anonimizado: **CC BY 4.0**.
- Evidencia restringida: excluida del paquete público.
