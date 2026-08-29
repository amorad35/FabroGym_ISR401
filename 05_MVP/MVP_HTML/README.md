# FabroGym MVP — demostración funcional

Aplicación web estática del MVP académico de FabroGym.

## Ejecución rápida

Abra `index.html` con Chrome, Edge o Firefox.

Como alternativa:

```bash
python -m http.server 8080
```

y abra:

```text
http://localhost:8080
```

## Ejecución con Docker

Esta carpeta contiene un `Dockerfile`. Desde `05_MVP/MVP_HTML/` ejecute:

```bash
docker build -t fabrogym-mvp .
docker run --rm -p 8080:80 fabrogym-mvp
```

Después abra:

```text
http://localhost:8080
```

No se utiliza `docker compose` mientras no exista un archivo `docker-compose.yml` o `compose.yml` versionado.

## Credenciales de demostración

- Administrador: `admin` / `admin123`
- Recepción: `recepcion` / `recep123`
- Instructor: `instructor` / `instr123`

## Persistencia

La aplicación utiliza `localStorage` y no requiere una base de datos externa.

## Privacidad

Todos los datos utilizados deben ser ficticios o sintéticos. No deben almacenarse datos personales reales, información de salud, biometría, fotografías ni credenciales reales.
