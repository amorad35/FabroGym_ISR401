# FabroGym — Producto Mínimo Viable (MVP) · Entrega 4 (2B)

## 1. Descripción

Prototipo web estático de FabroGym construido con **HTML5, CSS3 y JavaScript**, datos exclusivamente sintéticos y persistencia local mediante `localStorage`. No requiere base de datos externa para la demostración.

Esta versión cierra el criterio **C3** con **16 de 19 RF Must implementados (84,2 %)**. Permanecen fuera del alcance del MVP `RF-16`, `RF-17` y `RF-19`.

## 2. Estructura

```text
05_MVP/
├── README.md
├── docker-compose.yml
├── video_demo.mp4
├── verificacion/
│   ├── MATRIZ_COBERTURA_C3.csv
│   ├── VERIFICACION_C3.md
│   ├── resultado_pruebas_ui.json
│   └── captura_cobertura_c3.png
└── MVP_HTML/
    ├── Dockerfile
    ├── .dockerignore
    ├── README_DOCKER.md
    ├── README_2B_PATCH.md
    ├── ABRIR_PROTOTIPO.bat
    ├── index.html
    └── assets/
        ├── css/styles.css
        └── js/
            ├── data.js
            └── app.js
```

## 3. Ejecución local

Opción directa: abrir `05_MVP/MVP_HTML/index.html` en Chrome, Edge o Firefox.

Opción con servidor local:

```bash
cd 05_MVP/MVP_HTML
python -m http.server 8080
```

Luego abrir `http://localhost:8080`.

## 4. Ejecución con Docker

Desde `05_MVP/`:

```bash
docker compose up --build
```

Abrir `http://localhost:8080`.

Para detener:

```bash
docker compose down
```

También se puede construir directamente con el `Dockerfile` de `MVP_HTML/`. Consulte `MVP_HTML/README_DOCKER.md`.

## 5. Credenciales de demostración

| Rol | Usuario | Contraseña |
|---|---|---|
| Administrador | `admin` | `admin123` |
| Recepción | `recepcion` | `recep123` |
| Instructor | `instructor` | `instr123` |

Son credenciales académicas y sintéticas.

## 6. Cobertura C3

```text
16 / 19 × 100 = 84,21 %
```

RF Must implementados:

`RF-01`, `RF-02`, `RF-04`, `RF-05`, `RF-06`, `RF-07`, `RF-08`, `RF-09`, `RF-10`, `RF-11`, `RF-13`, `RF-14`, `RF-15`, `RF-20`, `RF-22`, `RF-23`.

RF Must no implementados y no contabilizados:

- `RF-16` — entradas y ajustes de stock;
- `RF-17` — venta y descuento de existencias;
- `RF-19` — conciliación y cierre de caja.

La trazabilidad detallada está en `verificacion/MATRIZ_COBERTURA_C3.csv`.

## 7. Verificación técnica

Sobre esta copia exacta se ejecutaron **31/31 comprobaciones de interfaz y lógica en Chromium**, incluyendo autenticación, permisos, alta/búsqueda/actualización de clientes, validación de duplicados, pagos confirmados, renovación de membresía, asistencias y excepciones, filtros, inventario, novedades, rutinas, versionado y pantalla de cobertura. El resultado registrado no produjo errores JavaScript.

Consulte `verificacion/VERIFICACION_C3.md` y `verificacion/resultado_pruebas_ui.json`.

## 8. Video de demostración

`video_demo.mp4` se conserva dentro de la carpeta MVP como evidencia de demostración. Tras integrar cambios adicionales posteriores a esta versión, debe comprobarse que el video siga representando el estado final del prototipo antes del corte.

## 9. Privacidad y alcance

El MVP utiliza únicamente datos ficticios. No deben introducirse nombres, identificaciones, teléfonos, fotografías, datos médicos, credenciales reales ni otra información que permita identificar participantes o clientes reales.

Es un prototipo académico demostrativo. No incluye facturación electrónica, pasarelas bancarias, biometría ni un componente de IA en operación.
