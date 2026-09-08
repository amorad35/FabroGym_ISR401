# Verificación C3 — MVP FabroGym

## Resultado

- RF Must priorizados: **19**.
- RF Must implementados en esta versión: **16**.
- Cobertura: **84,21 %**.
- Umbral C3: **≥ 80 %**.
- RF no contabilizados: **RF-16, RF-17, RF-19**.

## Comprobación ejecutada

Se ejecutó una prueba automatizada de interfaz sobre la copia exacta de `MVP_HTML`, cargando `data.js` y `app.js` en Chromium. Resultado: **31/31 comprobaciones correctas**, sin errores JavaScript durante el recorrido.

Las comprobaciones incluyeron:

1. rechazo de credenciales inválidas e inicio de sesión válido;
2. restricciones de navegación por rol;
3. creación de plan;
4. alta y búsqueda de cliente por código, nombre y contacto;
5. advertencia de coincidencia antes de duplicar;
6. rechazo de renovación sin pago confirmado;
7. registro de pago confirmado y comprobante interno;
8. renovación con pago y visualización de inicio/vencimiento;
9. novedad vinculada a cliente y consulta desde el cliente;
10. rechazo de asistencia no vigente y registro de excepción autorizada;
11. filtro de asistencias por cliente, fecha y turno con conteo;
12. creación de producto;
13. creación de rutina completa;
14. nueva versión de rutina y conservación de la anterior en solo lectura;
15. alertas de vencimiento de tres días;
16. pantalla C3 con 16/19 y exclusión explícita de RF-16, RF-17 y RF-19.

El detalle máquina a máquina está en `resultado_pruebas_ui.json`. `captura_cobertura_c3.png` corresponde al resultado final de la pantalla de cobertura durante la misma verificación.

## Docker

La configuración incluye `docker-compose.yml` en `05_MVP/` y `Dockerfile` en `MVP_HTML/`. En el entorno de generación se verificó la estructura y sintaxis de los archivos, pero no se ejecutó Docker porque el motor Docker no estaba disponible en dicho entorno. La ejecución final debe comprobarse en Docker Desktop antes de la defensa con:

```bash
cd 05_MVP
docker compose up --build
```
