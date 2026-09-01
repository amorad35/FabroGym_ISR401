# README_reproducibilidad - FabroGym Fase 2

## Que contiene
Este directorio cierra el analisis empirico reproducible de la Entrega 4 (2B) sin fabricar metricas no
soportadas. La unidad principal del Enfoque 3 son los seis walkthroughs documentados en el protocolo v1.4;
las 10 entrevistas iniciales se conservan para el corpus general y la ficha tecnica, y la encuesta de 70
clientes se analiza como evidencia descriptiva de dominio.

## Identificadores congelados
Entrevistas: `ENTR-01` ... `ENTR-10`.
Walkthroughs no tecnicos: `WALK-NTEC-01`, `WALK-NTEC-02`, `WALK-NTEC-03`.
Walkthroughs tecnicos: `WALK-TEC-01`, `WALK-TEC-02`, `WALK-TEC-03`.
Member checking: `MC-P01`, `MC-P02`, `MC-P03`.

No renombre estos codigos.

## Ejecucion
Desde `06_Experimento/`:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r scripts_analisis/requirements.txt
python scripts_analisis/run_all.py
```

La ejecucion regenera las tablas y figuras principales en `resultados/`.

## Datos de entrada
- `datos_crudos/encuesta_clientes_anonimizada.csv`: 70 respuestas; columnas directas de identificacion vacias.
- `datos_crudos/sesiones_multimedia_desde_ficha_v3_1.csv`: subconjunto analitico de la ficha tecnica v3.1,
  conservando nombres exactos, codigos, duraciones y hashes declarados para audio/video.
- `datos_crudos/codificacion_walkthroughs.csv`: 76 fragmentos codificados.
- `datos_crudos/member_checking_estructurado.csv`: 12 decisiones extraidas de la evidencia documental.
- `datos_crudos/member_checking/Revisiones_RNF_explicabilidad_FabroGym_2026-08-29.pdf`: evidencia documental anonimizada.
- `datos_crudos/walkthroughs/`: seis transcripciones anonimizadas normalizadas a `WALK-*`.

## Resultados clave reproducidos
- 16 sesiones multimedia; videos = **06:18:08** (378.133 min); audios = **06:18:14**.
- Encuesta: **n=70**, sin variable tecnico/no tecnico y sin Likert de explicabilidad.
- Walkthroughs: **76 fragmentos**, 49 tecnicos, 27 no tecnicos, 37 codigos normalizados, 18 categorias.
- Explicabilidad: **9 fragmentos pertinentes**, 4 RNF terminales.
- Member checking: **12 decisiones** = 4 Confirmado + 8 Ajustado + 0 No confirmado.
- Saturacion por codigo: ultimas tres = **6.306%**, no cumple estrictamente <=5%.
- Estabilizacion axial: **1.852%**, evidencia complementaria.

## Decisiones metodologicas
No se calculan Fleiss kappa ni Mann-Whitney porque el protocolo v1.4 no preregistro hipotesis inferenciales
para tres sesiones por perfil y no existen puntuaciones cuantitativas de explicabilidad por participante.
Tampoco se reetiquetan preguntas generales de encuesta como Likert de explicabilidad.

`tabla_aplicabilidad_pruebas_estadisticas.csv` documenta cada no-aplicabilidad.

## Integridad
El script solo valida el formato de los SHA-256 declarados. Para afirmar que un hash coincide con el archivo
audiovisual se debe ejecutar `sha256sum` o equivalente sobre el material real de la zona restringida.
