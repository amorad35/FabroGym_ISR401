# FAIR_CHECKLIST — FabroGym 2B

**Proyecto:** FabroGym — ISR-401  
**Estado documental:** cierre final 2B — verificaciones pre-tag cerradas  
**Repositorio:** `https://github.com/amorad35/FabroGym_ISR401`

Este archivo documenta el estado FAIR y de preservación verificable del proyecto antes del congelamiento mediante tag.

## Estado actual

| Área | Comprobación | Evidencia | Estado |
|---|---|---|---|
| Findable | Identificador persistente del paquete | Zenodo v2.0.0 — DOI `10.5281/zenodo.22237884` | **VERIFICADO** |
| Findable | Registro del protocolo | OSF — DOI `10.17605/OSF.IO/62YSC` | **VERIFICADO** |
| Findable | Título, descripción, autores y palabras clave | Zenodo + `CITATION.cff` | **VERIFICADO** |
| Findable | Citación legible por máquina | `CITATION.cff` | **DISPONIBLE** |
| Accessible | Paquete público | Zenodo / GitHub | **DISPONIBLE** |
| Accessible | Separación público/restringido | `08_Etica/` + auditor de privacidad | **VERIFICADA** |
| Accessible | Auditoría de privacidad | `07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md` | **0 BLOQUEOS / B6 MANUAL CERRADO** |
| Interoperable | Formatos abiertos/estructurados | CSV, JSON, TXT, MD, SVG | **DISPONIBLE** |
| Interoperable | Identificadores estables | ENTR, WALK, MC, RF, RNF y RD | **DISPONIBLE** |
| Interoperable | Diccionario de datos | `07_Datos/diccionario_datos.csv` | **DISPONIBLE** |
| Reusable | Licencias | CC BY 4.0 datos/documentación; MIT código | **DISPONIBLE** |
| Reusable | Proveniencia | `07_Datos/datos_crudos/PROVENIENCIA_FUENTES.md` + OSF | **DISPONIBLE** |
| Reusable | Reproducibilidad | `07_Datos/scripts/run_all.py` + `requirements.txt` | **VERIFICADA** |
| Reusable | Versionado | Git + `CHANGELOG.md` + Zenodo 2.0.0 | **DISPONIBLE** |
| Reusable | Evaluación FAIR externa | `fair_assessment.pdf` | **88 % — FAIR moderate** |
| Preservación | Software Heritage | Snapshot real previo al tag final | **VERIFICADO; ACTUALIZACIÓN POST-TAG PENDIENTE** |

## F-UJI

**Recurso evaluado:** *Replication package for Explainability Requirements for Fitness Routine Recommendations: A Field Case Study in Ecuador*  
**PID:** `10.5281/zenodo.22237884`  
**Fecha de evaluación:** 2026-09-11  
**F-UJI:** 4.0.0  
**Versión de métrica:** 0.8  
**Resultado global:** **88 % — FAIR level: moderate**

| Dimensión | Puntaje | Nivel |
|---|---:|---|
| Findable | 7/7 | advanced |
| Accessible | 6/7 | moderate |
| Interoperable | 4/6 | moderate |
| Reusable | 6/6 | moderate |

La evidencia se conserva como `fair_assessment.pdf`.

## Software Heritage

Snapshot archivado actualmente:

```text
swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e
```

Revision archivada:

```text
swh:1:rev:56ae64739c8dfcb93de77b9085afaf74b029e5fd
```

Directory SWHID:

```text
swh:1:dir:864d5a537b9e2fa6931f7f2b3ad23a06275432fa
```

Este snapshot es real y verificable. Corresponde al estado anterior al tag final; después de publicar el tag de entrega se ejecutará **Software Heritage → Save again** para preservar el estado congelado. Esta operación es deliberadamente posterior al tag y no constituye un pendiente de contenido del proyecto.

## Reproducibilidad canónica B1

La cadena canónica del cierre es:

```bash
cd 07_Datos
python -m pip install -r scripts/requirements.txt
python scripts/run_all.py
```

`06_Experimento/` se conserva como procedencia/historial metodológico y no sustituye a `07_Datos/`.

## Privacidad

El reporte `07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md` documenta:

- **0 hallazgos automáticos bloqueantes**;
- capa restringida documentada;
- 5 fotografías A6 con EXIF técnicamente válido;
- confirmaciones humanas de cifrado, ausencia de claves y revisión visual **cerradas**;
- **0 confirmaciones humanas pendientes**.

## Estado de cierre FAIR

Cerrado antes del tag:

- [x] Zenodo v2.0.0 con DOI real.
- [x] OSF con DOI real.
- [x] `fair_assessment.pdf`.
- [x] F-UJI ejecutado: 88 %.
- [x] SWHID real archivado.
- [x] `07_Datos/` declarado como paquete canónico.
- [x] Auditoría automática de privacidad con 0 bloqueos.
- [x] Confirmaciones humanas B6 cerradas.
- [x] Verificación final desde clon limpio ejecutada.
- [x] Checksums definitivos regenerados/verificados.
- [x] README raíz y `CHANGELOG.md` normalizados para A5/B1.

Operaciones de congelamiento/post-tag:

- [ ] Crear y publicar el tag anotado de la versión entregada.
- [ ] Verificar en GitHub que el tag remoto existe.
- [ ] Ejecutar Software Heritage → **Save again** sobre el estado congelado.

> No se debe realizar un nuevo commit únicamente para perseguir un SWHID posterior: primero se congela con el tag y luego se solicita la nueva preservación.
