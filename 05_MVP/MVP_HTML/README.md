# FabroGym — Producto Mínimo Viable (MVP)

## 1. Descripción

FabroGym es un Producto Mínimo Viable desarrollado como una aplicación web estática para demostrar los principales procesos administrativos y operativos de un gimnasio.

El MVP fue implementado con **HTML5, CSS3 y JavaScript**, utiliza datos completamente sintéticos y almacena temporalmente la información en el navegador mediante `localStorage`. No requiere una base de datos externa, servidor de aplicaciones ni instalación de Docker para su ejecución básica.

## 2. Propósito de esta carpeta

La carpeta `05_MVP/` contiene los artefactos necesarios para evidenciar el funcionamiento del MVP en la Entrega 3 (2A):

```text
05_MVP/
├── README.md
├── video_demo.mp4
└── MVP_HTML/
    ├── index.html
    ├── styles.css
    └── app.js
```

> **Nota:** La rúbrica solicita que el código fuente del MVP se aloje también en un repositorio Git público separado. Antes del corte, debe añadirse en la siguiente sección la URL definitiva de dicho repositorio.

## 3. Repositorios

- **Repositorio principal del proyecto:**  
  https://github.com/amorad35/FabroGym_ISR401

- **Código fuente disponible en este repositorio:**  
  `05_MVP/MVP_HTML/`

- **Repositorio Git público separado del MVP:**  
  `REEMPLAZAR_CON_LA_URL_DEL_REPOSITORIO_FabroGym_MVP`

## 4. Ejecución local

### 4.1 Método principal: abrir `index.html`

Debido a que FabroGym es una aplicación web estática, su ejecución local se realiza mediante un procedimiento equivalente a un despliegue con contenedores:

1. Descargar o clonar el repositorio.
2. Abrir la carpeta `05_MVP/MVP_HTML/`.
3. Hacer doble clic en el archivo `index.html`.
4. Seleccionar Chrome, Microsoft Edge o Firefox.
5. Utilizar las credenciales de demostración.

No es obligatorio instalar Docker para este método.

### 4.2 Método alternativo: servidor local de Python

En caso de que el navegador restrinja alguna función al abrir archivos locales, ejecutar desde la carpeta `MVP_HTML/`:

```bash
python -m http.server 8080
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

## 6. Funcionalidades implementadas

El MVP permite demostrar los siguientes procesos:

- Autenticación de usuarios.
- Aplicación de permisos según el rol.
- Registro mínimo de clientes.
- Búsqueda y consulta de clientes.
- Actualización o reactivación de clientes.
- Consulta de vigencia de membresías.
- Renovación de membresías.
- Alertas de vencimiento.
- Registro de asistencias.
- Prevención de asistencias duplicadas.
- Consulta del historial de asistencias.
- Administración básica de rutinas.
- Registro del seguimiento de rutinas.

## 7. Cobertura de requisitos funcionales Must

La priorización vigente identifica **19 requisitos funcionales Must**. El MVP implementa **12 requisitos**, alcanzando una cobertura de:

```text
12 / 19 × 100 = 63,2 %
```

Por tanto, la cobertura supera el mínimo del 60 % requerido para el MVP.

| ID | Requisito funcional | Estado |
|---|---|---|
| RF-AUT-01 | Autenticar usuario | Implementado |
| RF-AUT-02 | Aplicar permisos por rol | Implementado |
| RF-CLI-01 | Registrar cliente mínimo | Implementado |
| RF-CLI-02 | Buscar y consultar cliente | Implementado |
| RF-CLI-03 | Actualizar o reactivar cliente | Implementado |
| RF-MEM-02 | Activar o renovar membresía | Implementado |
| RF-MEM-03 | Consultar vigencia | Implementado |
| RF-MEM-04 | Alertar vencimientos | Implementado |
| RF-ASI-01 | Registrar asistencia | Implementado |
| RF-ASI-02 | Consultar asistencia | Implementado |
| RF-RUT-01 | Administrar rutinas | Implementado |
| RF-RUT-02 | Registrar seguimiento | Implementado |

## 8. Video de demostración

- **Archivo:** `video_demo.mp4`
- **Ubicación:** `05_MVP/video_demo.mp4`
- **Duración máxima permitida:** 3 minutos.
- **Contenido:** recorrido funcional del sistema.
- **Datos utilizados:** exclusivamente ficticios.
- **Método de ejecución mostrado:** apertura directa del archivo `index.html`.

El video debe mostrar, como mínimo:

1. Apertura del archivo `index.html`.
2. Inicio de sesión.
3. Panel principal.
4. Registro y búsqueda de un cliente ficticio.
5. Consulta y renovación de membresía.
6. Registro y consulta de asistencia.
7. Creación de una rutina.
8. Registro de seguimiento.
9. Porcentaje de cobertura de requisitos Must.

## 9. Persistencia de datos

La aplicación utiliza `localStorage` para mantener los datos de demostración dentro del navegador.

Esto implica que:

- Los datos permanecen en el navegador después de recargar la página.
- No existe conexión con una base de datos externa.
- Los datos pueden eliminarse mediante la opción **Restablecer demo** o limpiando el almacenamiento local del navegador.
- La información almacenada tiene únicamente fines académicos y demostrativos.

## 10. Privacidad y ética

El MVP no utiliza información real de clientes, participantes o establecimientos.

Durante la demostración deben usarse únicamente datos ficticios, por ejemplo:

```text
Nombre: Usuario Demostración
Identificación: 0999999999
Teléfono: 0990000000
Plan: Mensual
```

No deben registrarse ni mostrarse:

- Nombres reales.
- Cédulas reales.
- Números telefónicos reales.
- Datos biométricos.
- Fotografías de clientes.
- Información médica o de salud.
- Comprobantes bancarios reales.
- Contraseñas de servicios reales.

## 11. Tecnologías utilizadas

- HTML5.
- CSS3.
- JavaScript.
- `localStorage`.
- Navegadores compatibles: Chrome, Microsoft Edge y Firefox.

## 12. Limitaciones del MVP

Esta versión tiene alcance demostrativo y académico. Por tanto:

- No emplea una base de datos persistente.
- No incluye facturación electrónica.
- No se integra con bancos ni servicios externos.
- No utiliza reconocimiento biométrico.
- No procesa datos médicos o de salud.
- No incorpora inteligencia artificial.
- No representa todavía una versión preparada para producción.

## 13. Equipo responsable

**Equipo FabroGym**

- Alvia Villegas Erick Adalberto.
- Mera Arias Erick Jhair.
- Mora Duarte Alex José.
- Ponce Rivera Mery Helenmey.
- Vaca Romero David Octavio.

## 14. Licencia

El código fuente del MVP debe publicarse bajo licencia **MIT** o **Apache-2.0**, conforme al alcance definido para el repositorio.

La licencia no comprende evidencias restringidas, consentimientos originales, audios, videos de entrevistas ni información identificable del trabajo de campo.
