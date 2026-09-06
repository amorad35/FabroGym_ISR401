# F4-A11 — EXIF inventario final preparado

## Resultado técnico

Se procesaron los dos RAR originales recibidos desde el teléfono.

- Fotografías A6 seleccionadas para `10_Autoria/fotos_equipo/`: **6**
- Fotografías de aplicación del cuestionario: **5**
- Total de filas en `exif_inventario.csv`: **11**
- Filas con fecha EXIF real: **11**
- Fechas inventadas: **0**
- Metadatos EXIF modificados: **0**

Las seis fotografías A6 seleccionadas contienen al menos dos personas del equipo en el gimnasio según revisión visual del material recibido.

## Privacidad del cuestionario

Las cinco fotografías originales del cuestionario contienen personas identificables.
Por eso se entregan dentro de:

`PENDIENTE_PRIVACIDAD_NO_SUBIR_A_GIT/Fotos_Aplicacion_Cuestionario_originales/`

No deben copiarse al repositorio público hasta comprobar que el consentimiento real autoriza la publicación de la imagen.

La ruta prevista, solo si la publicación está autorizada, es:

`02_Evidencias/Cuestionario/Fotos_Aplicacion/`

A11 ya registra su EXIF y SHA-256 real sin alterar los archivos.

## Archivos excluidos de `foto equipo.rar`

El RAR contenía **18 archivos que no se incorporaron como A6**. Se excluyeron porque no cumplen el criterio visual de una foto de equipo con al menos dos integrantes, son imágenes de entorno/individuales, son irrelevantes o contienen documentación/datos que no corresponde publicar como evidencia A6.

No se copiaron esos archivos al paquete final.

## Regla de integridad

Este paquete no inventó fechas, modelos de dispositivo ni metadatos.
Cuando el modelo exacto del teléfono no está disponible en EXIF, el CSV lo indica expresamente.
