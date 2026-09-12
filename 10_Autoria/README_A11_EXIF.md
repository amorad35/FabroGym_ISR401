# F4-A11 — Inventario EXIF y fotografías de aplicación

## Resultado técnico

El inventario conserva la información técnica obtenida de los archivos originales recibidos.

- Fotografías A6 seleccionadas del equipo: **6**
- Fotografías de aplicación del cuestionario: **5**
- Total de filas en `exif_inventario.csv`: **11**
- Filas con fecha EXIF real: **11**
- Fechas inventadas: **0**
- Metadatos EXIF modificados en los originales: **0**

## Fotografías del cuestionario

Las cinco fotografías originales del cuestionario contienen personas identificables. Para preservar la evidencia original y sus metadatos EXIF se conservan dentro del contenedor restringido:

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`

El contenedor debe permanecer cifrado/protegido y su contraseña o clave no debe registrarse en el repositorio.

Las copias destinadas a revisión pública se conservan en:

`02_Evidencias/Cuestionario/Fotos_Aplicacion/`

Estas copias se tratan como versiones públicas enmascaradas. El enmascaramiento puede modificar el hash o los metadatos de la copia pública; por ello, `exif_inventario.csv` conserva como fuente primaria la fecha, dispositivo y SHA-256 de los archivos originales.

El estado de las cinco filas `F3-01_APLICACION_CUESTIONARIO` queda registrado como:

`PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`

Esto indica que existe una copia pública enmascarada y que el original con EXIF se conserva en la capa restringida.

## Regla de integridad

No se inventan fechas, modelos de dispositivo ni metadatos. Los originales no se sobrescriben con las versiones enmascaradas y la evidencia restringida conserva su función de respaldo técnico.

## Correspondencia con las copias públicas actuales

El inventario mantiene en la columna `Nombre` el nombre del archivo original del que se obtuvo el EXIF y el SHA-256. La columna `Ruta_final_o_prevista` apunta a la copia pública enmascarada existente actualmente en el repositorio:

- `IMG_20260721_102618.jpg` → `Aplicacion_Cuestionario_01..jpg`
- `IMG_20260721_104307.jpg` → `Aplicacion_Cuestionario_02.jpg`
- `IMG_20260721_154701.jpg` → `Aplicacion_Cuestionario_03.jpg`
- `IMG_20260721_154901.jpg` → `Aplicacion_Cuestionario_04.jpg`
- `IMG_20260825_142844.jpg` → `Aplicacion_Cuestionario_05.jpg`

La diferencia de nombre no altera la trazabilidad: los valores EXIF y SHA-256 registrados corresponden al original, mientras que la ruta corresponde a la copia pública enmascarada.
