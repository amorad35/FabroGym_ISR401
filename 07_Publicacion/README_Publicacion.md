# 07_Publicacion — FabroGym

## Propósito

Esta carpeta conserva el manuscrito y artefactos de publicación/replicación asociados al proyecto FabroGym. El registro Zenodo publicado se mantiene como evidencia histórica externa.

> **Importante para B1:** `07_Publicacion/` **no es el paquete canónico de datos y análisis de la Entrega Final**. La única cadena canónica y evaluable es `07_Datos/`.

## Contenido

- manuscrito y fuentes de publicación;
- artefactos de metadatos;
- copia local normalizada del paquete asociado al depósito Zenodo;
- documentación de reproducibilidad histórica.

## Ejecución canónica para la Entrega Final

Desde la raíz del repositorio:

```bash
cd 07_Datos
python -m pip install -r scripts/requirements.txt
python scripts/run_all.py
```

## Relación con el paquete local de publicación

`dataset_zenodo/` conserva una copia local de trabajo vinculada al depósito publicado y puede contener scripts internos de replicación histórica. Esos scripts **no sustituyen ni compiten con `07_Datos/scripts/run_all.py` como orquestador oficial de B1**.

## ERS/SRS

La única ERS/SRS académica vigente está en:

```text
01_ERS/ERS_SRS_2B_v2.0.pdf
01_ERS/ERS_SRS_2B_v2.0.tex
```

`dataset_zenodo/srs/README.md` la referencia sin duplicarla.

## Repositorio

https://github.com/amorad35/FabroGym_ISR401

## Licencia

Los datos y documentación pública anonimizada se documentan bajo CC BY 4.0. La evidencia restringida se rige por las reglas de custodia/cifrado del expediente ético.

## Estado de Zenodo

El depósito publicado es la versión 2.0.0 con DOI específico:

https://doi.org/10.5281/zenodo.22237884

No se modifica retrospectivamente. Cualquier corrección futura deberá publicarse como una nueva versión.
