# Resultados - FabroGym

Esta carpeta almacenará únicamente productos derivados de la evidencia real y verificable del **Enfoque 3: Explicabilidad como Requisito No Funcional (RNF)**.

## Base empírica

La evidencia principal corresponde a seis walkthroughs ya realizados antes del registro OSF: 3 técnicos y 3 no técnicos. Su tratamiento es previo/formativo. El análisis reproducible se centra en la sistematización de necesidades de explicabilidad, candidatos a RNF, contraste descriptivo entre perfiles y member checking si esta actividad se ejecuta.

## Estado actual

No se incorporan resultados inventados ni archivos llenados con valores hipotéticos.

La existencia de cada salida depende de que exista información real suficiente para generarla.

## Estructura prevista

```text
06_Experimento/resultados/
├── README.md
├── codificacion_walkthroughs_procesada.csv
├── resumen_necesidades_por_perfil.csv
├── resumen_dimensiones.csv
├── resumen_candidatos_rnf.csv
├── cobertura_dimensiones.csv
└── resumen_member_checking.csv
```

`cobertura_dimensiones.csv` se genera únicamente cuando la matriz de codificación permita establecer de forma trazable qué dimensiones fueron evaluadas y cuál es el denominador válido.

`resumen_member_checking.csv` se genera únicamente si la actividad se ejecuta y existe una matriz estructurada de decisiones reales.

## Análisis que no se asumen

Esta carpeta no presupone respuestas Likert, U de Mann-Whitney, tamaños del efecto, intervalos de confianza ni kappa entre rondas.

Si un análisis no puede calcularse con la evidencia disponible, se reporta como **no aplicable** o **no calculable**, según corresponda.

## Trazabilidad

Cada salida debe poder relacionarse con:

- la evidencia anonimizada o seudonimizada de origen;
- `02_Matriz_Codificacion_Walkthroughs.csv`;
- `03_Matriz_Candidatos_RNF_Explicabilidad.csv`;
- `05_Matriz_Operacionalizacion_Explicabilidad.csv`;
- los scripts versionados de `06_Experimento/scripts_analisis/`;
- el commit del repositorio utilizado para ejecutar el análisis.

## Privacidad

Los resultados públicos no deben contener nombres, firmas, cédulas, teléfonos, correos personales, audios, videos ni otros identificadores directos.
