# Revisión automática de privacidad — F3-07 / B6

**Estado automático:** **SIN HALLAZGOS AUTOMÁTICOS BLOQUEANTES**.  
**Estado humano de cierre:** **CONFIRMACIONES MANUALES CERRADAS**.

## Criterio aplicado

- `07_Datos/` y los artefactos de publicación deben permanecer sin datos personales directos.
- La capa restringida cifrada se trata de forma separada.
- La presencia de un contenedor restringido expresamente documentado no constituye por sí sola un hallazgo bloqueante.
- El auditor automático no abre archivos cifrados ni conoce contraseñas; las comprobaciones de cifrado, ausencia de claves y revisión visual fueron confirmadas manualmente por el equipo antes del tag final.

## Alcance de la auditoría

- Archivos del árbol inspeccionados por nombre/extensión: **1008**.
- CSV inspeccionados en `07_Datos/datos_crudos` y `datos_procesados`: **20**.
- CSV no legibles durante el análisis: **0**.
- Hallazgos automáticos bloqueantes: **0**.
- Advertencias / comprobaciones humanas pendientes: **0**.

## Capa restringida documentada

- `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — **CIFRADO/PROTECCIÓN CONFIRMADOS MANUALMENTE** — contenedor restringido previsto por FabroGym y versionado mediante Git LFS; la clave permanece fuera del repositorio.
- `02_Evidencias/00_Restringido/fichas_tecnicas.csv` — **DOCUMENTADO** — inventario técnico de evidencia con códigos, duración, códec, tamaño y SHA-256.
- `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` — **CIFRADO/PROTECCIÓN CONFIRMADOS MANUALMENTE** — contenedor de fotografías originales A11 utilizado para preservar EXIF; la clave permanece fuera del repositorio.

## Resultado automático

No se detectaron hallazgos automáticos bloqueantes con las reglas aplicadas.

Los artefactos de la capa restringida están documentados expresamente por la política F3-07/B6. Su sola presencia no se interpreta como exposición accidental de datos.

Las cinco fotografías públicas del cuestionario figuran en `10_Autoria/exif_inventario.csv` con estado `PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`. Los registros de fotografías de autoría/equipo ya no conservan el marcador transitorio `EQUIPO_AUTORIA_REVISAR_PUBLICACION`, pues su revisión de publicación quedó cerrada.

## Confirmaciones manuales cerradas

- **CIFRADO_CONFIRMADO** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z`.
- **CLAVE_FUERA_DE_GIT_CONFIRMADA** — no se conserva la contraseña/clave en GitHub, README, commits ni artefactos públicos.
- **CIFRADO_CONFIRMADO** — `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`.
- **REVISION_VISUAL_CONFIRMADA** — las cinco fotografías públicas del cuestionario permanecen enmascaradas y sin identificadores no autorizados.
- **REVISION_VISUAL_CONFIRMADA** — consentimientos censurados y actas públicas revisados sin identificadores no autorizados.
- **CAPA_PUBLICA_CONFIRMADA** — `07_Datos/` y los artefactos de publicación revisados sin datos personales directos.

## Verificaciones informativas

- **LFS_RESTRINGIDO_ESPERADO** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — puntero Git LFS documentado de **1.521.924.213 bytes**, SHA-256 `a1b9b56a4fddf469a39bab3a51bcc891c85c0d0ce70432bf8602513f84c24070`.
- **A6_EXIF_OK** — `10_Autoria/exif_inventario.csv` — los **5** registros F3-01 documentan fecha EXIF, fuente EXIF, dispositivo y SHA-256 válidos.
- **A6_PRIVACIDAD_DOCUMENTADA** — los **5** registros F3-01 están clasificados como `PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`.
- **RESTRINGIDO_DOCUMENTADO** — los tres artefactos de la capa restringida están contemplados por la política actual del proyecto.

## Verificación técnica A6 — fotografías del cuestionario y EXIF

- Registros `F3-01_APLICACION_CUESTIONARIO` en `10_Autoria/exif_inventario.csv`: **5**.
- Registros con fecha EXIF, fuente EXIF, dispositivo, `Estado_EXIF=OK` y SHA-256 válido: **5**.
- Copias fotográficas presentes en `02_Evidencias/Cuestionario/Fotos_Aplicacion/`: **5**.
- Estado de privacidad documentado: **`PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`**.
- **Resultado técnico A6:** **CUMPLE**.

## Multimedia pública clasificada

- `05_MVP/video_demo.mp4` — video demostrativo del MVP.
- `09_Defensa/video_defensa.mp4` — grabación de la defensa final.
- `10_Autoria/grabaciones/Vd_01.mp4` — grabación de sesión de trabajo del equipo.
- `10_Autoria/grabaciones/Vd_02.mp4` — grabación de sesión de trabajo del equipo.

## Revisión visual/manual

La revisión humana de las piezas públicas y de los contenedores restringidos fue registrada como **COMPLETADA** para el cierre B6.

- [x] `02_Evidencias/00_Restringido/evidencias_restringidas.7z` está cifrado/protegido.
- [x] La contraseña/clave del contenedor restringido **NO** aparece en GitHub, README, commits ni artefactos públicos.
- [x] `A11 Fotos_Originales_Cuestionario.7z` está cifrado/protegido y su clave permanece fuera del repositorio.
- [x] Las cinco fotografías públicas del cuestionario siguen visualmente enmascaradas y no revelan identificadores no autorizados.
- [x] Los consentimientos censurados y actas públicas no exponen firmas, cédulas, teléfonos, correos ni otros identificadores.
- [x] La capa pública de `07_Datos/` y los artefactos de publicación no contienen datos personales directos.

## Interpretación del código de salida

- `0`: no existen hallazgos automáticos bloqueantes. Las confirmaciones humanas de cierre B6 están documentadas como completadas.
- `2`: existe al menos un hallazgo automático que debe corregirse antes del release/tag final.

## Estado de cierre

**RESULTADO CONSOLIDADO: APTO PARA CREAR EL TAG FINAL**, con **0 hallazgos automáticos bloqueantes** y **0 confirmaciones humanas pendientes**.
