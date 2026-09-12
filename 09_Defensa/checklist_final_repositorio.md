# Checklist final del repositorio — FabroGym 2B

**Repositorio:** `https://github.com/amorad35/FabroGym_ISR401`  
**Objetivo:** comprobar criterios de piso y los ítems específicos A1–A6 / B1–B6 antes del tag final.

## 1. Criterios de piso

- [ ] **P1 — Carátula/SGA:** confirmar que el PDF subido al SGA muestre, en una sola línea, la URL correcta del repositorio.
- [x] **P2 — Reproducibilidad documental:** `01_ERS/ERS_SRS_2B_v2.0.tex` existe y el README raíz documenta compilador, archivo principal y órdenes de compilación.
- [x] **P3 — Evidencia vacía:** las transcripciones problemáticas del paquete fueron corregidas y no se mantienen placeholders deliberados como evidencia.
- [ ] **P4 — Autoría del historial:** ejecutar una última vez `git shortlog -sne --all --use-mailmap` y comprobar identidades/correos institucionales normalizados.
- [ ] **P5 — Línea base:** crear y publicar un **tag anotado** sobre el commit definitivo. Actualmente este es el principal piso aún pendiente.
- [x] **P6 — Paquete de datos:** `07_Datos/` existe con estructura canónica y `python scripts/run_all.py` como orquestador oficial.
- [x] **P7 — Evidencia de autoría:** existe `10_Autoria/` con estructura A1–A12 y `.mailmap` en la raíz.
- [x] **P8 — Contribución individual:** Mera, Mora y Ponce poseen aportes versionados y evidencia de participación en la defensa.
- [x] **P9 — Uso de IA:** existe `10_Autoria/declaracion_uso_ia.md`.

## 2. Bloque A — correcciones específicas FabroGym

- [x] **A1 — Transcripciones vacías:** sustituidas/eliminadas como evidencia vacía; el paquete ya conserva contenido real anonimizado.
- [x] **A2 — IDs RF/RNF:** normalizados de forma continua en ERS y artefactos asociados.
- [ ] **A3 — Tag anotado:** pendiente crear y publicar después del último commit de contenido.
- [x] **A4 — Correo e identidades:** `.mailmap` presente y configuración institucional documentada.
- [x] **A5 — ERS divergente:** eliminadas las copias v2.2 del paquete; la única ERS vigente es `01_ERS/ERS_SRS_2B_v2.0.*`; el cambio quedó registrado en `CHANGELOG.md`.
- [x] **A6 — Fotos de aplicación:** existen cinco copias públicas enmascaradas y sus originales con EXIF se preservan en la capa restringida; `exif_inventario.csv` mantiene la trazabilidad.

## 3. Bloque B — agregados específicos FabroGym

### B1 — `07_Datos`

- [x] `datos_crudos/`
- [x] `datos_procesados/`
- [x] `scripts/`
- [x] `scripts/run_all.py`
- [x] `scripts/requirements.txt`
- [x] `resultados/`
- [x] `diccionario_datos.csv`
- [x] `README_datos.md`
- [x] `LICENSE-DATA.txt`
- [x] `checksums_datos.sha256`
- [x] `desviaciones.md`
- [x] `registro_deposito.md`
- [x] `07_Datos/` declarado como **único paquete canónico**.
- [ ] Ejecutar una última vez desde clon limpio y comprobar que no requiere intervención manual.

### B2 — `10_Autoria`

- [x] A1 — `bitacora_sesiones.csv`
- [x] A2 — `capturas/`
- [x] A3 — fuentes editables
- [x] A4 — `grabaciones/`
- [x] A5 — `notas_campo/`
- [x] A6 — `fotos_equipo/`
- [x] A7 — `doble_codificacion/`
- [x] A8 — `correspondencia/`
- [x] A9 — `declaracion_uso_ia.md`
- [x] A10 — `aporte_individual.md` + `aporte_individual_FIRMA.pdf`
- [x] A11 — `exif_inventario.csv`
- [x] A12 — `/.mailmap`
- [ ] Antes del tag: eliminar/sustituir cualquier marcador `PENDIENTE_COMMIT_*` que aún exista en la bitácora y sincronizar `aporte_individual.md` con los últimos commits.

### B3 — evidencia de campo

- [x] Cinco fotografías de aplicación del cuestionario.
- [x] Doble codificación independiente de al menos el 20 % del corpus de walkthroughs con dos hojas completas.

### B4 — números y documentación

- [x] Kappa/acuerdo con intervalo de confianza.
- [x] Tamaño del efecto con IC del 95 % generado por script.
- [x] Diccionario de datos.
- [x] Registro de desviaciones con fecha y motivo.

### B5 — seis requisitos del componente inteligente

- [x] Recomendación de rutina.
- [x] Explicabilidad.
- [x] Equidad.
- [x] Supervisión humana.
- [x] Monitoreo posterior.
- [x] Clasificación del nivel de riesgo.
- [x] Requisitos trazados y verificables.

### B6 — ética y protección de datos

- [x] Declaración de base de licitud/fundamento.
- [x] Finalidad.
- [x] Plazo de conservación.
- [x] Responsables de custodia.
- [x] Separación de capa pública y restringida.
- [x] Auditor automático vigente: **0 hallazgos bloqueantes**.
- [ ] Confirmar manualmente que `evidencias_restringidas.7z` está cifrado/protegido.
- [ ] Confirmar que su contraseña/clave no aparece en Git.
- [ ] Confirmar manualmente el cifrado/protección de `A11 Fotos_Originales_Cuestionario.7z`.
- [ ] Confirmar que las cinco copias públicas están autorizadas o suficientemente enmascaradas.
- [ ] Revisar visualmente consentimientos censurados/actas públicas para evitar identificadores no autorizados.

## 4. Defensa

- [x] `09_Defensa/presentacion.pptx`
- [x] `09_Defensa/presentacion.pdf`
- [x] `09_Defensa/guion.pdf`
- [x] `09_Defensa/video_defensa.mp4`
- [x] No se exige una demostración operativa en vivo del MVP.
- [x] `MANIFEST_DEFENSA.csv` actualizado después de incorporar el video.

## 5. Ciencia abierta y preservación

- [x] Zenodo v2.0.0 — DOI `10.5281/zenodo.22237884`.
- [x] OSF — DOI `10.17605/OSF.IO/62YSC`.
- [x] `fair_assessment.pdf`.
- [x] F-UJI 4.0.0 / métrica 0.8 — **88 % FAIR moderate**.
- [x] Snapshot real de Software Heritage archivado.
- [ ] Después del tag final: Software Heritage → **Save again**.

## 6. Operaciones finales — hacer en este orden

1. [ ] Corregir `10_Autoria/bitacora_sesiones.csv` si todavía contiene `PENDIENTE_COMMIT_CIERRE_MVP_DEFENSA_AUTORIA`.
2. [ ] Sincronizar `10_Autoria/aporte_individual.md` con los últimos commits reales.
3. [ ] Confirmar manualmente privacidad/cifrado de B6.
4. [ ] Corregir, si aún existe, el nombre `Aplicacion_Cuestionario_01..jpg` a `Aplicacion_Cuestionario_01.jpg` y sincronizar su ruta en el inventario.
5. [ ] Ejecutar el auditor de privacidad y confirmar **0 bloqueos**.
6. [ ] Regenerar/verificar `checksums.sha256` general como uno de los últimos cambios.
7. [ ] Clonar el repositorio en una carpeta limpia.
8. [ ] Compilar la ERS desde `01_ERS/`.
9. [ ] Ejecutar `07_Datos/scripts/run_all.py`.
10. [ ] Ejecutar `git shortlog -sne --all --use-mailmap`.
11. [ ] Confirmar `git status` limpio.
12. [ ] Crear el tag anotado final y publicarlo.
13. [ ] Verificar en GitHub que el tag remoto existe.
14. [ ] Software Heritage → **Save again**.

## 7. Regla de congelamiento

Después de crear el tag anotado no se debe modificar el contenido entregado salvo que exista un error real que obligue a crear una nueva línea base.

La versión evaluable será el commit alcanzado por el tag anotado publicado.
