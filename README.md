# FabroGym — Ingeniería de Requerimientos (ISR-401)

Repositorio académico del proyecto **FabroGym**, desarrollado en la Universidad Técnica Estatal de Quevedo para documentar la especificación, evidencia, modelado, trazabilidad, MVP y componente empírico del proyecto.

## Estado actual

El trabajo vigente corresponde a la **Entrega 4 (2B / Defensa Final)**. El componente empírico activo utiliza el **Enfoque 3: Explicabilidad como Requisito No Funcional (RNF)**.

El protocolo de prerregistro vigente es la **versión 1.3, actualizada el 28 de agosto de 2026**, disponible en:

```text
06_Experimento/protocolo.tex
06_Experimento/protocolo.pdf
```

Antes del registro OSF se realizaron **seis walkthroughs reales**: tres con participantes de perfil técnico y tres con participantes de perfil no técnico. Estas sesiones se consideran evidencia empírica **previa/formativa** y no datos confirmatorios preregistrados.

El registro OSF se realizará después de esas seis sesiones y antes de la codificación y el análisis sistemático definidos en el protocolo. No se declaran rondas adicionales de walkthrough ni se divide artificialmente la evidencia existente.

Mientras no exista el comprobante oficial del registro OSF se conserva:

```text
06_Experimento/PENDIENTE_osf_registration.md
```

## Estructura del repositorio

```text
FabroGym_ISR401/
├── 01_ERS/              # Especificación de requisitos
├── 02_Evidencias/       # Evidencia pública anonimizada y zona restringida
├── 03_Modelado/         # Diagramas UML y mockups
├── 04_Trazabilidad/     # Matriz de trazabilidad
├── 05_MVP/              # MVP académico y video de demostración
├── 06_Experimento/      # Componente empírico vigente y prerregistro OSF
├── 07_Publicacion/      # Paquete histórico de publicación de la Entrega 3 (2A)
├── 08_ETICA/            # Documentación ética del proyecto
├── 09_Defensa/          # Artefactos de presentación y defensa
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
└── checksums.sha256
```

`07_Publicacion/` conserva artefactos de la **Entrega 3 (2A)** como evidencia histórica. Sus descripciones de estado deben interpretarse en el contexto temporal de esa entrega y no como el estado vigente del componente empírico 2B.

## Componente empírico vigente

La carpeta `06_Experimento/` contiene el paquete metodológico activo del Enfoque 3.

### Instrumentos y matrices

```text
06_Experimento/instrumentos/
├── 01_Guia_Walkthrough_Explicabilidad.pdf
├── 02_Matriz_Codificacion_Walkthroughs.csv
├── 03_Matriz_Candidatos_RNF_Explicabilidad.csv
├── 04_Ficha_Caracterizacion_Participante.pdf
├── 05_Matriz_Operacionalizacion_Explicabilidad.csv
└── 06_Acta_Member_Checking.pdf
```

No existe un cuestionario Likert activo para el estudio de explicabilidad. Tampoco se preregistran por defecto U de Mann-Whitney, tamaños del efecto, intervalos de confianza sobre puntuaciones Likert ni kappa entre rondas cuando los datos necesarios no existen.

### Análisis reproducible

Los scripts activos se encuentran en:

```text
06_Experimento/scripts_analisis/
```

Su función es validar las matrices, sistematizar la codificación real disponible, resumir necesidades de explicabilidad, analizar candidatos a RNF y procesar el member checking únicamente si existe evidencia de esa actividad.

Los resultados se generan en:

```text
06_Experimento/resultados/
```

No se incorporan resultados hipotéticos ni se completan datos faltantes por inferencia.

## Privacidad y evidencia

El repositorio público debe contener únicamente información apta para publicación. No deben publicarse nombres completos de participantes, cédulas, firmas, teléfonos, correos personales, audios, videos, rostros identificables, consentimientos originales ni otra información que permita reidentificación.

La carpeta `02_Evidencias/00_Restringido/` es una **clasificación documental y no un mecanismo de control de acceso**. Cualquier material identificable que permanezca versionado en un repositorio público debe estar protegido conforme al protocolo y a las autorizaciones aplicables; las credenciales o claves de cifrado nunca deben almacenarse en este repositorio.

## Reproducibilidad y congelamiento

`checksums.sha256` se utiliza para verificar la integridad del estado preparado para registro. Debe regenerarse **solo después de completar todas las correcciones previas al congelamiento**.

El SHA que se declare en OSF debe corresponder al commit definitivo generado después de:

1. cerrar la revisión de coherencia documental;
2. verificar privacidad y ausencia de información publicable indebidamente;
3. regenerar `checksums.sha256`;
4. revisar que no queden referencias obsoletas al Enfoque 2, Likert o versiones anteriores del protocolo.

## Licenciamiento y citación

Consulte `LICENSE` para los términos aplicables al código, documentación y datos anonimizados, y `CITATION.cff` para la información de citación del proyecto.
