# MVP HTML v2 - Fabro Gym

## Alcance implementado

El MVP cubre los seis requisitos funcionales del bloque Mera:

- RF-ASI-01: registrar asistencia y validar estado/duplicado.
- RF-ASI-02: consultar historial, filtrar y exportar asistencias.
- RF-RUT-01: crear y asignar rutinas.
- RF-RUT-02: registrar seguimiento y versionar rutinas.
- RF-INS-01: consultar alumnos asignados e información operativa mínima.
- RF-INS-02: registrar y consultar disponibilidad, retrasos y ausencias del instructor.

## Ejecución

1. Abra `index.html` con Chrome, Edge o Firefox.
2. También puede ejecutar un servidor local desde esta carpeta:

```bash
python -m http.server 8080
```

3. Abra `http://localhost:8080`.

## Persistencia

Los datos sintéticos se almacenan en `localStorage`. El botón “Restablecer demo” recupera el conjunto inicial.

## Privacidad

No se utilizan datos reales de clientes, información corporal, biometría, diagnósticos ni fotografías. Todos los nombres y registros son ficticios.
