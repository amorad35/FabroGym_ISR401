# FabroGym — parche MVP Entrega 4 (2B)

Este paquete está pensado para **reemplazar/añadir únicamente** los archivos equivalentes dentro del prototipo `FabroGym_HTML_Interactivo_Escala_Equilibrada` utilizado en validaciones.

## Cobertura Must

Se mantienen 12 RF existentes y se incorporan:

- RF-MEM-01 — Configurar planes y promociones.
- RF-PAG-01 — Registrar pago y comprobante interno.
- RF-INV-01 — Administrar productos.
- RF-NOV-01 — Gestionar novedades internas.

Cobertura final documentada: **16/19 = 84,2 %**.

No se cuentan como implementados RF-INV-02, RF-VEN-01 ni RF-CAJ-01.

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
