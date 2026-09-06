# Resultados - FabroGym

Esta carpeta almacenará únicamente productos derivados de la evidencia real y verificable del **Enfoque 3: Explicabilidad como Requisito No Funcional (RNF)**.

## Base empírica

La evidencia principal corresponde a seis walkthroughs ya realizados antes del registro OSF: 3 técnicos y 3 no técnicos. Su tratamiento es previo/formativo. El análisis reproducible se centra en la sistematización de necesidades de explicabilidad, candidatos a RNF, contraste descriptivo entre perfiles y member checking si esta actividad se ejecuta.

## Estado actual

No se incorporan resultados inventados ni archivos llenados con valores hipotéticos.

La existencia de cada salida depende de que exista información real suficiente para generarla.

## Salidas generables por los scripts

Con datos válidos en la matriz de codificación, `analizar_walkthroughs.py` puede generar:

```text
codificacion_walkthroughs_procesada.csv
resumen_necesidades.csv
resumen_necesidades_por_perfil.csv
resumen_dimensiones.csv
resumen_perfil_dimension.csv
```

Con candidatos RNF válidos, `analizar_rnf.py` puede generar:

```text
resumen_candidatos_rnf.csv
candidatos_por_perfil.csv
candidatos_por_dimension.csv
cobertura_dimensiones.csv
```

`cobertura_dimensiones.csv` registra una proporción únicamente cuando se proporciona un denominador verificable. Si ese denominador no está establecido, la cobertura se mantiene como descripción y la proporción se reporta como no calculable.

Si se ejecuta el member checking y existe una matriz estructurada de decisiones reales, `analizar_member_checking.py` puede generar:

```text
resumen_member_checking.csv
```

## Análisis que no se asumen

Esta carpeta no presupone respuestas Likert, U de Mann-Whitney, tamaños del efecto, intervalos de confianza ni kappa entre rondas.

Si un análisis no puede calcularse con la evidencia disponible, se reporta como **no aplicable** o **no calculable**, según corresponda.

## Trazabilidad

Cada salida debe poder relacionarse con:

- la evidencia anonimizada o seudonimizada de origen;
- `06_Experimento/datos_crudos/codificacion_walkthroughs.csv`;
- `06_Experimento/instrumentos/03_Matriz_Candidatos_RNF_Explicabilidad.csv`;
- `06_Experimento/instrumentos/05_Matriz_Operacionalizacion_Explicabilidad.csv`;
- los scripts versionados de `06_Experimento/scripts_analisis/`;
- el commit del repositorio utilizado para ejecutar el análisis.

## Privacidad

Los resultados públicos no deben contener nombres, firmas, cédulas, teléfonos, correos personales, audios, videos ni otros identificadores directos.
