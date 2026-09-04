# 10_Autoria — Evidencia de autoría y trabajo propio

## 1. Propósito

Esta carpeta reúne la evidencia verificable de autoría, contribución individual y trabajo propio del equipo FabroGym para la Entrega 4 (2B / Defensa Final) de ISR-401.

Su objetivo es permitir que un tercero pueda comprobar, a partir de evidencia real y trazable, quién participó en cada actividad, qué artefactos produjo o revisó, qué decisiones tomó y qué commits del repositorio respaldan esa contribución.

La carpeta `10_Autoria/` no sustituye al historial Git ni a los artefactos técnicos del proyecto. Los complementa con evidencia de proceso, trabajo colaborativo y procedencia.

---

## 2. Principios de integridad

Toda evidencia incorporada en esta carpeta debe cumplir las siguientes reglas:

- corresponder a una actividad real;
- conservar su fecha y procedencia reales;
- no ser retrofechada;
- no ser reconstruida artificialmente para aparentar trabajo previo;
- no contener nombres, firmas, documentos o datos personales de terceros cuando no deban publicarse;
- no declarar sesiones, capturas, grabaciones, fotografías, comunicaciones, codificaciones o firmas que no existan;
- no utilizar archivos vacíos, de relleno o placeholders;
- conservar los identificadores de commit reales cuando se cite trabajo versionado;
- mantener coherencia entre el artefacto, la persona responsable y el historial Git.

Cualquier evidencia que no pueda verificarse de forma independiente no debe presentarse como acreditada.

---

## 3. Estructura de evidencia A1–A12

La evidencia de autoría se organiza conforme a la guía específica de FabroGym.

### A1 — `bitacora_sesiones.csv`

Registro cronológico de las sesiones reales de trabajo del equipo.

Cada fila debe incluir, como mínimo:

- identificador de sesión;
- fecha;
- hora de inicio;
- hora de fin;
- modalidad;
- integrantes participantes;
- usuario Git de cada participante;
- artefacto o ruta trabajada;
- decisiones tomadas;
- commits producidos durante la sesión.

La bitácora debe construirse a partir de actividades y commits verificables. No se crean sesiones ficticias para cubrir días sin evidencia.

### A2 — `capturas/`

Capturas de pantalla utilizadas como evidencia de trabajo individual.

Cada integrante debe aportar capturas reales en las que se observe:

- la herramienta utilizada;
- el archivo o artefacto de FabroGym abierto;
- el reloj o fecha visible del sistema;
- el nombre de la sesión de usuario o identidad de trabajo.

Nomenclatura:

```text
AAAA-MM-DD_usuario_artefacto.png
```

Las capturas deben corresponder al trabajo efectivamente realizado.

### A3 — Fuentes editables de diagramas

Se conservan los archivos fuente editables de los diagramas entregados junto con sus exportaciones utilizadas en el proyecto.

Ejemplos de formatos:

```text
*.vpp
*.drawio
*.puml
*.svg
*.png
```

La imagen exportada no sustituye al archivo editable cuando este exista.

Las fuentes editables deben permanecer vinculadas a los diagramas realmente incorporados en `03_Modelado/` y en la ERS/SRS.

### A4 — `grabaciones/`

Grabaciones reales de sesiones de trabajo colaborativo.

Cada grabación debe mostrar trabajo efectivo sobre FabroGym y permitir identificar:

- edición o revisión de artefactos;
- discusión técnica del equipo;
- decisiones tomadas durante la sesión.

Las grabaciones se conservan únicamente cuando hayan sido producidas durante una sesión efectiva de trabajo.

### A5 — `notas_campo/`

Notas manuscritas o registros de campo reales obtenidos durante actividades de elicitación o validación.

Deben conservar:

- fecha visible;
- relación clara con la sesión correspondiente;
- legibilidad suficiente para su revisión.

No se reconstruyen notas con posterioridad para simular evidencia de una sesión pasada.

### A6 — `fotos_equipo/`

Fotografías reales del equipo durante actividades relacionadas con el proyecto.

Deben conservar sus metadatos originales y respetar las condiciones de privacidad y consentimiento aplicables.

No se modifican los metadatos de captura para alterar fecha, dispositivo o procedencia.

### A7 — `doble_codificacion/`

Evidencia de doble codificación independiente sobre el mismo subconjunto del corpus de walkthroughs.

Debe contener:

- hoja de codificación del primer integrante;
- hoja de codificación del segundo integrante;
- identificación del subconjunto común codificado;
- script utilizado para calcular el acuerdo;
- resultado del coeficiente de acuerdo;
- intervalo de confianza correspondiente.

Las dos codificaciones deben realizarse de forma independiente antes de calcular el acuerdo.

### A8 — `correspondencia/`

Comunicaciones reales y fechadas con la organización relacionadas con el proyecto.

Pueden incluir:

- solicitudes;
- autorizaciones;
- confirmaciones de cita;
- coordinación de sesiones;
- comunicaciones de seguimiento.

Antes de su publicación debe revisarse la presencia de datos personales o información que deba mantenerse restringida.

### A9 — `declaracion_uso_ia.md`

Declaración de uso de herramientas de inteligencia artificial en el proyecto.

Debe indicar, por sección o artefacto relevante:

- herramienta utilizada;
- propósito de uso;
- persona responsable de revisar el resultado;
- método de verificación aplicado;
- secciones en las que no se utilizó IA, cuando corresponda.

El uso de IA no sustituye la responsabilidad académica de los integrantes que firman los artefactos.

### A10 — `aporte_individual.md`

Registro de contribución individual del equipo.

Para cada integrante debe documentarse:

- actividad realizada;
- artefacto o ruta correspondiente;
- rol ejercido;
- commits que acreditan la contribución;
- tipo de participación: autoría, revisión, validación o integración.

Los commits citados deben existir realmente en el historial del repositorio y corresponder al integrante declarado.

La versión de cierre debe ser revisada y firmada por los cinco integrantes declarados del equipo.

### A11 — `exif_inventario.csv`

Inventario técnico de las fotografías utilizadas como evidencia.

Cada registro debe incluir:

- nombre del archivo;
- fecha de captura obtenida de metadatos;
- dispositivo;
- SHA-256;
- observaciones de procedencia cuando sean necesarias.

El inventario se genera a partir de los archivos originales, sin alterar sus metadatos.

### A12 — `.mailmap`

La evidencia A12 se mantiene en la raíz del repositorio:

```text
/.mailmap
```

Su función es unificar las identidades históricas de Git con los nombres y correos institucionales de los integrantes declarados.

No debe crearse una segunda copia independiente dentro de `10_Autoria/`.

---

## 4. Relación con el historial Git

El historial Git constituye evidencia central de autoría.

Para cada contribución citada en A1 o A10 deben utilizarse hashes de commit reales.

Reglas:

- cada integrante realiza sus commits con su identidad real;
- se utiliza correo institucional;
- no se atribuyen a una persona commits realizados por otra;
- no se reescribe el historial para fabricar distribución de trabajo;
- los mensajes de commit deben describir el cambio realizado.

La evidencia documental de `10_Autoria/` debe ser consistente con el historial Git.

---

## 5. Contribución individual y defensa

La contribución individual no se acredita únicamente mediante una declaración escrita.

Debe poder demostrarse mediante una combinación verificable de:

- commits;
- artefactos producidos o revisados;
- sesiones registradas;
- capturas;
- fuentes editables;
- evidencia de revisión;
- participación en la defensa.

Cada integrante debe poder explicar técnicamente los artefactos y decisiones que se le atribuyen.

---

## 6. Privacidad y publicación

`10_Autoria/` contiene evidencia del trabajo del equipo, no evidencia personal de participantes del estudio.

Antes de incorporar cualquier archivo se debe comprobar que no publique indebidamente:

- cédulas;
- firmas de terceros;
- teléfonos;
- correos privados;
- direcciones;
- credenciales;
- datos biométricos;
- información restringida del gimnasio;
- evidencia identificable de participantes sin autorización.

Cuando una evidencia legítima contenga información que no deba ser pública, se conserva en la zona restringida correspondiente y en `10_Autoria/` se documenta únicamente la referencia verificable permitida.

---

## 7. Verificación previa al cierre

Antes de la entrega final, una persona del equipo distinta de quien produjo cada artefacto debe revisar la evidencia de autoría.

La comprobación final debe verificar:

1. que `10_Autoria/` contiene evidencia real para A1–A11 y que A12 se referencia correctamente desde `/.mailmap`;
2. que no existen archivos vacíos o placeholders;
3. que las fechas y metadatos no han sido alterados;
4. que los commits citados existen;
5. que los autores de los commits corresponden a integrantes declarados;
6. que las rutas citadas existen;
7. que la doble codificación conserva las dos hojas independientes y el cálculo reproducible;
8. que las fotografías conservan los metadatos originales requeridos;
9. que la declaración de uso de IA cubre los artefactos correspondientes;
10. que la contribución individual puede demostrarse documentalmente y durante la defensa.

La verificación firmada de cierre se incorpora como:

```text
10_Autoria/verificacion_previa.pdf
```

---

## 8. Regla de incorporación de evidencia

Esta carpeta se construye únicamente con evidencia real generada durante el desarrollo y cierre de FabroGym.

No se crean carpetas o archivos vacíos únicamente para completar visualmente A1–A12.

Cada elemento se incorpora únicamente cuando existe evidencia verificable y puede mantenerse íntegro hasta la versión final del repositorio.
