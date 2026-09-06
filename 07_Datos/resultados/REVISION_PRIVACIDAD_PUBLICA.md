# Revisión automática de privacidad — F3-07

- Archivos del árbol público inspeccionados por nombre/extensión: **845**.
- CSV de `07_Datos/datos_crudos` y `datos_procesados` inspeccionados: **20**.
- Hallazgos automáticos: **2**.
- PDFs censurados/actas que requieren revisión visual adicional: **22**.

## Hallazgos

- **ARCHIVO_MULTIMEDIA** — `05_MVP/video_demo.mp4` — archivo audiovisual presente en el árbol público
- **COLUMNA_IDENTIFICABLE** — `07_Datos/datos_crudos/encuesta_clientes_anonimizada.csv` — columna=Escriba un comentario opcional sobre su experiencia en el gimnasio. No incluya nombres ni datos de salud.  ; valores_no_vacios=42

## Revisión manual obligatoria

Este resultado no inspecciona visualmente el contenido de PDFs, imágenes o fotografías. Las copias censuradas, actas enmascaradas y fotografías F3-01 deben revisarse antes del release.

La confirmación del cifrado y acceso de la capa restringida se realiza fuera de GitHub.
