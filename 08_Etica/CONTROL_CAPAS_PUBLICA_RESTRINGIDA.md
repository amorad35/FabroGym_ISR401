# F3-07 — Control de capa pública [P] y capa restringida [R]

## Regla obligatoria

FabroGym separa la evidencia en dos capas:

- **[P] Pública:** datos anonimizados o seudonimizados, transcripciones anonimizadas, matrices de análisis, scripts, resultados, instrumentos no identificables y copias censuradas/enmascaradas aptas para publicación.
- **[R] Restringida:** consentimientos originales firmados, firmas, cédulas, audios, videos identificables, transcripciones sin anonimizar, fotografías identificables sin autorización de publicación y cualquier otro dato personal directo.

La capa [R] debe permanecer fuera de GitHub y de Zenodo, almacenada bajo acceso restringido y cifrado/protegido.

## Situación verificada antes de la integración final

En el repositorio público actual ya existe una política de separación [P]/[R] y las carpetas públicas de consentimientos y walkthroughs usan copias censuradas/enmascaradas. La revisión de nombres del repositorio no muestra los consentimientos originales como archivos públicos; sí existen referencias documentales a sus rutas o hashes, lo cual no equivale a publicar los originales.

El `.gitignore` actual no contiene todavía reglas específicas para impedir que material restringido se añada por accidente. Este paquete añade esas barreras.

## F3-01 — dependencia pendiente

Las fotografías de aplicación del cuestionario todavía están en progreso. Antes de publicarlas:

1. comprobar que no muestran nombres, respuestas individuales, teléfonos, correos, cédulas ni pantallas con datos personales;
2. si aparece una persona reconocible, confirmar autorización de publicación o generar una versión pública no identificable;
3. conservar el original identificable únicamente en [R] cuando corresponda;
4. preservar en el original la fecha/metadatos exigidos.

Por esta dependencia, **F3-07 permanece EN PROGRESO** hasta revisar las fotografías finales.

## Verificación de la capa restringida

GitHub no puede demostrar que la capa [R] está cifrada porque precisamente esa capa debe estar fuera del repositorio. Antes de cerrar F3-07, un integrante debe confirmar localmente:

- [ ] originales restringidos fuera de la carpeta clonada;
- [ ] almacenamiento restringido cifrado/protegido;
- [ ] acceso limitado a integrantes autorizados;
- [ ] consentimientos originales disponibles para las sesiones que los requieren;
- [ ] audios/videos reales fuera del repositorio público;
- [ ] fotografías F3-01 clasificadas como [P] o [R];
- [ ] auditoría automática final ejecutada después de integrar todos los paquetes.

No se registran en Git contraseñas, claves ni rutas privadas sensibles.
