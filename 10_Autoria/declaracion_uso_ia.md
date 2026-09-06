# Declaración de uso de inteligencia artificial — FabroGym

**Proyecto:** FabroGym — Ingeniería de Requerimientos ISR-401  
**Entrega:** Entrega 4 (2B / Defensa Final)  
**Artefacto:** A9 — `10_Autoria/declaracion_uso_ia.md`  
**Estado de este archivo:** **FINAL — revisión consolidada. Ponce queda registrado como verificador humano y no permanecen filas `POR CONFIRMAR`.**

---

## 1. Principio de declaración

El equipo declara el uso de herramientas de inteligencia artificial de forma transparente y por artefacto o sección relevante.

La IA se utilizó como herramienta de apoyo para revisión, organización, redacción técnica, generación de borradores de documentación, preparación y corrección de scripts, revisión de código, comprobaciones de consistencia y preparación de materiales de defensa. La responsabilidad académica, la aceptación de cambios, la integración al repositorio y la interpretación de los resultados corresponde a los integrantes del equipo.

La IA **no se considera fuente de evidencia primaria**. No se utiliza para inventar entrevistas, walkthroughs, fotografías, capturas, firmas, consentimientos, respuestas de participantes, fechas, comunicaciones, commits ni resultados empíricos inexistentes.

Cuando una salida de IA propone código, texto académico o una transformación de datos, el resultado solo se acepta después de contrastarlo con los archivos reales del proyecto y, cuando corresponde, ejecutarlo o revisarlo sobre los datos y artefactos versionados.

---

## 2. Herramienta identificada en el cierre 2B

| Herramienta | Proveedor | Modelo / versión documentada | Temperatura | Uso general documentado |
|---|---|---|---|---|
| ChatGPT | OpenAI | GPT-5.6 Sol en la sesión de cierre 2B documentada | No expuesta ni configurable por el equipo en la interfaz utilizada | Auditoría y revisión de consistencia; apoyo de redacción; generación y corrección de documentación técnica; preparación de scripts reproducibles; revisión/corrección de código; validación estructural de artefactos; organización del cierre 2B y preparación de defensa. |

> **Nota de trazabilidad del modelo.** Para sesiones históricas en las que la interfaz no dejó un registro verificable del modelo exacto o de parámetros como temperatura, el equipo no reconstruye retrospectivamente valores no observados. Se documenta el modelo visible en la sesión de cierre y se deja constancia de que la temperatura no fue expuesta ni configurada manualmente.

> Con base en el expediente revisado para este cierre no se identificó otra herramienta de IA que deba declararse. Si un integrante hubiera utilizado otra herramienta de IA fuera del expediente documentado, deberá incorporarla antes del commit definitivo; no debe agregarse una herramienta que no haya sido utilizada realmente.

---

## 3. Declaración por artefacto / sección relevante

| Sección o artefacto | Uso de IA | Herramienta | Finalidad del uso | Verificador humano | Método de verificación | Estado |
|---|---|---|---|---|---|---|
| `01_ERS/` — revisión y normalización de ERS/SRS | Sí | ChatGPT | Detectar inconsistencias, apoyar normalización de identificadores, revisar trazabilidad y proponer correcciones documentales. | Ponce | Comparación contra ERS/SRS real, matrices del repositorio, requisitos normalizados y trazabilidad. | **CERRADO** |
| Requisitos RF/RNF/RD y trazabilidad | Sí | ChatGPT | Apoyo para detectar IDs inconsistentes, duplicados, huecos y relaciones de trazabilidad. | Ponce | Revisión contra archivos fuente y conteos finales; comprobación de rutas e IDs reales. | **CERRADO** |
| UML, diagramas y mockups originales | No se atribuye IA a la creación original; **sí hubo IA en la revisión y normalización 2B** | ChatGPT, únicamente para revisión/normalización 2B | Conservar los artefactos originales, revisar consistencia, normalizar referencias/IDs y documentar incidencias sin atribuir a IA una autoría original no demostrada. | Ponce | Contraste con fuentes editables A3, inventario UML disponible, archivos existentes y cambios documentados durante la normalización 2B. | **CERRADO — sin atribución de autoría original a IA** |
| Evidencia primaria: entrevistas | No para generar evidencia | — | La IA no produjo respuestas, audios, videos, fechas ni contenido atribuido a participantes. | Ponce | Contraste con evidencia primaria real, fichas técnicas y archivos de sesión. | **CERRADO** |
| Evidencia primaria: walkthroughs | No para generar evidencia; sí como apoyo documental posterior | ChatGPT para organización/análisis documental | La IA no produjo observaciones o respuestas ficticias; se utilizó posteriormente para apoyar organización, consolidación y análisis documental. | Ponce | Contraste con actas, corpus y archivos reales de WALK. | **CERRADO** |
| Cuestionario y conjunto analítico `n=70` | Sí, solo para revisión/procesamiento documental | ChatGPT | Apoyo para estructurar documentación, controles del corte analítico y coherencia de archivos derivados. | Ponce | Contraste con exportación real y ejecución/revisión de scripts; sin modificar respuestas originales. | **CERRADO** |
| F3-02 / A7 — doble codificación | Sí, como apoyo técnico | ChatGPT | Preparar estructura, subconjunto, hojas y script de cálculo de acuerdo. | Ponce | Contraste con las dos hojas/codificaciones humanas y ejecución del cálculo sobre los archivos reales. | **CERRADO — confirmación humana incorporada** |
| F3-03 — kappa e IC95 % | Sí, como apoyo de programación | ChatGPT | Preparación del script reproducible para cálculo del acuerdo e intervalo de confianza. | Ponce | Ejecución del script sobre las dos codificaciones humanas y revisión del resultado. | **CERRADO** |
| F3-04 — tamaño del efecto e IC95 % técnico vs no técnico | Sí | ChatGPT | Preparación del script, documentación metodológica y salida reproducible del análisis descriptivo-exploratorio. | Ponce | Ejecución de `calcular_efecto_perfiles.py`, contraste con CSV fuente y revisión de la interpretación. | **CERRADO** |
| F3-05 — diccionario de datos | Sí | ChatGPT | Completar descripciones de columnas a partir de nombres, valores observados y transformaciones documentadas. | Ponce | Comparación columna por columna con CSV reales y pipeline. | **CERRADO** |
| F3-06 — separación crudo/procesado y proveniencia | Sí | ChatGPT | Redactar y organizar documentación de proveniencia y mapeo fuente → transformación → salida. | Ponce | Verificación de rutas reales, entradas, salidas y scripts existentes. | **CERRADO** |
| F3-07 — capas pública/restringida | Sí | ChatGPT | Apoyo para política de privacidad, reglas de `.gitignore` y script de revisión automática. | Ponce | Ejecución del verificador sobre el repositorio integrado y revisión visual/manual de archivos sensibles. | **CERRADO** |
| F3-08 — desviaciones del protocolo | Sí | ChatGPT | Ayudar a estructurar el registro de desviaciones reales sin alterar retrospectivamente el protocolo. | Ponce | Contraste con protocolo v1.4, OSF, cronología real y artefactos reproducibles. | **CERRADO** |
| `06_Experimento/scripts_analisis/` | Sí | ChatGPT | Apoyo en generación/corrección de código Python y documentación de reproducibilidad. | Ponce | Ejecución local de scripts; comparación de salidas con datos de entrada; revisión del código antes de integración. | **CERRADO** |
| `07_Datos/scripts/` y documentación de datos | Sí | ChatGPT | Apoyo en scripts espejo, documentación, inventarios y controles de consistencia. | Ponce | Ejecución local y contraste con estructura real de `07_Datos/`. | **CERRADO** |
| Resultados, cifras y tablas empíricas | IA solo como apoyo técnico, no como fuente de resultados | ChatGPT + scripts versionados | La IA ayudó a escribir/revisar código y a explicar resultados; las cifras finales proceden de datos y scripts ejecutables. | Ponce | Regeneración/contraste de resultados desde datos y scripts; revisión de que las cifras tengan respaldo reproducible. | **CERRADO** |
| Registro de desviaciones / OSF | Sí | ChatGPT | Apoyo de redacción y consistencia metodológica. | Ponce | Contraste con registro OSF, fechas reales y protocolo. | **CERRADO** |
| Zenodo / FAIR / documentación de publicación | Sí | ChatGPT | Revisión de coherencia de DOI, README, CITATION y documentación FAIR. | Ponce | Verificación de identificadores contra depósitos reales y archivos del repositorio cuando están disponibles. | **CERRADO** |
| Manuscrito — título, resumen y palabras clave | Sí | ChatGPT | Apoyo de redacción, edición, síntesis y adecuación a la estructura editorial requerida. | Ponce | Comparación con el manuscrito versionado y verificación de que datos, alcance y afirmaciones correspondan al proyecto real. | **CERRADO** |
| Manuscrito — Introducción | Sí | ChatGPT | Apoyo de claridad, estructura, revisión y redacción técnica a partir del dominio y evidencia ya documentados. | Ponce | Revisión humana y contraste de afirmaciones con fuentes, ERS/SRS y evidencia del proyecto. | **CERRADO** |
| Manuscrito — Trabajo relacionado | Sí | ChatGPT | Apoyo de organización, redacción y revisión del posicionamiento bibliográfico. | Ponce | Comprobación de referencias contra `referencias.bib` y fuentes reales; no se aceptan referencias inventadas. | **CERRADO** |
| Manuscrito — Metodología | Sí, en el cierre 2B | ChatGPT | Apoyo para documentar procedimiento, desviaciones, reproducibilidad y limitaciones metodológicas. | Ponce | Contraste con protocolo, OSF, datos, scripts y cronología real. | **CERRADO** |
| Manuscrito — Resultados | Sí, únicamente como apoyo de redacción/interpretación de salidas reproducibles | ChatGPT | Ayudar a describir resultados ya obtenidos por scripts; no producir datos. | Ponce | Toda cifra se contrasta/regenera desde scripts y datos publicados o versionados. | **CERRADO** |
| Manuscrito — Discusión | Sí | ChatGPT | Apoyo de redacción, organización de la argumentación e interpretación limitada al alcance de los resultados reales. | Ponce | Contraste de la interpretación con resultados reproducibles y bibliografía revisada. | **CERRADO** |
| Manuscrito — Amenazas a la validez | Sí, en el cierre 2B | ChatGPT | Apoyo para identificar y redactar amenazas/limitaciones a partir del procedimiento real. | Ponce | Revisión humana contra diseño real, muestra, protocolo y análisis ejecutado. | **CERRADO** |
| Manuscrito — Conclusiones | Sí | ChatGPT | Apoyo de redacción y síntesis final. | Ponce | Confirmación de que cada conclusión deriva de resultados reales y no incorpora hallazgos nuevos no sustentados. | **CERRADO** |
| Ética y privacidad `08_Etica/` | Sí, como apoyo documental | ChatGPT | Revisión de estructura, separación pública/restringida y controles de privacidad. | Ponce | Contraste con documentos éticos reales; la IA no genera firmas, consentimientos o autorizaciones inexistentes. | **CERRADO** |
| MVP / código de aplicación | Sí, como apoyo de desarrollo y revisión | ChatGPT | Apoyo para revisar/corregir código del MVP, alinear funcionalidades con requisitos y documentar cambios técnicos. | Ponce | Contraste con historial/diffs disponibles, `05_MVP/MVP_HTML/assets/js/app.js`, documentación del parche y pruebas del MVP. | **CERRADO** |
| Defensa / material de presentación | Sí, como apoyo de preparación | ChatGPT | Apoyo para síntesis, banco de preguntas y respuestas, escenarios de demostración, checklist y preparación del guion/material de defensa. | Ponce | Contraste con artefactos finales del repositorio, especialmente `09_Defensa/banco_preguntas_respuestas.md`, `09_Defensa/escenarios_demo.md` y checklist asociado. | **CERRADO** |
| `10_Autoria/` — estructura, plantillas y controles | Sí | ChatGPT | Apoyo para organizar evidencia A1–A12, preparar plantillas y reglas de integridad. | Ponce | Solo aceptar evidencia real; contraste de archivos con fechas, metadatos y Git cuando corresponde. | **CERRADO** |
| A8 — `correspondencia/` | Sí, únicamente para estructura documental | ChatGPT | Preparar carpetas, inventario y guía de privacidad. | Ponce | Las capturas/mensajes corresponden a comunicaciones reales; la IA no genera correspondencia histórica. | **CERRADO** |
| A9 — `declaracion_uso_ia.md` | Sí | ChatGPT | Preparar, revisar y consolidar esta declaración a partir de los usos documentados y del cierre realizado por el equipo. | Ponce | Revisión final línea por línea, eliminación de estados pendientes y comprobación de coherencia con los artefactos documentados. | **FINAL** |

---

## 4. Métodos de verificación humana utilizados/aceptados para este proyecto

Según el tipo de salida, la comprobación queda descrita con el método pertinente. Entre los métodos empleados o aplicables al cierre están:

- comparación contra evidencia primaria real;
- comparación con ERS/SRS, matrices y trazabilidad versionadas;
- revisión de diffs y commits Git cuando están disponibles;
- ejecución de scripts Python sobre datos reales;
- comparación de tablas generadas contra CSV de entrada;
- comprobación de DOI, OSF y otras referencias contra sus registros reales cuando corresponda;
- revisión de fuentes bibliográficas;
- inspección de rutas y archivos en el repositorio;
- revisión cruzada por integrantes del equipo;
- validación manual de privacidad y anonimización;
- comprobación de metadatos y hashes cuando corresponda.

La declaración no convierte a la IA en verificadora ni en fuente de autoridad. La aceptación final de cada cambio corresponde al equipo humano.

---

## 5. Usos expresamente excluidos

El equipo no presenta como uso válido de IA:

- creación de entrevistas o respuestas inexistentes;
- reconstrucción de notas de campo como si fueran contemporáneas;
- creación de fotografías o capturas para simular trabajo histórico;
- generación de firmas o consentimientos;
- creación de correspondencia retroactiva;
- alteración de fechas o metadatos;
- asignación ficticia de autoría o commits;
- invención de resultados, tamaños de muestra, métricas, tablas o cifras;
- modificación retrospectiva del protocolo para hacer coincidir los resultados;
- generación de conclusiones no sustentadas por los datos.

---

## 6. Cierre de A9

Para el cierre de esta declaración se efectuó la consolidación de las filas pendientes y se adoptaron los siguientes criterios:

1. **Ponce** queda registrado como verificador humano del documento.
2. Las cinco secciones pendientes del manuscrito —título/resumen/palabras clave, Introducción, Trabajo relacionado, Discusión y Conclusiones— quedan declaradas con **uso de ChatGPT como apoyo de redacción/revisión**, no como fuente de datos ni como autor académico.
3. El **MVP/código** queda declarado con uso de ChatGPT como apoyo de desarrollo, revisión y corrección técnica.
4. La **defensa** queda declarada con uso de ChatGPT como apoyo de preparación, síntesis, preguntas, escenarios y checklist; esta declaración no implica que la IA haya realizado la defensa ni generado evidencia audiovisual de ella.
5. Para **UML, diagramas y mockups originales** no se atribuye a IA la autoría original porque el expediente revisado no demuestra ese hecho. Sí se declara el uso de ChatGPT en la **revisión y normalización 2B** de dichos artefactos.
6. F3-02/A7 queda cerrado como uso de IA de apoyo técnico con confirmación humana sobre las codificaciones reales.
7. No quedan marcadores `POR CONFIRMAR`, `Requiere nombre del verificador` ni `Requiere confirmación humana` en esta versión.
8. No se declara ninguna herramienta adicional de IA sin evidencia de uso real.

**Esta consolidación no autoriza a inventar hechos históricos ni a sustituir evidencia primaria. Si antes del commit definitivo el equipo identifica un uso real de otra herramienta de IA que no figure aquí, debe añadirse de forma transparente.**

---

## 7. Declaración de responsabilidad

Las herramientas de IA utilizadas en FabroGym funcionaron como apoyo. La autoría, responsabilidad académica, selección de evidencia, decisiones metodológicas, revisión final, integración al repositorio y defensa corresponden al equipo humano.

La versión final de este documento refleja los usos documentados y conserva una distinción explícita entre **apoyo de IA** y **evidencia/decisión humana**.
