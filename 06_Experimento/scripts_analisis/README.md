# 06_Experimento/scripts_analisis — scripts históricos de procedencia

## Estado para la Entrega Final 2B

Esta carpeta **no es la cadena canónica de ejecución de B1**.

Los scripts aquí conservados documentan una etapa previa del desarrollo del componente empírico y se mantienen por trazabilidad, procedencia y regla de no-retroceso.

El único paquete canónico ejecutable del cierre está en:

```text
07_Datos/
```

Ejecución oficial:

```bash
cd 07_Datos
python -m pip install -r scripts/requirements.txt
python scripts/run_all.py
```

## Contenido histórico

Esta carpeta conserva, entre otros:

- `validar_entradas.py`
- `analizar_walkthroughs.py`
- `analizar_rnf.py`
- `analizar_member_checking.py`
- `run_all.py`
- `requirements.txt`

Estos archivos permiten auditar la evolución del análisis, pero **`06_Experimento/scripts_analisis/run_all.py` no debe citarse como el orquestador oficial de la Entrega Final**.

## Procedencia

Los scripts consolidados en `07_Datos/scripts/` proceden de esta línea de trabajo y fueron normalizados para integrar en un solo paquete:

- datos crudos;
- datos procesados;
- scripts;
- resultados;
- diccionario de datos;
- licencia;
- checksums;
- desviaciones;
- registro de depósito.

## Regla de interpretación

La presencia física de estos scripts históricos no implica dos paquetes vigentes:

```text
06_Experimento/scripts_analisis/  -> histórico / procedencia
07_Datos/scripts/                 -> canónico / evaluable / ejecutable
```
