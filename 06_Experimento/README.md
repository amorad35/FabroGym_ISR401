# 06_Experimento - FabroGym

Esta carpeta contiene el material del componente empirico de la Entrega 3 (2A). El enfoque seleccionado es la deteccion automatica de ambiguedad y malos olores en 25 requisitos funcionales mediante un detector determinista en Python, comparado con el consenso de al menos tres evaluadores independientes.

## Estado actual

- `protocolo.pdf`: preparado.
- Instrumentos de recoleccion v2.7: incorporados.
- Instrumentos de evaluacion experta: preparados.
- Corpus de 25 RF y scripts: preparados.
- Resultados: solo plantillas, sin datos inventados.
- `osf_registration.pdf`: PENDIENTE. Debe obtenerse del registro real en OSF.

Mientras no exista el comprobante oficial, se conserva `PENDIENTE_osf_registration.md`. No debe renombrarse ninguna guia como si fuera el comprobante.

## Estructura

```text
06_Experimento/
├── README.md
├── protocolo.pdf
├── PENDIENTE_osf_registration.md
├── fuentes/
│   └── requisitos_fabrogym_v1.5.8.csv
├── instrumentos/
│   ├── A02_Instrumentos_Recoleccion_v2_7.pdf
│   ├── 01_Guia_Evaluacion_Expertos.pdf
│   ├── 02_Plantilla_Consentimiento_Evaluador.pdf
│   ├── 03_Matriz_Evaluacion_Expertos.csv
│   ├── 04_Rubrica_Evaluacion_Experta.csv
│   ├── 06_Plantilla_Registro_Desacuerdos.csv
│   └── 07_Diccionario_Campos.md
├── prompts_llm/
│   └── README_NO_APLICA.md
├── resultados/
│   ├── README.md
│   ├── plantilla_salida_detector.csv
│   ├── plantilla_consenso_experto.csv
│   └── figuras/
│       └── README.md
└── scripts_analisis/
    ├── README.md
    ├── requirements.txt
    ├── detector_ambiguedad.py
    ├── generar_matrices_evaluacion.py
    ├── preparar_consenso.py
    ├── validar_entradas.py
    ├── analizar_resultados.py
    ├── prueba_sintetica.py
    └── run_all.py
```

## Paso pendiente obligatorio: OSF

1. Registrar realmente el protocolo en OSF antes de ejecutar el experimento real.
2. Exportar o imprimir la pagina oficial del registro.
3. Verificar que muestre URL persistente y sello temporal.
4. Guardarla en esta raiz como `osf_registration.pdf`.
5. Eliminar `PENDIENTE_osf_registration.md`.

## Resultados

No se deben llenar ni generar resultados reales antes del prerregistro OSF. Despues de recopilar las evaluaciones, guardar la matriz completa como `resultados/evaluaciones_expertos.csv` y ejecutar:

```bash
pip install -r scripts_analisis/requirements.txt
python scripts_analisis/run_all.py
```

## Privacidad

Los consentimientos firmados y cualquier dato identificable no se publican aqui. Deben permanecer en `02_Evidencias/00_Restringido/` dentro del contenedor cifrado. En esta carpeta solo se publican instrumentos vacios, codigos y datos anonimizados.
