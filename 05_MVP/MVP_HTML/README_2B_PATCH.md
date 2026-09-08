# FabroGym MVP — cierre C3 de Entrega 4 (2B)

## Cobertura Must

La priorización vigente contiene 19 RF Must. Esta versión implementa y documenta 16:

- RF-01, RF-02;
- RF-04, RF-05, RF-06;
- RF-07, RF-08, RF-09, RF-10;
- RF-11;
- RF-13, RF-14;
- RF-15;
- RF-20;
- RF-22, RF-23.

Cobertura:

```text
16 / 19 = 84,21 %
```

No se contabilizan como implementados:

- RF-16 — entradas y ajustes de stock;
- RF-17 — venta y descuento de existencias;
- RF-19 — conciliación y cierre de caja.

## Cambios funcionales de cierre

- búsqueda de clientes por código, nombre normalizado o contacto;
- consulta de último pago, última asistencia y novedades abiertas;
- advertencia de coincidencias antes de crear duplicados;
- renovación de membresía condicionada a plan vigente y pago confirmado no aplicado;
- fechas de inicio y vencimiento visibles;
- alertas de membresías vencidas o con vencimiento en los próximos tres días;
- asistencia con excepción autorizada documentada;
- filtros de asistencia por cliente, fecha y turno con conteo;
- rutinas con objetivo, series, repeticiones, descanso y días;
- versionado real de rutinas con historial anterior en solo lectura;
- IDs sincronizados con el catálogo normalizado RF-01...RF-25.

## Docker

El despliegue se ejecuta desde `05_MVP/` con:

```bash
docker compose up --build
```

El `Dockerfile` está en `MVP_HTML/` y sirve el prototipo mediante Nginx.
