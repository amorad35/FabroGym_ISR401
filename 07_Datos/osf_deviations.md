# Registro de desviaciones reales del protocolo — FabroGym

## 1. Propósito

Este archivo registra únicamente diferencias reales y verificables entre el procedimiento efectivamente seguido por FabroGym y el protocolo/prerregistro OSF v1.4.

No se modifican retrospectivamente fechas, respuestas, instrumentos, evidencias ni resultados para hacerlos coincidir con el protocolo. Las condiciones metodológicas que son limitaciones, pero no cambios del procedimiento previsto, se separan explícitamente de las desviaciones.

**Registro OSF:** `https://osf.io/62ysc/`  
**DOI OSF:** `10.17605/OSF.IO/62YSC`  
**Protocolo:** v1.4  
**Fecha de publicación del registro:** 29/08/2026

---

## 2. Registro resumido

| ID | Fecha/periodo | Desviación real | Motivo | Impacto | Tratamiento | Estado |
|---|---|---|---|---|---|---|
| DEV-OSF-01 | 12/08/2026–29/08/2026 | Las seis sesiones WALK ocurrieron antes de la publicación del prerregistro OSF. | El prerregistro se formalizó después de ejecutar las sesiones. | Los WALK no pueden presentarse como datos confirmatorios recogidos bajo un protocolo previamente registrado. | Se conserva la cronología real y los WALK se tratan como evidencia previa/formativa; el análisis posterior se declara como posterior al registro. | DOCUMENTADA |
| DEV-AN-02 | 05/09/2026 | Se añadió al cierre 2B una verificación de acuerdo intercodificador mediante doble codificación sobre un subconjunto superior al 20 %, con Cohen's kappa e IC95 %. | La guía terminal exige doble codificación y medida de acuerdo con intervalo de confianza; el procedimiento no formaba parte del análisis preregistrado v1.4. | El resultado debe interpretarse como análisis adicional de cierre y no como prueba preregistrada. | Se conservan el subconjunto, las dos hojas de codificación, el script y los resultados del acuerdo; no se reescribe el protocolo histórico. | DOCUMENTADA |
| DEV-AN-03 | 05/09/2026 | Se añadió tamaño del efecto + IC95 % para la comparación técnico vs no técnico. | La guía terminal específica lo exige, mientras que el pipeline previo trataba la comparación por perfiles como descriptiva/cualitativa y no aplicaba una prueba inferencial por participante. | El análisis adicional no debe presentarse como hipótesis confirmatoria preregistrada ni como inferencia poblacional. | Se usa una medida descriptivo-exploratoria por categorías, generada por script, con IC95 % bootstrap y sin p-valor por participante. | DOCUMENTADA |

---

# 3. DEV-OSF-01 — Walkthroughs anteriores al prerregistro

## Condición esperada

Una actividad que se presente como confirmatoria bajo un prerregistro debe ejecutarse después del sello temporal del registro correspondiente.

## Situación real

Las sesiones `WALK-TEC-01..03` y `WALK-NTEC-01..03` se realizaron entre el 12 y el 22 de agosto de 2026. El registro OSF se publicó el 29 de agosto de 2026.

## Impacto y tratamiento

Las sesiones conservan valor como evidencia empírica previa/formativa, pero no se presentan como recolección confirmatoria posterior al prerregistro. Se mantiene la secuencia real:

**WALK → protocolo v1.4 → registro OSF → sistematización/análisis posterior.**

## Evidencia

- `02_Evidencias/Validacion_walkthrough/`
- `06_Experimento/datos_crudos/sesiones_multimedia_desde_ficha_v3_1.csv`
- `06_Experimento/protocolo.tex`
- `06_Experimento/osf_registration.pdf`
- DOI `10.17605/OSF.IO/62YSC`

---

# 4. DEV-AN-02 — Doble codificación y acuerdo intercodificador añadidos en cierre 2B

## Condición previa

El pipeline previo no trataba una medida de acuerdo intercodificador como análisis preregistrado aplicable.

## Situación real

Durante el cierre terminal 2B se incorporó una comprobación adicional sobre un subconjunto común superior al 20 % del corpus WALK, con dos hojas de codificación y cálculo reproducible de Cohen's kappa con IC95 %.

## Motivo

La guía específica de cierre exige doble codificación de al menos el 20 % y una medida de acuerdo acompañada de intervalo de confianza.

## Impacto y tratamiento

El resultado se informa como **análisis adicional de cierre**, no como análisis confirmatorio preregistrado. No se modifica la versión histórica del protocolo para simular que el procedimiento estaba previsto desde el inicio.

## Evidencia terminal

La evidencia correspondiente se conserva en el bloque de doble codificación preparado para `10_Autoria/doble_codificacion/`, incluyendo las dos hojas, el subconjunto común, el script de kappa y sus resultados.

---

# 5. DEV-AN-03 — Tamaño del efecto técnico vs no técnico añadido en cierre 2B

## Condición previa

Antes del cierre terminal, la comparación entre los tres WALK técnicos y los tres no técnicos se trataba como descriptiva/cualitativa y no se aplicaba una prueba inferencial por participante.

## Situación real

En F3-04 se añadió una medida de tamaño del efecto con IC95 % sobre las categorías temáticas comparables entre perfiles.

## Motivo

La guía específica de cierre exige reportar tamaño del efecto e intervalo de confianza para la comparación técnico vs no técnico.

## Impacto y tratamiento

Se incorpora como análisis **descriptivo-exploratorio**, no como prueba confirmatoria preregistrada. La unidad del cálculo es la categoría temática pareada y no una puntuación independiente por participante. No se genera un p-valor ni se afirma una diferencia poblacional.

## Evidencia terminal

- `06_Experimento/scripts_analisis/calcular_efecto_perfiles.py`
- `06_Experimento/resultados/F3-04_TAMANIO_EFECTO.md`
- `06_Experimento/resultados/tablas/tabla_efecto_perfiles.csv`
- espejo reproducible correspondiente en `07_Datos/`

---

# 6. Condiciones metodológicas registradas que NO se clasifican como nuevas desviaciones

Estas condiciones deben seguir reportándose por transparencia, pero no se presentan como cambios posteriores del protocolo salvo que exista evidencia específica de ello:

- **Normalización de identificadores WALK:** es una corrección de nomenclatura y trazabilidad, no una nueva recolección ni un nuevo análisis.
- **Cuestionario:** el conjunto analítico oficial permanece en `n=70`; no contiene perfil técnico/no técnico ni una escala de explicabilidad por dimensión, por lo que se analiza únicamente dentro del alcance real de sus variables.
- **Saturación:** si el criterio estricto no se alcanza, se reporta como resultado/limitación y no se transforma en una desviación.
- **Member checking sin grabación audiovisual:** la ausencia de grabación se declara como limitación documental; no se fabrica evidencia.
- **Normalización terminal RF/RNF/RD:** es una corrección de especificación y trazabilidad, no una modificación retrospectiva de la evidencia primaria.
- **Corte y proveniencia del cuestionario:** la muestra analítica permanece congelada en el corte documentado; esto se trata como procedencia del conjunto analítico, no como una desviación adicional mientras no contradiga una regla explícita del protocolo.

---

# 7. Regla para futuras actualizaciones

Solo se añadirá una nueva entrada cuando exista:

1. una condición prevista explícitamente por el protocolo;
2. una diferencia real frente a esa condición;
3. una fecha o periodo verificable;
4. un motivo sustentable;
5. evidencia del impacto y del tratamiento aplicado.

Las actividades pendientes no se registran como si ya hubieran ocurrido. Las entradas históricas no se eliminan para hacer coincidir retrospectivamente el protocolo con el estado final.
