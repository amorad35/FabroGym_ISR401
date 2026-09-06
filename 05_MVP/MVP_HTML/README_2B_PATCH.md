# FabroGym — parche MVP Entrega 4 (2B)

Este paquete está pensado para **reemplazar/añadir únicamente** los archivos equivalentes dentro del prototipo `FabroGym_HTML_Interactivo_Escala_Equilibrada` utilizado en validaciones.

## Cobertura Must

Se mantienen 12 RF existentes y se incorporan:

- RF-07 — Configurar planes y promociones.
- RF-11 — Registrar pago y comprobante interno.
- RF-15 — Administrar productos.
- RF-20 — Gestionar novedades internas.

La fuente histórica declara **16/19 = 84,2 %**, pero existe una cifra divergente de 12/19. Este bloque no resuelve la cobertura por inferencia: los 19 RF Must quedan **sujetos a verificación terminal C3** contra código y pruebas.

## Archivos del parche

- `index.html`
- `assets/css/styles.css`
- `assets/js/data.js`
- `assets/js/app.js`
- `ABRIR_PROTOTIPO.bat`

Conservar las demás carpetas `assets/` y `pages/` del prototipo original.

## Credenciales sintéticas

- Administrador: `admin / admin123`
- Recepción: `recepcion / recep123`
- Instructor: `instructor / instr123`

Todos los datos son sintéticos y el MVP usa `localStorage`. No procesa pagos reales, biometría, datos de salud ni IA operativa.
