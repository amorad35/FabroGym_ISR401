# Dos escenarios de demostracion - FabroGym 2B

## Reglas antes de iniciar
- Abrir el MVP antes de entrar al aula y probarlo sin internet si es posible.
- Usar solo credenciales demo y datos sinteticos.
- No usar nombres reales, pagos reales ni informacion de clientes reales.
- Tener una captura local de respaldo por cada paso critico.

## Demo 1 - Cliente, pago, membresia y asistencia
**Objetivo:** demostrar el flujo operativo principal de recepcion.

**Requisitos trazados:** RF-CLI-01, RF-CLI-02, RF-MEM-02, RF-MEM-03, RF-PAG-01, RF-ASI-01.

**Pasos:**
1. Iniciar sesion con rol de recepcion.
2. Buscar un cliente sintetico o registrar uno nuevo.
3. Registrar pago de membresia y mostrar comprobante interno.
4. Renovar/activar membresia y verificar fecha de vencimiento.
5. Registrar asistencia no biometrica.
6. Mostrar que el estado quedo actualizado.

**Frase final:** Este escenario demuestra continuidad entre evidencia de campo, RF Must, criterio de aceptacion y prototipo.

## Demo 2 - Inventario, venta y cierre de caja
**Objetivo:** mostrar control operativo y reduccion de errores en ventas e inventario.

**Requisitos trazados:** RF-INV-01, RF-INV-02, RF-VEN-01, RF-CAJ-01, RF-AUT-03.

**Pasos:**
1. Crear o consultar un producto con stock minimo.
2. Registrar entrada o ajuste de inventario.
3. Realizar una venta con medio de pago demo.
4. Verificar descuento de stock.
5. Ejecutar cierre de caja o resumen operativo.
6. Mostrar trazabilidad/auditoria si la pantalla lo permite.

**Plan B:** si el MVP falla, abrir el PDF/diapositiva con la ruta de demo, mostrar capturas locales y explicar la traza requisito -> evidencia -> pantalla.
