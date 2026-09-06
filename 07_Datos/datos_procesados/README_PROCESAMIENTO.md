# Datos procesados — trazabilidad de transformaciones

## Regla

Los archivos de esta carpeta son **salidas del pipeline**. No deben editarse a mano para cambiar cifras, estados o resultados.

La entrada se toma desde `datos_crudos/`. La ejecución reproducible se realiza desde la raíz de este paquete:

```bash
python scripts/run_all.py
```

Algunas salidas pueden conservar los mismos valores que su archivo fuente. Eso no las convierte en datos crudos: son copias canónicas escritas por el script para mantener una separación explícita entre insumos y productos del análisis.

## Mapa fuente → transformación → salida

| Salida en `datos_procesados/` | Fuente en `datos_crudos/` | Transformación reproducible | Script |
|---|---|---|---|
| `RNF_explicabilidad_final.csv` | `candidatos_RNF_explicabilidad_member_checked.csv` | Normaliza el ID terminal, conserva el ID candidato y añade los estados del requisito/componente/MVP. | `scripts/run_all.py` |
| `codificacion_walkthroughs.csv` | `codificacion_walkthroughs.csv` | Salida canónica escrita por el script a partir de la matriz fuente; no añade decisiones de codificación. | `scripts/run_all.py` |
| `comparacion_perfiles_walkthroughs.csv` | `comparacion_perfiles_walkthroughs_fuente.csv` | Copia canónica escrita por el script para consumo de resultados y tablas. | `scripts/run_all.py` |
| `curva_estabilizacion_categorias_axiales.csv` | `estabilizacion_categorias_axiales_fuente.csv` | Añade el acumulado de categorías axiales por orden de sesión. | `scripts/run_all.py` |
| `curva_saturacion_codigos_walkthroughs.csv` | `curva_codigos_nuevos_walkthroughs_fuente.csv` | Añade códigos acumulados y porcentaje de códigos nuevos respecto del total final. | `scripts/run_all.py` |
| `encuesta_clientes_limpia.csv` | `encuesta_clientes_anonimizada.csv` | Normaliza las cabeceras por posición para el análisis; no crea respuestas nuevas. | `scripts/run_all.py` |
| `fragmentos_explicabilidad_desde_codificacion.csv` | `codificacion_walkthroughs.csv` | Filtra los registros cuya marca Aplicable_Explicabilidad es Sí/Si. | `scripts/run_all.py` |
| `fragmentos_pertinentes_explicabilidad.csv` | `fragmentos_pertinentes_explicabilidad.csv` | Salida canónica escrita por el script desde el subconjunto fuente congelado. | `scripts/run_all.py` |
| `member_checking.csv` | `member_checking_estructurado.csv` | Salida canónica escrita por el script desde la matriz estructurada de member checking. | `scripts/run_all.py` |
| `sesiones_multimedia_verificadas.csv` | `sesiones_multimedia_desde_ficha_v3_1.csv` | Añade duración en segundos y validación de formato SHA-256 para audio y video. | `scripts/run_all.py` |

## Resultados adicionales

Las tablas, figuras, resúmenes, intervalos de confianza y demás productos analíticos se escriben en `resultados/`. No se almacenan como datos crudos.

Los análisis añadidos durante el cierre terminal, como kappa/IC95% y tamaño del efecto técnico vs no técnico, deben conservar su script y sus resultados sin modificar manualmente las cifras producidas.
