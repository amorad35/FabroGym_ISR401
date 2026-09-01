# FabroGym — Ingeniería de Requerimientos (ISR-401)

Repositorio académico del proyecto **FabroGym**, desarrollado en la Universidad Técnica Estatal de Quevedo (UTEQ) para la Entrega 4 (2B / Defensa Final) de Ingeniería de Requerimientos.

## Estado 2B

FabroGym documenta la ingeniería de requisitos de un sistema de gestión de gimnasio local. El componente empírico usa el **Enfoque 3: explicabilidad como Requisito No Funcional (RNF)** para estudiar necesidades de explicación asociadas a un **componente de recomendación de rutinas propuesto**. El recomendador/IA **no se presenta como implementado** en el MVP.

| Componente | Estado de cierre |
|---|---|
| ERS/SRS | `01_ERS/ERS_SRS_2B_v2.0.pdf` y fuente LaTeX |
| Trazabilidad | catálogo terminal + matriz 2B con 97 vínculos cerrados |
| MVP | parche validado con objetivo 16/19 RF Must; verificar sustitución final en `05_MVP/` |
| Análisis empírico | reproducible desde `06_Experimento/scripts_analisis/run_all.py` |
| Manuscrito | `07_Publicacion/manuscrito_final.pdf` + `.tex`, plantilla Springer Nature |
| Dataset Zenodo | **PREPARADO PARA DEPÓSITO DESPUÉS DE FASE 6** en `07_Publicacion/dataset_zenodo/` |
| Registro OSF | publicado: https://osf.io/62ysc/ — DOI 10.17605/OSF.IO/62YSC |
| DOI Zenodo | `PENDIENTE_POST_FASE6` — no inventado |
| Software Heritage SWHID | `PENDIENTE_POST_FASE6` — no inventado |
| F-UJI / FAIR | `PENDIENTE_POST_ZENODO` — no se declara puntaje sin ejecutar la herramienta |


## Equipo y ORCID

| Integrante | Rol principal | ORCID |
|---|---|---|
| Erick Adalberto Alvia Villegas | Analista líder / entrevistador | 0009-0001-3777-470X |
| Erick Jhair Mera Arias | Documentador / responsable de encuestas | 0009-0001-0068-1796 |
| Alex José Mora Duarte | Modelador / apoyo de análisis | 0009-0000-2494-2842 |
| Mery Helenmey Ponce Rivera | Verificador / calidad de requisitos | 0009-0006-6041-9198 |
| David Octavio Vaca Romero | Apoyo documental / evidencias | 0009-0000-4457-3095 |

**Cita recomendada antes del depósito:** Equipo PFC FabroGym (2026), *FabroGym: explainability requirements and reproducible requirements-engineering artifacts*, versión 2.0, Universidad Técnica Estatal de Quevedo, GitHub. Después del depósito final, sustituir esta cita por la emitida con el DOI Zenodo real y `CITATION.cff` actualizado.

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

La carpeta `07_Publicacion/dataset_zenodo/` está preparada como **predepósito**. Como el equipo decidió obtener el DOI solo al terminar todas las fases, el procedimiento correcto es:

1. finalizar Fase 6 y el estado definitivo del repositorio;
2. ejecutar `python scripts_release/build_zenodo_package.py` desde la raíz del repositorio;
3. ejecutar `python scripts_release/validate_public_release.py 07_Publicacion/dataset_zenodo`;
4. revisar manualmente privacidad y el manifiesto;
5. crear/publicar el depósito Zenodo y obtener el DOI real;
6. actualizar DOI, SWHID y F-UJI con `POST_FASE6_ZENODO_SWH_FUJI.md`.

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
