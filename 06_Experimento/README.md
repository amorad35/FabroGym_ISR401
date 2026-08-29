# 06_Experimento - FabroGym

Esta carpeta contiene el componente empírico de **FabroGym - Enfoque 3: Explicabilidad como Requisito No Funcional (RNF)**.

## Estado actual

La evidencia empírica disponible está constituida por **seis walkthroughs reales realizados antes del registro OSF**: tres con participantes técnicos y tres con participantes no técnicos. Estas sesiones corresponden a **validaciones generales de FabroGym**, se tratan como evidencia previa/formativa y no como datos confirmatorios preregistrados.

El **prerregistro cualitativo fue formalizado y publicado en OSF Registries el 29 de agosto de 2026**, después de estas seis sesiones y antes de la codificación y el análisis sistemático definidos en el protocolo. El registro público se encuentra en:

- **OSF:** https://osf.io/62ysc/
- **DOI:** https://doi.org/10.17605/OSF.IO/62YSC
- **Tipo de registro:** Qualitative Preregistration
- **Commit congelado pre-OSF:** `d2886d7453185daca62427c75729773b3510d1bb`

No se presupone que las seis sesiones hayan evaluado una misma explicación estructurada ni que en todas se haya presentado un componente específico de recomendación de rutinas. Después del registro se realizará la codificación sistemática de la evidencia completa y únicamente los fragmentos con relación verificable con explicabilidad se utilizarán para formular o refinar candidatos a RNF de este enfoque.

No se declaran rondas adicionales de walkthrough ni se divide artificialmente la evidencia existente en Ronda 1 / Ronda 2.

## Protocolo vigente

El protocolo activo corresponde a la **versión 1.4**:

```text
06_Experimento/protocolo.tex
06_Experimento/protocolo.pdf
```

La versión 1.4 conserva la secuencia temporal definida en la v1.3 y corrige la correspondencia entre la naturaleza general de los walkthroughs ya realizados y el análisis posterior de explicabilidad.

El protocolo establece un estudio de caso único basado en la sistematización cualitativa y descriptiva de los seis walkthroughs existentes, la identificación trazable de fragmentos pertinentes para explicabilidad, la formulación de candidatos a RNF y el member checking final si esta actividad todavía se encuentra pendiente.

## Evidencia de walkthroughs

Los seis walkthroughs satisfacen el mínimo de sesiones establecido para la validación terminal: **3 técnicas + 3 no técnicas**.

La sistematización debe preservar la fecha y naturaleza real de cada sesión. La fecha de incorporación posterior a GitHub u OSF no modifica su clasificación temporal.

El guion o instrumento realmente utilizado en cada sesión se conserva como evidencia del procedimiento cuando exista. Los instrumentos creados posteriormente para sistematizar la explicabilidad no se presentan retroactivamente como si hubieran sido aplicados durante las sesiones.

## Instrumentos y matrices activas

```text
06_Experimento/instrumentos/
├── 01_Guia_Walkthrough_Explicabilidad.pdf
├── 02_Matriz_Codificacion_Walkthroughs.csv
├── 03_Matriz_Candidatos_RNF_Explicabilidad.csv
├── 04_Ficha_Caracterizacion_Participante.pdf
├── 05_Matriz_Operacionalizacion_Explicabilidad.csv
└── 06_Acta_Member_Checking.pdf
```

- `01_Guia_Walkthrough_Explicabilidad.pdf` estructura la **sistematización posterior** de la evidencia disponible; no se presenta como el instrumento aplicado retroactivamente en las seis sesiones.
- `02_Matriz_Codificacion_Walkthroughs.csv` registra unidades temáticas trazables de los walkthroughs.
- `03_Matriz_Candidatos_RNF_Explicabilidad.csv` registra candidatos a RNF derivados únicamente de fragmentos verificables pertinentes para explicabilidad.
- `04_Ficha_Caracterizacion_Participante.pdf` permite documentar información de perfil solo cuando pueda verificarse.
- `05_Matriz_Operacionalizacion_Explicabilidad.csv` documenta las variables y tratamientos definidos para el análisis.
- `06_Acta_Member_Checking.pdf` se utiliza únicamente si la sesión final de member checking todavía se encuentra pendiente y se ejecuta.

No se mantiene un cuestionario Likert como instrumento activo mientras no existan respuestas Likert reales y verificables correspondientes al estudio de explicabilidad.

## Análisis previsto

El análisis se limita a la evidencia realmente disponible e incluye, cuando sea sustentable:

- codificación cualitativa de los seis walkthroughs y conservación de sus hallazgos generales;
- identificación trazable del subconjunto de fragmentos pertinente para explicabilidad;
- síntesis de necesidades de explicabilidad sustentadas por ese subconjunto;
- formulación y refinamiento de candidatos a RNF con trazabilidad a su evidencia de origen;
- contraste descriptivo y cualitativo entre participantes técnicos y no técnicos únicamente sobre evidencia pertinente;
- conteos de categorías o dimensiones cuando provengan de una codificación reproducible;
- cobertura de dimensiones mediante candidatos a RNF verificables, únicamente cuando el denominador y la clasificación puedan establecerse de forma trazable;
- resumen del member checking si la actividad se ejecuta.

No se preregistran ni se ejecutan por defecto U de Mann-Whitney, tamaños del efecto, intervalos de confianza sobre puntuaciones Likert o kappa entre rondas. Si los datos necesarios no existen, el análisis correspondiente se declara **no aplicable** o **no calculable**.

## Scripts reproducibles

Los scripts activos se encuentran en:

```text
06_Experimento/scripts_analisis/
```

Su función es validar matrices, resumir la codificación existente, calcular conteos descriptivos y cobertura cuando corresponda, y procesar las decisiones de member checking si se dispone de ellas. Cualquier ajuste técnico necesario para reflejar la matriz final se realizará después del registro y quedará versionado.

Los scripts del experimento anterior de detección de ambigüedad, Precision, Recall, F1, McNemar o consenso experto no forman parte del árbol activo del Enfoque 3. La trazabilidad de esas versiones permanece en el historial Git.

## Resultados

Los productos reproducibles se almacenarán en:

```text
06_Experimento/resultados/
```

La carpeta no debe contener resultados inventados. Sus archivos se generan únicamente a partir de matrices o evidencias reales y verificables.

## Prerregistro OSF

El prerregistro cualitativo del estudio fue formalizado en **OSF Registries** el **29 de agosto de 2026**.

- **Registro público:** https://osf.io/62ysc/
- **DOI:** https://doi.org/10.17605/OSF.IO/62YSC
- **Tipo:** Qualitative Preregistration
- **Protocolo registrado:** versión 1.4
- **Commit congelado pre-OSF:** `d2886d7453185daca62427c75729773b3510d1bb`

El comprobante documental del registro se conserva como:

```text
06_Experimento/osf_registration.pdf
```

El registro declara expresamente que los seis walkthroughs fueron realizados antes del sello temporal de OSF, que corresponden a validaciones generales de FabroGym y que constituyen evidencia previa/formativa, no datos confirmatorios preregistrados.

Asimismo, no se afirma retroactivamente que las seis sesiones evaluaron una misma explicación estructurada ni que en todas se presentó un componente específico de recomendación de rutinas. La codificación y el análisis sistemático se realizan después del registro, utilizando únicamente evidencia verificable y trazable.

## Privacidad

El paquete público no debe incluir nombres completos de participantes, cédulas, firmas, teléfonos, correos personales, audios, videos, rostros identificables o consentimientos firmados.

Los materiales identificables permanecen en la zona restringida. Las matrices públicas utilizan códigos seudónimos o datos agregados y no completan por inferencia información que no pueda verificarse.
