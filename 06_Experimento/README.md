# 06_Experimento - FabroGym

Esta carpeta contiene el componente empírico de **FabroGym - Enfoque 3: Explicabilidad como Requisito No Funcional (RNF)**.

## Estado actual

La evidencia empírica disponible está constituida por **seis walkthroughs reales ya realizados antes del registro OSF**: tres con participantes técnicos y tres con participantes no técnicos. Estas sesiones se tratan como evidencia previa/formativa y no como datos confirmatorios preregistrados.

El registro OSF se realizará después de estas seis sesiones. Su finalidad es documentar transparentemente el estado temporal del estudio y congelar las decisiones analíticas y las actividades que todavía se encuentren pendientes.

No se declaran rondas adicionales de walkthrough ni se divide artificialmente la evidencia existente en Ronda 1 / Ronda 2.

## Protocolo vigente

El protocolo activo corresponde a la **versión 1.2**:

```text
06_Experimento/protocolo.tex
06_Experimento/protocolo.pdf
```

El protocolo establece un estudio de caso único basado en la sistematización cualitativa y descriptiva de los seis walkthroughs existentes, la formulación trazable de candidatos a RNF y el member checking final si esta actividad todavía se encuentra pendiente.

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

- `01_Guia_Walkthrough_Explicabilidad.pdf` estructura la **sistematización** de la evidencia ya disponible.
- `02_Matriz_Codificacion_Walkthroughs.csv` registra unidades temáticas trazables de los walkthroughs.
- `03_Matriz_Candidatos_RNF_Explicabilidad.csv` registra candidatos a RNF derivados únicamente de evidencia verificable.
- `04_Ficha_Caracterizacion_Participante.pdf` permite documentar información de perfil solo cuando pueda verificarse.
- `05_Matriz_Operacionalizacion_Explicabilidad.csv` documenta las variables y tratamientos definidos en el protocolo v1.2.
- `06_Acta_Member_Checking.pdf` se utiliza únicamente si la sesión final de member checking todavía se encuentra pendiente y se ejecuta.

No se mantiene un cuestionario Likert como instrumento activo mientras no existan respuestas Likert reales y verificables correspondientes al estudio de explicabilidad.

## Análisis previsto

El análisis se limita a la evidencia realmente disponible e incluye, cuando sea sustentable:

- codificación y síntesis cualitativa de necesidades de explicabilidad;
- formulación y refinamiento de candidatos a RNF con trazabilidad a su evidencia de origen;
- contraste descriptivo y cualitativo entre participantes técnicos y no técnicos;
- conteos de categorías o dimensiones cuando provengan de una codificación reproducible;
- cobertura de dimensiones mediante candidatos a RNF verificables, únicamente cuando el denominador y la clasificación puedan establecerse de forma trazable;
- resumen del member checking si la actividad se ejecuta.

No se preregistran ni se ejecutan por defecto U de Mann-Whitney, tamaños del efecto, intervalos de confianza sobre puntuaciones Likert o kappa entre rondas. Si los datos necesarios no existen, el análisis correspondiente se declara **no aplicable** o **no calculable**.

## Scripts reproducibles

Los scripts activos se encuentran en:

```text
06_Experimento/scripts_analisis/
```

Su función es validar matrices, resumir la codificación existente, calcular conteos descriptivos y cobertura cuando corresponda, y procesar las decisiones de member checking si se dispone de ellas.

Los scripts del experimento anterior de detección de ambigüedad, Precision, Recall, F1, McNemar o consenso experto no forman parte del árbol activo del Enfoque 3. La trazabilidad de esas versiones permanece en el historial Git.

## Resultados

Los productos reproducibles se almacenarán en:

```text
06_Experimento/resultados/
```

La carpeta no debe contener resultados inventados. Sus archivos se generan únicamente a partir de matrices o evidencias reales y verificables.

## Prerregistro OSF

Mientras no exista el comprobante oficial se conserva:

```text
06_Experimento/PENDIENTE_osf_registration.md
```

Después de formalizar el registro, el comprobante oficial se guardará como:

```text
06_Experimento/osf_registration.pdf
```

El registro deberá declarar expresamente que los seis walkthroughs fueron realizados antes del sello temporal de OSF.

## Privacidad

El paquete público no debe incluir nombres completos de participantes, cédulas, firmas, teléfonos, correos personales, audios, videos, rostros identificables o consentimientos firmados.

Los materiales identificables permanecen en la zona restringida. Las matrices públicas utilizan códigos seudónimos o datos agregados y no completan por inferencia información que no pueda verificarse.
