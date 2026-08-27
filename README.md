# 06_Experimento - FabroGym

Esta carpeta contiene el componente empírico del proyecto **FabroGym**, correspondiente al **Enfoque 3: Explicabilidad como Requisito No Funcional (RNF)**.

El estudio tiene como finalidad identificar, refinar y validar requisitos de explicabilidad aplicables a un componente propuesto de recomendación de rutinas, considerando la percepción de perfiles técnicos y no técnicos vinculados al dominio del sistema.

## Estado actual

- `protocolo.tex` y `protocolo.pdf`: actualizados a la versión 1.1 del protocolo de prerregistro.
- El prerregistro en Open Science Framework (OSF) aún no se ha realizado.
- `PENDIENTE_osf_registration.md` se mantiene como marcador hasta obtener el comprobante oficial del registro.
- Las sesiones walkthrough realizadas antes del sello temporal de OSF se consideran evidencia exploratoria o formativa.
- La ronda empírica confirmatoria deberá ejecutarse después del prerregistro OSF.
- Los materiales pertenecientes al enfoque experimental anterior todavía deben separarse y conservarse en una carpeta histórica.
- Los instrumentos, scripts de análisis y estructura de resultados del Enfoque 3 se encuentran pendientes de actualización y alineación con el protocolo vigente.

## Diseño empírico

El protocolo distingue dos etapas de trabajo:

### Validación exploratoria o formativa

Las entrevistas, encuestas, walkthroughs u otras actividades realizadas antes del sello temporal de OSF pueden utilizarse como antecedentes para:

- identificar necesidades preliminares de explicabilidad;
- refinar escenarios de validación;
- mejorar el guion de walkthrough;
- definir dimensiones del cuestionario;
- formular candidatos iniciales a RNF de explicabilidad.

Los datos obtenidos en esta etapa no formarán parte de la base confirmatoria ni de los contrastes estadísticos preregistrados.

### Ronda confirmatoria

Después del prerregistro OSF se ejecutará la nueva ronda empírica definida en el protocolo. Esta etapa contemplará, según corresponda:

- walkthroughs con perfiles técnicos y no técnicos;
- cuestionario Likert de explicabilidad;
- identificación y refinamiento de candidatos a RNF;
- comparación entre perfiles;
- cobertura de dimensiones de explicabilidad;
- member checking;
- análisis cualitativo y cuantitativo reproducible.

Los análisis confirmatorios se realizarán únicamente con datos obtenidos después del sello temporal del prerregistro.

## Instrumentos previstos

El paquete metodológico del Enfoque 3 deberá incluir instrumentos equivalentes a los siguientes:

```text
06_Experimento/instrumentos/
├── 01_Guia_Walkthrough_Explicabilidad.pdf
├── 02_Cuestionario_Likert_Explicabilidad.pdf
├── 03_Matriz_Candidatos_RNF_Explicabilidad.csv
├── 04_Ficha_Caracterizacion_Participante.pdf
├── 05_Matriz_Operacionalizacion_Explicabilidad.csv
└── 06_Acta_Member_Checking.pdf
```

Estos archivos deberán corresponder a plantillas e instrumentos metodológicos. No deben contener resultados confirmatorios antes de la recolección correspondiente.

## Organización del experimento anterior

Los materiales asociados al enfoque previo de detección de ambigüedad y evaluación experta no forman parte del estudio que se prerregistrará en OSF.

Estos archivos deberán conservarse, sin eliminarlos, en una estructura histórica separada, por ejemplo:

```text
06_Experimento/historico_enfoque2/
```

La finalidad de esta separación es mantener trazabilidad del trabajo anterior y evitar que sus instrumentos, fuentes, scripts o plantillas se confundan con el Enfoque 3.

## Análisis previsto

El análisis del Enfoque 3 deberá alinearse con el protocolo vigente e incluir, cuando corresponda:

- estadísticos descriptivos de las respuestas Likert;
- análisis por perfil técnico y no técnico;
- comparación entre perfiles mediante U de Mann-Whitney;
- tamaño del efecto;
- cobertura de dimensiones de explicabilidad;
- cobertura y validación de candidatos a RNF;
- acuerdo entre evaluadores o rondas cuando proceda;
- member checking;
- síntesis cualitativa de observaciones;
- tablas y figuras reproducibles mediante scripts versionados.

Los scripts y archivos de resultados asociados exclusivamente al detector de ambigüedad, Precision, Recall, F1, McNemar o consenso experto pertenecen al enfoque anterior y deberán archivarse o sustituirse según corresponda.

## Prerregistro OSF

El registro OSF debe realizarse antes de iniciar la nueva ronda empírica confirmatoria.

Hasta obtener el comprobante oficial se mantiene:

```text
06_Experimento/PENDIENTE_osf_registration.md
```

Después de completar y aprobar el registro, el comprobante deberá conservarse como:

```text
06_Experimento/osf_registration.pdf
```

La versión del paquete experimental utilizada para el prerregistro deberá identificarse mediante el SHA del commit de congelamiento correspondiente.

## Privacidad y gestión de datos

La carpeta pública del experimento podrá contener únicamente instrumentos vacíos, scripts, documentación metodológica y datos anonimizados o seudonimizados que puedan compartirse legítimamente.

Los siguientes elementos deben permanecer fuera del paquete público:

- nombres completos de participantes;
- cédulas;
- firmas;
- correos personales;
- números telefónicos;
- audios;
- videos;
- fotografías identificables;
- consentimientos firmados;
- cualquier otro dato personal o identificador directo.

Las evidencias restringidas deberán mantenerse en la zona correspondiente del proyecto y no publicarse directamente en OSF.

## Reproducibilidad

Los datos confirmatorios, una vez obtenidos y anonimizados, deberán poder procesarse mediante scripts versionados dentro de:

```text
06_Experimento/scripts_analisis/
```

Las tablas, métricas y figuras resultantes deberán generarse de manera reproducible y almacenarse en:

```text
06_Experimento/resultados/
```

La estructura definitiva de estas carpetas se actualizará antes del congelamiento del paquete para prerregistro.
