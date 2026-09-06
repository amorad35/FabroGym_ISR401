# ERS/SRS FabroGym - Entrega 4 (2B)

Versión terminal vigente: **ERS_SRS_2B_v2.0**.

La versión académica vigente es 2.0. Las etiquetas internas 2.1 y 2.2 son revisiones históricas no vigentes. Esta versión integra los 54 diagramas UML definitivos del equipo.

Archivos principales:
- `ERS_SRS_2B_v2.0.pdf`
- `ERS_SRS_2B_v2.0.tex`
- `referencias.bib` (bibliografía versionada del entregable)
- `figuras_2B/` (figuras auxiliares utilizadas por el documento)
- `modelado_final/` (mirror controlado de 54 PNG para compilación y portabilidad)
- `../03_Modelado/Diagramas_UML/` (ubicación canónica del modelado UML)

## Canonicidad y sincronización UML

`03_Modelado/Diagramas_UML/` es la fuente canónica de las imágenes y fuentes
editables del modelado. `01_ERS/modelado_final/` es un mirror de compilación:
conserva las mismas 54 rutas PNG y debe permanecer byte a byte idéntico a la
fuente canónica. Toda actualización UML debe realizarse primero en
`03_Modelado/Diagramas_UML/` y después sincronizarse al mirror; no deben
mantenerse versiones divergentes.

Para compilar el handoff, extraiga el ZIP completo conservando `01_ERS/` y
`03_Modelado/` como directorios hermanos. Desde `01_ERS/`, ejecute tres veces:

```bash
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
```

No copie únicamente el archivo `.tex`: la compilación requiere también
`figuras_2B/` y al menos uno de los dos árboles UML sincronizados. El handoff
incluye ambos para permitir la verificación de su igualdad.

Zenodo publicado, versión 2.0.0; DOI específico: `10.5281/zenodo.22237884`.
