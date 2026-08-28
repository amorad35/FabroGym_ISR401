# Scripts de análisis - FabroGym

Esta carpeta contiene scripts reproducibles alineados con el **protocolo v1.2** del Enfoque 3: Explicabilidad como Requisito No Funcional (RNF).

## Alcance

Los scripts trabajan sobre matrices estructuradas derivadas de la evidencia real disponible. No requieren ni generan respuestas Likert inexistentes y no suponen rondas adicionales de walkthrough.

## Archivos

- `validar_entradas.py`: valida estructura mínima, perfiles permitidos y campos obligatorios.
- `analizar_walkthroughs.py`: resume unidades codificadas por perfil, necesidad y dimensión cuando corresponda.
- `analizar_rnf.py`: resume candidatos a RNF y calcula cobertura únicamente cuando la información necesaria está disponible.
- `analizar_member_checking.py`: resume decisiones Confirmado / Ajustado / No confirmado si existe una matriz real de member checking.
- `run_all.py`: ejecuta los análisis disponibles sin exigir archivos opcionales inexistentes.
- `requirements.txt`: indica la versión mínima de Python; no se requieren librerías externas.

## Entradas principales

```text
06_Experimento/instrumentos/02_Matriz_Codificacion_Walkthroughs.csv
06_Experimento/instrumentos/03_Matriz_Candidatos_RNF_Explicabilidad.csv
```

El member checking puede incorporarse opcionalmente mediante un CSV estructurado con las columnas:

```text
ID,Resultado,Observaciones
```

Ese archivo se crea únicamente después de ejecutar la actividad y transcribir de manera fiel las decisiones del acta.

## Tratamiento analítico

Los scripts pueden generar:

- número de unidades codificadas por perfil;
- conteos de necesidades o categorías;
- distribución descriptiva por dimensión cuando exista una codificación válida;
- número de candidatos RNF por perfil y dimensión;
- cobertura descriptiva de dimensiones cuando sea calculable;
- resumen de decisiones de member checking cuando exista evidencia.

No se calcula U de Mann-Whitney, tamaño del efecto, IC95 % o kappa entre rondas, porque el protocolo v1.2 no presupone los datos necesarios para esos análisis.

## Resultados

Las salidas se guardan en:

```text
06_Experimento/resultados/
```

Los scripts no incorporan resultados predefinidos ni completan datos faltantes por inferencia.
