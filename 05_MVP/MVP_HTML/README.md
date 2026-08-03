# FabroGym MVP — demostración funcional

MVP académico ejecutable para la Entrega 3 (2A) de Ingeniería de Requerimientos. Implementa flujos de autenticación, clientes, membresías, asistencias y rutinas con datos totalmente sintéticos.

## Cobertura de requisitos Must

La priorización vigente del proyecto contiene 19 RF Must. Este MVP implementa 12 RF Must:

- RF-AUT-01, RF-AUT-02
- RF-CLI-01, RF-CLI-02, RF-CLI-03
- RF-MEM-02, RF-MEM-03, RF-MEM-04
- RF-ASI-01, RF-ASI-02
- RF-RUT-01, RF-RUT-02

**Cobertura:** 12/19 = **63,2 %**, superior al mínimo del 60 % exigido para el MVP.

## Ejecución rápida sin Docker

Abra `index.html` con Chrome o Edge. Para evitar restricciones del navegador, también puede ejecutar:

```bash
python -m http.server 8080
```

Después abra `http://localhost:8080`.

## Ejecución con Docker

```bash
docker compose up --build
```

Después abra `http://localhost:8080`.

## Credenciales de demostración

- Administrador: `admin` / `admin123`
- Recepción: `recepcion` / `recep123`
- Instructor: `instructor` / `instr123`

## Persistencia

La aplicación utiliza `localStorage`. No se conecta a una base de datos externa.

## Privacidad y ética

Todos los nombres, identificaciones, teléfonos, asistencias y rutinas son ficticios. El sistema muestra la etiqueta **DATO SINTÉTICO — NO REAL** y no utiliza información de clientes reales, datos de salud, biometría ni fotografías.

## Video

El archivo `video_demo.mp4` presenta el recorrido funcional y dura menos de tres minutos.

## Tecnologías

HTML5, CSS3, JavaScript, Nginx y Docker Compose.
