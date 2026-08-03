# 07_Publicacion - FabroGym

## Propósito

Esta carpeta contiene el borrador de manuscrito y el paquete de datos abierto preparado para la Entrega 3 (2A) de Ingeniería de Requerimientos (ISR-401).

## Contenido

- `manuscrito_borrador.pdf`: versión 1.0 del artículo paralelo.
- `manuscrito_fuente/`: fuente LaTeX, bibliografía y figuras.
- `analisis_revistas.md`: comparación de seis revistas candidatas.
- `dataset_zenodo/`: conjunto de datos anonimizado y material reproducible.

## Estado de la evidencia

El paquete utiliza exclusivamente evidencia pública anonimizada:

- 10 entrevistas anonimizadas;
- 59 fragmentos codificados;
- 16 códigos temáticos y 2 memos/restricciones de diseño;
- 32 respuestas de cuestionario anonimizadas, incluidas 4 respuestas de pilotaje;
- 25 requisitos funcionales, 15 no funcionales y 4 restricciones;
- matriz de trazabilidad con 44 identificadores únicos.

No se incluyen consentimientos originales, firmas, cédulas, audios, videos, rostros, voces, datos clínicos, biometría, peso, medidas corporales ni archivos que permitan reidentificar participantes.

## Limitaciones declaradas

- La curva de códigos es descriptiva y no demuestra saturación teórica.
- La muestra del cuestionario es no probabilística y contiene cuatro respuestas de pilotaje.
- Las sesiones de walkthrough, la cobertura funcional del MVP, el registro OSF, el depósito Zenodo y el DOI permanecen pendientes; no se presentan como resultados ejecutados.
- Los textos completos de las transcripciones continúan en `02_Evidencias/Transcripciones/`. El JSON del paquete indexa sus rutas y contiene la totalidad de los fragmentos codificados para evitar versiones divergentes.

## Compilación del manuscrito

```bash
cd manuscrito_fuente
pdflatex manuscrito.tex
bibtex manuscrito
pdflatex manuscrito.tex
pdflatex manuscrito.tex
```

## Ejecución del análisis

```bash
cd dataset_zenodo
python scripts_analisis/run_all.py
```

## Repositorio

https://github.com/amorad35/FabroGym_ISR401

## Licencia

Los datos anonimizados se preparan para licencia CC BY 4.0. La licencia no cubre la zona restringida del proyecto.
