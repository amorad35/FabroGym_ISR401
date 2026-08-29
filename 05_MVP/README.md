# FabroGym — Producto Mínimo Viable (MVP)

## 1. Descripción

FabroGym es un Producto Mínimo Viable desarrollado como una aplicación web estática para demostrar procesos administrativos y operativos de un gimnasio.

El MVP utiliza **HTML5, CSS3 y JavaScript**, datos sintéticos y `localStorage`. No requiere una base de datos externa para su ejecución demostrativa.

## 2. Contenido

```text
05_MVP/
├── README.md
├── video_demo.mp4
└── MVP_HTML/
    ├── Dockerfile
    ├── README.md
    ├── index.html
    ├── styles.css
    └── app.js
```

## 3. Código fuente

El código fuente disponible en este repositorio se encuentra en:

```text
05_MVP/MVP_HTML/
```

El código fuente del MVP se encuentra disponible en este repositorio, dentro de 05_MVP/MVP_HTML/. No se utiliza un repositorio independiente para esta versión del proyecto.

## 4. Ejecución local

### Opción rápida

1. Abrir `05_MVP/MVP_HTML/`.
2. Abrir `index.html` con Chrome, Edge o Firefox.

También puede utilizarse un servidor local:

```bash
cd 05_MVP/MVP_HTML
python -m http.server 8080
```

Luego abrir:

```text
http://localhost:8080
```

### Opción con Docker

Desde `05_MVP/MVP_HTML/`:

```bash
docker build -t fabrogym-mvp .
docker run --rm -p 8080:80 fabrogym-mvp
```

Luego abrir:

```text
http://localhost:8080
```

## 5. Credenciales de demostración

| Rol | Usuario | Contraseña |
|---|---|---|
| Administrador | `admin` | `admin123` |
| Recepción | `recepcion` | `recep123` |
| Instructor | `instructor` | `instr123` |

Las credenciales son exclusivamente académicas y no corresponden a usuarios reales.

## 6. Cobertura documentada

La versión actual documenta 12 RF Must implementados de 19 priorizados:

```text
12 / 19 × 100 = 63,2 %
```

La cobertura deberá actualizarse si el MVP o la priorización cambian.

## 7. Video de demostración

Archivo disponible:

```text
05_MVP/video_demo.mp4
```

El video utiliza únicamente datos ficticios y evidencia el recorrido funcional del MVP.

## 8. Privacidad

El MVP debe utilizar exclusivamente datos sintéticos. No deben incorporarse nombres, identificaciones, teléfonos, fotografías, datos médicos, credenciales reales ni información que permita identificar a participantes o clientes.

## 9. Limitaciones

Esta versión es académica y demostrativa. No representa una versión preparada para producción ni incorpora facturación electrónica, pasarelas bancarias, biometría o inteligencia artificial en operación.
