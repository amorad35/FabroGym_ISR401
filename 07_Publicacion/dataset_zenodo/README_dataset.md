# Dataset FabroGym - Entrega 3 (2A)

## 1. Descripción

Conjunto de datos anonimizado y material reproducible del proyecto FabroGym, desarrollado en Ingeniería de Requerimientos (ISR-401), Universidad Técnica Estatal de Quevedo.

El paquete documenta la transformación de evidencia empírica de un dominio de gestión de gimnasios en requisitos trazables. No contiene datos clínicos, biometría, peso, medidas corporales, imágenes de participantes, voz, firmas, cédulas ni claves de reidentificación.

## 2. Estado del depósito

- **Versión del paquete:** 1.0
- **Fecha:** 2026-08-02
- **DOI:** pendiente
- **Zenodo:** pendiente de depósito
- **OSF:** pendiente de registro definitivo
- **Licencia prevista:** CC BY 4.0

No debe inventarse ni anticiparse un DOI.

## 3. Fuentes de datos

### Entrevistas

- 10 transcripciones anonimizadas.
- 59 fragmentos analíticos codificados.
- 16 códigos temáticos.
- 2 memos o restricciones éticas/de diseño.
- La curva de códigos es descriptiva y no demuestra saturación teórica.

`transcripciones_anonimizadas.json` indexa las rutas públicas de las diez transcripciones y contiene los fragmentos codificados. Los textos completos permanecen en `02_Evidencias/Transcripciones/` para evitar duplicación de versiones.

### Cuestionario

- 32 respuestas anonimizadas.
- 32 consentimientos electrónicos afirmativos.
- 4 respuestas de pilotaje incluidas.
- IDs seudónimos `ENC-CLI-001` a `ENC-CLI-032`.
- Muestreo no probabilístico; los resultados son descriptivos.

### Requisitos

- 25 requisitos funcionales.
- 15 requisitos no funcionales.
- 4 restricciones.
- 44 identificadores únicos en trazabilidad.

## 4. Estructura

```text
dataset_zenodo/
├── README_dataset.md
├── LICENSE_DATASET.txt
├── CITATION.cff
├── metadatos_encuesta.json
├── respuestas_cuestionario.csv
├── diccionario_variables.csv
├── transcripciones_anonimizadas.json
├── codificacion_tematica.csv
├── diccionario_codigos.csv
├── corpus_requisitos.json
├── matriz_trazabilidad.csv
├── priorizacion_moscow_kano_wsjf.csv
├── resultados/
│   ├── estadisticas_descriptivas.json
│   ├── resumen_encuesta.json
│   ├── frecuencias_encuesta.csv
│   ├── frecuencias_codigos.csv
│   ├── curva_saturacion.csv
│   └── figuras/
├── scripts_analisis/
└── fuentes/
```

## 5. Diccionario resumido

- `id_respuesta`: identificador seudónimo de encuesta.
- `consentimiento`: confirmación de participación adulta y voluntaria.
- `frecuencia_asistencia`: frecuencia declarada de asistencia.
- `consulta_membresia`: medio actual de consulta de membresía.
- `medio_preferido_avisos`: canal preferido para avisos.
- `prioridad_mejora`: proceso que debería mejorarse primero.
- `importancia_privacidad`: valoración ordinal sobre privacidad.
- `ID-EV`: identificador de evidencia.
- `RF`, `RNF`, `RD`: requisito funcional, no funcional y restricción.
- `ID-CU`, `ID-HU`, `ID-CA`: caso de uso, historia y criterio de aceptación.

El detalle completo está en `diccionario_variables.csv` y `diccionario_codigos.csv`.

## 6. Reproducción

Requisitos:

- Python 3.10 o superior.
- `matplotlib`.

Ejecución:

```bash
python scripts_analisis/run_all.py
```

Los scripts validan la estructura, recalculan frecuencias y generan figuras sin alterar los archivos fuente.

## 7. Anonimización

Se eliminaron nombres, marcas de tiempo, firmas, cédulas y columnas identificativas. Los códigos de participante no permiten por sí solos recuperar la identidad. Los archivos originales y la tabla de correspondencia, si existiera, permanecen en zona restringida y no forman parte del paquete.

## 8. Limitaciones

1. La muestra cuantitativa es pequeña, no probabilística y contiene cuatro registros de pilotaje.
2. Las respuestas abiertas no se interpretan como una segunda codificación temática cerrada en esta versión.
3. La curva de códigos no prueba saturación de significado.
4. Las validaciones walkthrough y las pruebas del MVP aún no se han ejecutado.
5. El estudio corresponde a un contexto académico y no demuestra efectividad del software en producción.

## 9. Citación sugerida antes del DOI

Alvia Villegas, E. A., Mera Arias, E. J., Mora Duarte, A. J., Ponce Rivera, M. H., & Vaca Romero, D. O. (2026). *FabroGym: conjunto de datos anonimizado para ingeniería de requisitos en la gestión de gimnasios* (Versión 1.0) [Conjunto de datos]. Universidad Técnica Estatal de Quevedo. https://github.com/amorad35/FabroGym_ISR401

Después del depósito, reemplazar la URL por el DOI asignado por Zenodo.

## 10. Contacto

Los correos institucionales y la persona autora de correspondencia deben confirmarse antes del envío o depósito.
