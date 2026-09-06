# FabroGym — Ingeniería de Requerimientos (ISR-401)

Repositorio académico del proyecto **FabroGym**, desarrollado en la Universidad Técnica Estatal de Quevedo (UTEQ) para la Entrega 4 (2B / Defensa Final) de Ingeniería de Requerimientos.

## Estado 2B

FabroGym documenta la ingeniería de requisitos de un sistema de gestión de gimnasio local. El componente empírico usa el **Enfoque 3: explicabilidad como Requisito No Funcional (RNF)** para estudiar necesidades de explicación asociadas a un **componente de recomendación de rutinas propuesto**. El recomendador/IA **no se presenta como implementado** en el MVP.

| Componente | Estado de cierre |
|---|---|
| ERS/SRS | `01_ERS/ERS_SRS_2B_v2.0.pdf` y fuente LaTeX |
| Trazabilidad | catálogo normalizado (25 RF, 23 RNF y 4 RD) + 97 trazas históricas y 8 planes de verificación IA |
| MVP | cobertura histórica declarada como 16/19 RF Must; estado sujeto a verificación terminal C3 en `05_MVP/` |
| Análisis empírico | reproducible desde `06_Experimento/scripts_analisis/run_all.py` |
| Manuscrito | `07_Publicacion/manuscrito_fuente/manuscrito_final.pdf` + `.tex`, plantilla Springer Nature |
| Dataset Zenodo | **PUBLICADO**, versión 2.0.0; la copia local es el snapshot del depósito publicado |
| Registro OSF | publicado: https://osf.io/62ysc/ — DOI 10.17605/OSF.IO/62YSC |
| DOI Zenodo | [`10.5281/zenodo.22237884`](https://doi.org/10.5281/zenodo.22237884) — versión específica publicada |
| Software Heritage SWHID | `PENDIENTE_FASE6` — se incorporará solo cuando exista un SWHID real y verificable |
| F-UJI / FAIR | `PENDIENTE_DE_EJECUCION` — el DOI Zenodo ya existe; no se declara puntaje hasta ejecutar F-UJI |


## Equipo y ORCID

| Integrante | Rol principal | ORCID |
|---|---|---|
| Erick Adalberto Alvia Villegas | Analista líder / entrevistador | 0009-0001-3777-470X |
| Erick Jhair Mera Arias | Documentador / responsable de encuestas | 0009-0001-0068-1796 |
| Alex José Mora Duarte | Modelador / apoyo de análisis | 0009-0000-2494-2842 |
| Mery Helenmey Ponce Rivera | Verificador / calidad de requisitos | 0009-0006-6041-9198 |
| David Octavio Vaca Romero | Apoyo documental / evidencias | 0009-0000-4457-3095 |

**Cita del depósito publicado:** Equipo PFC FabroGym (2026), *FabroGym: explainability requirements and reproducible requirements-engineering artifacts*, versión 2.0, Universidad Técnica Estatal de Quevedo, GitHub. Depósito publicado: Zenodo 2.0.0, DOI 10.5281/zenodo.22237884.

## Identificadores empíricos congelados

- Entrevistas iniciales: `ENTR-01` … `ENTR-10`.
- Walkthroughs no técnicos: `WALK-NTEC-01` … `WALK-NTEC-03`.
- Walkthroughs técnicos: `WALK-TEC-01` … `WALK-TEC-03`.
- Member checking: `MC-P01`, `MC-P02`, `MC-P03`.

Los seis `WALK-*` conservan su técnica original. No se renombran como entrevistas aunque formen parte del acumulado de 16 sesiones aceptado para el cierre académico.

## Resultados reproducibles de referencia

La ejecución versionada del análisis trabaja con 16 sesiones audiovisuales, 70 respuestas del cuestionario, 76 fragmentos de walkthrough codificados, 37 códigos normalizados, 18 categorías temáticas, 9 fragmentos pertinentes para explicabilidad y cuatro RNF de explicabilidad terminales. La curva por códigos produce 6.306 % en las últimas tres sesiones, por lo que **no se declara saturación estricta ≤5 %**; la estabilización axial de 1.852 % se informa solo como evidencia complementaria.

## Reproducir el análisis

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r 06_Experimento/scripts_analisis/requirements.txt
python 06_Experimento/scripts_analisis/run_all.py
```

Las tablas y figuras del manuscrito deben provenir de esta ruta reproducible. No se admiten cifras manuales sin respaldo de script.

## Paquete de replicación FAIR

El depósito Zenodo ya fue publicado como versión 2.0.0: https://doi.org/10.5281/zenodo.22237884. La carpeta `07_Publicacion/dataset_zenodo/` se conserva en esta tarea como snapshot histórico del paquete publicado y no se modifica. La ERS académica vigente 2.0 y la normalización de identificadores son correcciones posteriores del repositorio; una eventual versión correctiva del depósito deberá evaluarse y publicarse de forma controlada en una fase posterior, sin afirmar identidad byte a byte con la versión 2.0.0.

## Privacidad y zonas [P]/[R]

Solo material anonimizado/seudonimizado debe permanecer en la zona pública. **No** se publican audios o videos identificables, consentimientos originales, cédulas, firmas, rostros, voces, correos, teléfonos, IP ni documentos originales identificables. El material restringido permanece fuera del paquete Zenodo y debe almacenarse cifrado conforme al protocolo.

El member checking sí ocurrió y tiene evidencia documental con `MC-P01..03`; **no existe grabación audiovisual de esa actividad** y no se fabrica una.

## Ética

La documentación ética debe residir finalmente en `08_Etica/`. A13 y la Adenda solo pueden figurar como firmados cuando las firmas reales existan. No se retrofecha documentación.

## Licencias

- Código del MVP y scripts: **MIT**.
- Documentación y dataset anonimizado: **CC BY 4.0**.
- `02_Evidencias/00_Restringido/`: **excluido de la licencia abierta** y del depósito Zenodo.

Consulte `LICENSE` y `CITATION.cff`.
