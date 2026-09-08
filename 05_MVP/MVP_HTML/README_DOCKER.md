# FabroGym MVP — ejecución con Docker

El `Dockerfile` está dentro de `05_MVP/MVP_HTML/` y el archivo `docker-compose.yml` está en `05_MVP/`.

## Ejecución recomendada

Desde la carpeta `05_MVP/`:

```powershell
docker compose up --build
```

Abrir:

```text
http://localhost:8080
```

Para detener:

```powershell
docker compose down
```

También puede construirse directamente desde `05_MVP/MVP_HTML/`:

```powershell
docker build -t fabrogym-mvp .
docker run --rm -p 8080:80 fabrogym-mvp
```

El contenedor usa Nginx y publica exclusivamente el prototipo estático (`index.html` y `assets/`).
