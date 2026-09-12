# Revisión automática de privacidad — F3-07 / B6

**Estado automático:** **NO APTO PARA CIERRE AUTOMÁTICO**.

## Alcance de la auditoría

- Archivos del árbol público inspeccionados por nombre/extensión: **1008**.
- CSV inspeccionados en `07_Datos/datos_crudos` y `datos_procesados`: **20**.
- CSV no legibles durante el análisis: **0**.
- Hallazgos automáticos bloqueantes: **6**.
- Advertencias/documentación pendiente: **2**.
- Archivos comprimidos detectados en el árbol: **2**.

## Hallazgos automáticos que deben corregirse

- **ARCHIVO_COMPRIMIDO_RESTRINGIDO** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — archivo comprimido con nombre/ruta compatible con material restringido; su contenido no se abrió automáticamente
- **ARCHIVO_COMPRIMIDO_RESTRINGIDO** — `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` — archivo comprimido con nombre/ruta compatible con material restringido; su contenido no se abrió automáticamente
- **LFS_RESTRINGIDO_PUBLICADO** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — puntero Git LFS hacia material restringido (size=1521924213 bytes; sha256:a1b9b56a4fddf469a39bab3a51bcc891c85c0d0ce70432bf8602513f84c24070)
- **ORIGINAL_CUESTIONARIO_PUBLICO** — `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` — nombre compatible con fotografías originales del cuestionario
- **RUTA_RESTRINGIDA_PUBLICA** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — ruta declarada como restringida presente dentro del árbol público
- **RUTA_RESTRINGIDA_PUBLICA** — `02_Evidencias/00_Restringido/fichas_tecnicas.csv` — ruta declarada como restringida presente dentro del árbol público

## Advertencias y verificaciones manuales pendientes

- **A6_PRIVACIDAD_MANUAL_PENDIENTE** — `10_Autoria/exif_inventario.csv` — 5 registros F3-01 mantienen un estado de privacidad que exige revisión/confirmación manual; esto no invalida el EXIF técnico, pero sí debe cerrarse en F3-07/B6
- **GITIGNORE_SIN_REGLAS_PRIVACIDAD** — `.gitignore` — faltan marcadores/reglas preventivas para: 00_Restringido, PENDIENTE_PRIVACIDAD_NO_SUBIR_A_GIT, Fotos_Originales_Cuestionario

## Verificación técnica A6 — fotografías del cuestionario y EXIF

- Registros `F3-01_APLICACION_CUESTIONARIO` en `10_Autoria/exif_inventario.csv`: **5**.
- Registros con fecha EXIF, fuente EXIF, dispositivo, `Estado_EXIF=OK` y SHA-256 válido: **5**.
- Copias fotográficas presentes en `02_Evidencias/Cuestionario/Fotos_Aplicacion/`: **5**.
- **Resultado técnico A6:** **CUMPLE** el mínimo documental de cinco registros con metadatos EXIF válidos.

> La comprobación técnica A6 no equivale a autorización de publicación. La clasificación [P]/[R] y el consentimiento de fotografías identificables pertenecen al cierre manual de F3-07/B6.

## Multimedia pública clasificada

- `05_MVP/video_demo.mp4` — Video demostrativo del MVP.
- `09_Defensa/video_defensa.mp4` — Grabación de la defensa final.
- `10_Autoria/grabaciones/Vd_01.mp4` — Grabación de sesión de trabajo del equipo para evidencia de autoría.
- `10_Autoria/grabaciones/Vd_02.mp4` — Grabación de sesión de trabajo del equipo para evidencia de autoría.

## Revisión visual/manual requerida

- Consentimientos censurados: **16**.
- Actas de walkthrough: **6**.
- Fotografías públicas de aplicación del cuestionario: **5**.
- Fotografías públicas del equipo/autoria: **2**.
- Total de piezas que requieren o pueden requerir revisión visual según su naturaleza: **29**.

Este auditor no inspecciona visualmente el contenido de PDFs, imágenes o videos. Debe confirmarse manualmente que las copias censuradas/enmascaradas no revelen firmas, nombres, cédulas, teléfonos, correos, respuestas individuales u otros identificadores no autorizados.

La confirmación del cifrado, custodia y acceso de la capa restringida [R] se realiza fuera de GitHub y no puede ser demostrada por este script.

## Interpretación del código de salida

- `0`: no hay hallazgos automáticos bloqueantes; aún deben cerrarse las revisiones humanas aplicables.
- `2`: existe al menos un hallazgo automático que debe corregirse antes del release/tag final.
