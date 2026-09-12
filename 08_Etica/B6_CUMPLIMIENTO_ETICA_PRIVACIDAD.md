# B6 — Cumplimiento de ética y protección de datos

**Proyecto:** FabroGym — ISR-401  
**Entrega:** Entrega 4 (2B / Defensa Final)

## 1. Matriz de cumplimiento

| Requisito | Evidencia / decisión |
|---|---|
| **Base de licitud / fundamento de participación** | Participación voluntaria y consentimiento informado para la evidencia primaria de campo. |
| **Finalidad** | Uso académico para levantamiento, análisis, especificación y validación de requisitos, trazabilidad, reproducibilidad y publicación anonimizada. |
| **Plazo de conservación** | Las copias restringidas o reidentificables se mantienen únicamente durante el periodo autorizado para el proyecto/evaluación y, cuando corresponda, bajo custodia institucional. |
| **Responsable de custodia académica** | Equipo actual de cierre: Mera Arias Erick Jhair, Mora Duarte Alex José y Ponce Rivera Mery Helenmey, bajo supervisión académica del docente responsable. |

## 2. Separación pública / restringida

**[P] Pública:** transcripciones anonimizadas, matrices, resultados, requisitos, modelado, scripts, datos derivados y copias censuradas/enmascaradas aptas para publicación.

**[R] Restringida:** originales identificables, consentimientos firmados, grabaciones, fotografías originales no aptas para publicación y demás material con datos personales directos.

La guía específica de FabroGym exige mantener una **capa restringida cifrada** y una capa pública derivada sin datos personales.

## 3. Contenedor restringido documentado

Se conserva deliberadamente:

`02_Evidencias/00_Restringido/evidencias_restringidas.7z`

Su presencia no significa que los datos contenidos se publiquen en claro. Para que sea válido en el cierre:

- debe permanecer cifrado/protegido;
- la contraseña/clave debe mantenerse fuera del repositorio;
- sus originales no deben extraerse a rutas públicas;
- Zenodo y `07_Datos/` deben contener solo derivados aptos para publicación.

También se conserva `02_Evidencias/00_Restringido/fichas_tecnicas.csv` como inventario técnico de evidencia, sin sustituir ni exponer los archivos originales.

## 4. Fotografías A11

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` se trata como contenedor restringido. Solo puede permanecer versionado si está cifrado/protegido y la clave no está en Git. Las copias públicas deben estar autorizadas o enmascaradas.

## 5. Regla de minimización

FabroGym no publica en la capa [P]:

- cédulas;
- firmas originales;
- teléfonos o correos privados;
- datos reales de salud;
- biometría;
- medidas corporales identificables;
- pagos reales asociados a personas;
- historiales clínicos;
- originales identificables no autorizados.

## 6. Verificación de cierre

Ejecutar:

```bash
python 07_Datos/scripts/verificar_privacidad_publica.py
```

El resultado automático debe quedar sin hallazgos bloqueantes. Además, antes del tag final el equipo debe confirmar manualmente el cifrado de los contenedores restringidos y revisar visualmente las piezas públicas.

**Estado documental:** INTEGRADO Y VERSIONADO EN EL REPOSITORIO.  
**Estado de cierre:** sujeto únicamente a la ejecución final del verificador y a las confirmaciones humanas de cifrado/privacidad antes del tag.
