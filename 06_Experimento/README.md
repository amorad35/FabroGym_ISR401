# 06_Experimento — FabroGym

Esta carpeta conserva el **protocolo, prerregistro, instrumentos y procedencia histórica** del componente empírico de FabroGym — Enfoque 3: Explicabilidad como Requisito No Funcional (RNF).

> ## Estado para el cierre 2B
>
> `06_Experimento/` **NO es el paquete canónico ejecutable de análisis de la Entrega Final**.
>
> El único paquete canónico de datos y análisis para B1 es:
>
> ```text
> 07_Datos/
> ```
>
> y su ejecución oficial, desde la raíz de `07_Datos/`, es:
>
> ```bash
> python -m pip install -r scripts/requirements.txt
> python scripts/run_all.py
> ```
>
> Los datos, scripts y resultados que permanecen en `06_Experimento/` se conservan únicamente para documentar la **procedencia, cronología y evolución metodológica** del estudio. No constituyen una segunda cadena canónica.

## Estado empírico

La evidencia disponible está constituida por seis walkthroughs reales: tres con participantes técnicos y tres con participantes no técnicos. Las sesiones fueron realizadas antes del registro OSF y se tratan como evidencia previa/formativa, no como datos confirmatorios preregistrados.

El prerregistro cualitativo fue publicado en OSF Registries el 29 de agosto de 2026:

- **OSF:** https://osf.io/62ysc/
- **DOI:** https://doi.org/10.17605/OSF.IO/62YSC
- **Tipo de registro:** Qualitative Preregistration
- **Commit congelado pre-OSF:** `d2886d7453185daca62427c75729773b3510d1bb`

No se presupone que las seis sesiones hayan evaluado una misma explicación estructurada ni que en todas se haya presentado un componente específico de recomendación de rutinas.

## Protocolo

El protocolo documentado se conserva en:

```text
06_Experimento/protocolo.tex
06_Experimento/protocolo.pdf
```

La carpeta mantiene la evidencia metodológica necesaria para reconstruir cómo se diseñó y evolucionó el estudio.

## Instrumentos y matrices históricas/de procedencia

```text
06_Experimento/instrumentos/
├── 01_Guia_Walkthrough_Explicabilidad.pdf
├── 03_Matriz_Candidatos_RNF_Explicabilidad.csv
├── 04_Ficha_Caracterizacion_Participante.pdf
├── 05_Matriz_Operacionalizacion_Explicabilidad.csv
└── 06_Acta_Member_Checking.pdf
```

La codificación temática de procedencia se conserva en:

```text
06_Experimento/datos_crudos/codificacion_walkthroughs.csv
```

Estos artefactos documentan el origen de los insumos posteriormente consolidados en `07_Datos/datos_crudos/`.

## Scripts históricos de procedencia

La carpeta:

```text
06_Experimento/scripts_analisis/
```

se conserva para trazabilidad histórica y para demostrar la evolución de la cadena analítica. **No debe presentarse ni utilizarse como el orquestador oficial de B1.**

Para reproducir la Entrega Final debe utilizarse únicamente:

```bash
cd 07_Datos
python -m pip install -r scripts/requirements.txt
python scripts/run_all.py
```

No se eliminan los scripts históricos porque forman parte de la procedencia del estudio; su conservación no crea un segundo paquete canónico.

## Resultados históricos

Los archivos existentes en:

```text
06_Experimento/resultados/
```

documentan estados previos/intermedios del análisis. Los resultados canónicos regenerables de la Entrega Final están en:

```text
07_Datos/resultados/
```

## Prerregistro OSF

El comprobante documental se conserva como:

```text
06_Experimento/osf_registration.pdf
```

El registro declara la cronología real de los walkthroughs y evita presentarlos retroactivamente como evidencia confirmatoria posterior al OSF.

## Privacidad

Los artefactos metodológicos de esta carpeta no sustituyen la separación pública/restringida definida para el cierre. La política final de privacidad y custodia se documenta en `08_Etica/`.

## Regla de cierre

Para B1:

```text
CANÓNICO Y EJECUTABLE: 07_Datos/
HISTÓRICO / PROCEDENCIA: 06_Experimento/
PUBLICACIÓN / DEPÓSITO HISTÓRICO: 07_Publicacion/
```

Esta distinción elimina la ambigüedad entre cadenas de análisis sin borrar evidencia histórica válida.
