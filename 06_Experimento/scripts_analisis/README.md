# Scripts de análisis

## Salvaguarda de prerregistro

`run_all.py` bloquea la ejecución mientras exista `PENDIENTE_osf_registration.md` o falte `osf_registration.pdf`. Esto evita generar resultados reales antes del prerregistro.

## Flujo

1. `validar_entradas.py`: comprueba 25 RF, cobertura completa, evaluadores y dominios de valores.
2. `detector_ambiguedad.py`: clasifica posibles smells mediante reglas transparentes.
3. `preparar_consenso.py`: calcula mayoría experta y marca empates para adjudicación.
4. `analizar_resultados.py`: métricas, kappa, McNemar, desacuerdos y figuras.
5. `run_all.py`: orquesta el flujo real.
6. `prueba_sintetica.py`: verifica el entorno con datos ficticios, sin tocar el corpus real.
7. `generar_matrices_evaluacion.py`: regenera órdenes aleatorizados con semilla declarada.

## Entrada real esperada después de OSF

Copie la matriz completada como `resultados/evaluaciones_expertos.csv`. Debe conservar las columnas de `instrumentos/03_Matriz_Evaluacion_Expertos.csv`.

## Salidas

CSV de métricas, acuerdo y desacuerdos; figuras PNG y SVG.
