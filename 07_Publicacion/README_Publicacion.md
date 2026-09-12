# 07_Publicacion - FabroGym

## Propósito

Esta carpeta conserva el manuscrito y el paquete local de replicación utilizado para la Entrega 4 (2B) de Ingeniería de Requerimientos (ISR-401). El registro Zenodo publicado se mantiene como evidencia histórica externa; la copia local de entrega puede incorporar normalizaciones exigidas por la rúbrica y no se declara byte a byte idéntica al depósito remoto.

## Contenido

- `manuscrito_borrador.pdf`: versión 1.0 del artículo paralelo.
- `manuscrito_fuente/`: fuente LaTeX, bibliografía y figuras.
- `analisis_revistas.md`: comparación de seis revistas candidatas.
- `dataset_zenodo/`: copia local de trabajo del paquete de replicación asociado al Zenodo 2.0.0; para A5 referencia la ERS/SRS canónica de `01_ERS/` y no incorpora una segunda copia del documento.

## Estado de la evidencia

El paquete utiliza exclusivamente evidencia pública anonimizada:

- 10 entrevistas anonimizadas;
- 76 fragmentos de walkthrough codificados;
- 37 códigos normalizados y 18 categorías temáticas;
- **70 respuestas de cuestionario anonimizadas**, correspondientes al corte analítico vigente e incluidas las 4 respuestas de pilotaje;
- 25 requisitos funcionales, 23 no funcionales y 4 restricciones de diseño;
- matriz terminal con 105 trazas identificadas.

No se incluyen consentimientos originales, firmas, cédulas, audios, videos, rostros, voces, datos clínicos, biometría, peso, medidas corporales ni archivos que permitan reidentificar participantes.

## Limitaciones declaradas

- La curva de códigos es descriptiva y no demuestra saturación teórica.
- La muestra analítica del cuestionario es no probabilística, contiene 70 respuestas y conserva las cuatro respuestas de pilotaje.
- El registro OSF y el depósito Zenodo ya están publicados. La cobertura funcional del MVP sigue sujeta a verificación terminal C3; no se presenta como prueba ejecutada.
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

Los datos y la documentación pública anonimizada se documentan bajo CC BY 4.0. La licencia no cubre la zona restringida del proyecto.

## Estado de Zenodo

El depósito publicado es la versión 2.0.0 con DOI específico https://doi.org/10.5281/zenodo.22237884 y no se modifica retrospectivamente. Para la entrega académica vigente, `dataset_zenodo/` funciona como copia local normalizada: la única ERS/SRS vigente permanece en `01_ERS/ERS_SRS_2B_v2.0.*`, mientras `dataset_zenodo/srs/README.md` la referencia sin duplicarla. Una futura versión correctiva de Zenodo deberá publicarse como versión nueva y volver a validar manifiesto, checksums, privacidad y reproducibilidad.
