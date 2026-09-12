# 10_Autoria — Evidencia de autoría y trabajo propio

**Proyecto:** FabroGym — ISR-401  
**Entrega:** Entrega 4 (2B / Defensa Final)  
**Repositorio:** `https://github.com/amorad35/FabroGym_ISR401`

## 1. Propósito

Esta carpeta reúne la evidencia verificable de autoría, contribución individual y trabajo propio del equipo FabroGym.

La rúbrica final exige que `10_Autoria/` exista con los elementos A1 a A12 como un conjunto completo. Esta carpeta complementa el historial Git y los artefactos técnicos; no los sustituye.

## 2. Equipo actual de cierre

El equipo que realiza el cierre y la defensa final está conformado por:

- **Mera Arias Erick Jhair** — Git: `Emeraxs`
- **Mora Duarte Alex José** — Git: `amorad35`
- **Ponce Rivera Mery Helenmey** — Git: `Mery-003`

Las contribuciones históricas de integrantes que participaron anteriormente permanecen visibles en el historial Git y en los artefactos donde corresponden. No se eliminan, reasignan ni presentan como trabajo de los tres integrantes actuales.

## 3. Principios de integridad

Toda evidencia incorporada en `10_Autoria/` debe:

- corresponder a una actividad real;
- conservar fecha y procedencia reales;
- no ser retrofechada;
- no ser reconstruida artificialmente para aparentar trabajo previo;
- no contener placeholders ni archivos vacíos que anuncien evidencia inexistente;
- utilizar hashes de commit reales cuando se cite trabajo versionado;
- mantener coherencia entre artefacto, persona responsable e historial Git;
- respetar las reglas de privacidad y la separación entre capa pública y restringida.

## 4. Estructura A1–A12

### A1 — `bitacora_sesiones.csv`

Registro cronológico de sesiones reales de trabajo.

Cada fila debe documentar, según corresponda:

- identificador de sesión;
- fecha y horario;
- modalidad;
- participantes;
- usuarios Git;
- rutas trabajadas;
- decisiones tomadas;
- commits reales producidos;
- fuente de evidencia y observaciones.

No deben quedar marcadores como `PENDIENTE_COMMIT_*` en la versión congelada.

### A2 — `capturas/`

Capturas reales de trabajo individual o colaborativo sobre FabroGym.

Deben permitir relacionar la captura con:

- herramienta utilizada;
- artefacto trabajado;
- usuario o integrante;
- fecha/hora cuando esté disponible.

### A3 — `fuentes_editables/`

Fuentes editables de diagramas y modelos utilizados en el proyecto.

Incluye, cuando corresponda:

```text
*.vpp
*.drawio
*.puml
```

Las exportaciones PNG/PDF/SVG no sustituyen la fuente editable cuando esta existe.

### A4 — `grabaciones/`

Grabaciones reales de sesiones de trabajo del equipo.

Deben corresponder a actividades efectivas de revisión, edición, discusión o toma de decisiones sobre FabroGym.

### A5 — `notas_campo/`

Notas reales obtenidas durante actividades de elicitación, observación o validación.

No se reconstruyen notas posteriormente para aparentar evidencia de campo.

### A6 — `fotos_equipo/`

La evidencia fotográfica de autoría se organiza en:

```text
10_Autoria/
└── fotos_equipo/
    ├── 01_fotos_equipo/
    └── 02_Fotos_Aplicacion/
        └── A11 Fotos_Originales_Cuestionario.7z
```

Además, las **cinco copias públicas enmascaradas de aplicación del cuestionario** se encuentran en:

```text
02_Evidencias/Cuestionario/Fotos_Aplicacion/
```

Los originales utilizados para preservar EXIF se conservan dentro del contenedor restringido:

```text
10_Autoria/fotos_equipo/02_Fotos_Aplicacion/
A11 Fotos_Originales_Cuestionario.7z
```

Ese contenedor debe permanecer cifrado/protegido y su contraseña o clave no debe almacenarse en el repositorio.

### A7 — `doble_codificacion/`

Evidencia de doble codificación independiente de un subconjunto común del corpus de walkthroughs.

Debe conservar:

- las dos hojas independientes;
- el subconjunto codificado;
- el script de cálculo;
- kappa/acuerdo e intervalo de confianza.

### A8 — `correspondencia/`

Comunicaciones reales y fechadas con la organización relacionadas con el proyecto.

Antes de publicar cualquier pieza se revisa que no exponga datos personales no autorizados.

### A9 — `declaracion_uso_ia.md`

Declaración del uso de herramientas de IA por sección o artefacto relevante.

Debe indicar:

- herramienta;
- propósito;
- responsable de revisión;
- método de verificación;
- secciones donde no se utilizó IA, cuando corresponda.

### A10 — `aporte_individual.md` y evidencia firmada

`aporte_individual.md` documenta la contribución verificable de los **tres integrantes actuales de cierre**:

- Mera Arias Erick Jhair;
- Mora Duarte Alex José;
- Ponce Rivera Mery Helenmey.

Para cada integrante se registran actividades, rutas, rol y commits reales.

La conformidad firmada del equipo actual se conserva como:

```text
10_Autoria/aporte_individual_FIRMA.pdf
```

La versión firmada corresponde a los tres integrantes actuales de cierre. Los aportes históricos de otros integrantes permanecen en Git y no se borran ni se reasignan.

### A11 — `exif_inventario.csv`

Inventario técnico de fotografías utilizadas como evidencia.

Para las cinco fotografías de aplicación del cuestionario, el inventario conserva:

- fecha EXIF del original;
- dispositivo;
- SHA-256;
- estado EXIF;
- relación entre original restringido y copia pública enmascarada.

Las copias públicas pueden tener hash distinto del original por el enmascaramiento; el inventario primario se basa en los originales preservados.

### A12 — `/.mailmap`

La evidencia A12 se mantiene en la raíz:

```text
/.mailmap
```

Su función es normalizar identidades históricas de Git hacia nombres y correos institucionales sin reescribir el historial.

No se crea una segunda `.mailmap` dentro de `10_Autoria/`.

## 5. Relación con el historial Git

El historial Git es evidencia central de autoría.

Reglas:

- cada contribución citada debe apuntar a commits reales;
- los integrantes activos deben usar identidad real y correo institucional;
- no se atribuyen a una persona commits producidos por otra;
- no se reescribe el historial para fabricar distribución de trabajo;
- los mensajes de commit deben describir el cambio realizado.

Para la revisión final se recomienda comprobar:

```bash
git shortlog -sne --all --use-mailmap
```

## 6. Privacidad

`10_Autoria/` contiene evidencia del trabajo del equipo y debe respetar la política definida en `08_Etica/`.

Antes del tag final se debe confirmar:

- que los contenedores restringidos estén cifrados/protegidos;
- que sus contraseñas no estén almacenadas en Git;
- que las copias públicas enmascaradas no revelen identificadores no autorizados;
- que los consentimientos, actas y correspondencia pública estén adecuadamente censurados.

El reporte automático vigente se conserva en:

```text
07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md
```

y actualmente documenta **0 hallazgos automáticos bloqueantes**.

## 7. Verificación de cierre

Antes de congelar la entrega se debe comprobar:

1. A1–A12 presentes y coherentes;
2. ausencia de archivos vacíos/placeholder;
3. hashes de commit citados existentes;
4. autores normalizados mediante `.mailmap`;
5. doble codificación reproducible;
6. cinco fotografías A6 con EXIF válido y copias públicas enmascaradas;
7. declaración de uso de IA consistente;
8. `aporte_individual.md` sincronizado con los commits finales;
9. privacidad automática sin bloqueos y revisión humana completada;
10. `git status` limpio antes de crear el tag.

La verificación previa firmada se conserva como
`10_Autoria/verificacion_previa.pdf`, conforme a la guía específica
de cierre. Este archivo complementa A1–A12 y no sustituye ninguno
de esos elementos.

## 8. Estado de esta carpeta

`10_Autoria/` se mantiene como evidencia viva hasta el último commit previo al tag.

Antes de congelar la entrega únicamente deben sincronizarse los documentos de autoría si existen commits posteriores y eliminarse cualquier marcador pendiente que haya quedado en la bitácora.

No se deben crear evidencias ficticias ni modificar evidencia histórica ya válida.
