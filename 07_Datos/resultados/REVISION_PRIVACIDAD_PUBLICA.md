# Revisión automática de privacidad — F3-07 / B6

**Estado automático:** **SIN HALLAZGOS AUTOMÁTICOS BLOQUEANTES**.

## Criterio aplicado

- `07_Datos/` y los artefactos de publicación deben permanecer sin datos personales directos.
- La capa restringida cifrada se trata de forma separada.
- La presencia de un contenedor restringido expresamente documentado no constituye por sí sola un hallazgo bloqueante.
- El auditor no abre archivos cifrados ni conoce contraseñas; su cifrado/protección debe confirmarse manualmente.

## Alcance de la auditoría

- Archivos del árbol inspeccionados por nombre/extensión: **1008**.
- CSV inspeccionados en `07_Datos/datos_crudos` y `datos_procesados`: **20**.
- CSV no legibles durante el análisis: **0**.
- Hallazgos automáticos bloqueantes: **0**.
- Advertencias / comprobaciones humanas: **2**.

## Capa restringida documentada

- `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — **DOCUMENTADO** — contenedor de evidencia restringida previsto por FabroGym y versionado mediante Git LFS. Debe permanecer cifrado/protegido y la clave no debe almacenarse en el repositorio.
- `02_Evidencias/00_Restringido/fichas_tecnicas.csv` — **DOCUMENTADO** — inventario técnico de evidencia con códigos, duración, códec, tamaño y SHA-256.
- `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` — **DOCUMENTADO** — contenedor de fotografías originales A11 utilizado para preservar EXIF. Solo es admisible si está cifrado/protegido y su clave permanece fuera del repositorio.

## Resultado automático

No se detectaron hallazgos automáticos bloqueantes con las reglas aplicadas.

Los hallazgos del reporte anterior correspondientes a rutas/archivos de la capa restringida están documentados expresamente por la política F3-07/B6 y por el verificador actualizado. Su sola presencia no se interpreta como una exposición accidental de datos.

Las cinco fotografías públicas del cuestionario figuran actualmente en `10_Autoria/exif_inventario.csv` con estado de privacidad `PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`; por tanto, ya no corresponde mantener la advertencia histórica `VERIFICAR_CONSENTIMIENTO_ANTES_DE_PUBLICAR` como estado de esos cinco registros.

## Advertencias y verificaciones manuales pendientes

- **CONFIRMAR_CIFRADO_MANUAL** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — confirmar antes del tag final que el contenedor está cifrado/protegido y que la contraseña/clave no aparece en Git, README, commits ni artefactos públicos.
- **CONFIRMAR_CIFRADO_MANUAL** — `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` — confirmar antes del tag final que el contenedor está cifrado/protegido y que su clave permanece fuera del repositorio.

## Verificaciones informativas

- **LFS_RESTRINGIDO_ESPERADO** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — puntero Git LFS documentado de **1.521.924.213 bytes**, SHA-256 `a1b9b56a4fddf469a39bab3a51bcc891c85c0d0ce70432bf8602513f84c24070`.
- **A6_EXIF_OK** — `10_Autoria/exif_inventario.csv` — los **5** registros F3-01 documentan fecha EXIF, fuente EXIF, dispositivo y SHA-256 válidos.
- **A6_PRIVACIDAD_DOCUMENTADA** — los **5** registros F3-01 están clasificados como `PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`.
- **RESTRINGIDO_DOCUMENTADO** — los tres artefactos indicados en la sección de capa restringida están contemplados por la política actual del proyecto.

## Verificación técnica A6 — fotografías del cuestionario y EXIF

- Registros `F3-01_APLICACION_CUESTIONARIO` en `10_Autoria/exif_inventario.csv`: **5**.
- Registros con fecha EXIF, fuente EXIF, dispositivo, `Estado_EXIF=OK` y SHA-256 válido: **5**.
- Copias fotográficas presentes en `02_Evidencias/Cuestionario/Fotos_Aplicacion/`: **5**.
- Estado de privacidad documentado para las cinco copias: **`PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`**.
- **Resultado técnico A6:** **CUMPLE** el mínimo documental de cinco registros con metadatos EXIF válidos y la clasificación de privacidad vigente.

> La comprobación técnica A6 no sustituye la responsabilidad humana de verificar visualmente que las copias públicas no revelen identificadores no autorizados.

## Multimedia pública clasificada

- `05_MVP/video_demo.mp4` — video demostrativo del MVP.
- `09_Defensa/video_defensa.mp4` — grabación de la defensa final.
- `10_Autoria/grabaciones/Vd_01.mp4` — grabación de sesión de trabajo del equipo.
- `10_Autoria/grabaciones/Vd_02.mp4` — grabación de sesión de trabajo del equipo.

## Revisión visual/manual requerida

- Consentimientos censurados: **16**.
- Actas de walkthrough: **6**.
- Fotografías públicas de aplicación del cuestionario: **5**.
- Fotografías públicas del equipo/autoría: **2**.
- Total de piezas que requieren o pueden requerir revisión visual según su naturaleza: **29**.

Este auditor no inspecciona visualmente el contenido de PDFs, imágenes o videos. Debe confirmarse manualmente que las copias censuradas/enmascaradas no revelen firmas, nombres, cédulas, teléfonos, correos, respuestas individuales u otros identificadores no autorizados.

## Confirmaciones humanas antes del tag final

- [ ] `02_Evidencias/00_Restringido/evidencias_restringidas.7z` está cifrado/protegido.
- [ ] La contraseña/clave del contenedor restringido **NO** aparece en GitHub, README, commits ni artefactos públicos.
- [ ] `A11 Fotos_Originales_Cuestionario.7z` está cifrado/protegido y su clave permanece fuera del repositorio.
- [ ] Las cinco fotografías públicas del cuestionario siguen visualmente enmascaradas y no revelan identificadores no autorizados.
- [ ] Los consentimientos censurados y actas públicas no exponen firmas, cédulas, teléfonos, correos ni otros identificadores.
- [ ] La capa pública de `07_Datos/` y los artefactos de publicación no contienen datos personales directos.

## Interpretación del código de salida

- `0`: no existen hallazgos automáticos bloqueantes; todavía deben cerrarse las confirmaciones humanas anteriores.
- `2`: existe al menos un hallazgo automático que debe corregirse antes del release/tag final.

## Estado de cierre

**Resultado automático: APTO PARA CONTINUAR CON EL CIERRE**, condicionado únicamente a completar las confirmaciones humanas de cifrado y revisión visual antes de crear el tag final.
