# Registro de prompts LLM - no aplicable al diseño base

El Enfoque 2 seleccionado utiliza un detector determinista en Python con expresiones regulares. No se utiliza un LLM para clasificar los requisitos; por ello no existen prompt, temperatura, top-p, top-k ni semilla de generación que registrar.

La carpeta se conserva para respetar el árbol obligatorio y dejar documentada la no aplicabilidad.

Si antes del prerregistro el equipo decide incorporar un LLM, debe actualizar el protocolo, la adenda ética y el registro OSF. Cada ejecución deberá documentarse en un archivo Markdown con:

- prompt exacto;
- modelo y versión;
- temperatura, top-p y top-k;
- semilla, cuando la plataforma la permita;
- fecha y hora;
- material de entrada anonimizado;
- respuesta completa;
- responsable de la ejecución.

Después de observar resultados no se puede cambiar el método sin declarar una desviación del prerregistro.
