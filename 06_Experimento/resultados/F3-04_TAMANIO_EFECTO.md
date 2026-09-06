# F3-04 — Tamaño del efecto técnico vs no técnico

## Fuente de datos

`datos_crudos/comparacion_perfiles_walkthroughs_fuente.csv`

La fuente resume las 18 categorías temáticas identificadas en los seis walkthroughs:
tres sesiones técnicas y tres no técnicas.

## Método

La misma categoría se compara entre ambos perfiles, por lo que las 18 categorías se tratan como pares.
Se utiliza la **correlación biserial por rangos pareada (`r_rb`)** como tamaño del efecto.

El intervalo de confianza del 95 % se obtiene mediante **bootstrap percentil de 10000 réplicas**
con semilla reproducible `4012026`.

## Resultados

- Presencia de categorías por sesiones:
  `r_rb = 0.637363`, IC95% `[0.100000, 1.000000]`.
- Fragmentos codificados por categoría:
  `r_rb = 0.716667`, IC95% `[0.286765, 1.000000]`.

Un valor positivo indica una tendencia a mayor presencia o conteo en el perfil técnico.

## Alcance y limitación

Este resultado es **descriptivo-exploratorio**. Solo existen tres walkthroughs por perfil.
La unidad de este cálculo es la categoría temática pareada; no es una puntuación independiente por participante.
Por ello no se genera p-valor ni se afirma una diferencia poblacional.

## Reproducibilidad

Desde la raíz de `06_Experimento/`:

```bash
python scripts_analisis/calcular_efecto_perfiles.py
```

Desde la raíz de `07_Datos/`:

```bash
python scripts/calcular_efecto_perfiles.py
```

Los resultados se generan automáticamente en `resultados/tablas/`.
