# F3-07 — Control de capa pública [P] y capa restringida [R]

## Regla obligatoria

FabroGym separa la evidencia en dos capas:

- **[P] Pública:** datos anonimizados o seudonimizados, transcripciones anonimizadas, matrices de análisis, scripts, resultados, instrumentos no identificables y copias censuradas/enmascaradas aptas para publicación.
- **[R] Restringida:** consentimientos originales firmados, firmas, cédulas, audios, videos identificables, transcripciones sin anonimizar, fotografías identificables sin autorización de publicación y cualquier otro dato personal directo.

La capa [R] debe permanecer fuera de GitHub y de Zenodo, almacenada bajo acceso restringido y cifrado/protegido.

## Situación verificada antes de la integración final

En el repositorio público actual ya existe una política de separación [P]/[R] y las carpetas públicas de consentimientos y walkthroughs usan copias censuradas/enmascaradas. La revisión de nombres del repositorio no muestra los consentimientos originales como archivos públicos; sí existen referencias documentales a sus rutas o hashes, lo cual no equivale a publicar los originales.

El `.gitignore` actual no contiene todavía reglas específicas para impedir que material restringido se añada por accidente. Este paquete añade esas barreras.

## F3-01 — evidencia A6 verificada

Las cinco fotografías de aplicación del cuestionario requeridas para A6 se encuentran documentadas y conservan fecha EXIF y dispositivo. Por tanto, el requisito técnico de evidencia fotográfica y metadatos de A6 se considera cubierto.

La revisión de privacidad y autorización de publicación se controla de forma independiente dentro de F3-07/B6. Antes del cierre definitivo de la capa pública se debe comprobar que:

1. no se muestran nombres, respuestas individuales, teléfonos, correos, cédulas ni pantallas con datos personales;
2. si aparece una persona reconocible, existe autorización de publicación o se dispone de una versión pública no identificable;
3. el original identificable se conserva únicamente en [R] cuando corresponda;
4. se preservan en el original la fecha y los metadatos exigidos.

De esta forma, **A6 queda cubierto por la evidencia fotográfica y EXIF**, mientras que el cierre de **F3-07/B6** depende exclusivamente de la verificación final de privacidad y custodia.

## Verificación de la capa restringida

GitHub no puede demostrar que la capa [R] está cifrada porque precisamente esa capa debe estar fuera del repositorio. Antes de cerrar F3-07, un integrante debe confirmar localmente:

- [ ] originales restringidos fuera de la carpeta clonada;
- [ ] almacenamiento restringido cifrado/protegido;
- [ ] acceso limitado a integrantes autorizados;
- [ ] consentimientos originales disponibles para las sesiones que los requieren;
- [ ] audios/videos reales fuera del repositorio público;
- [ ] fotografías F3-01 clasificadas como [P] o [R];
- [x] auditoría automática final ejecutada después de integrar los paquetes públicos.

No se registran en Git contraseñas, claves ni rutas privadas sensibles.
