# A7 — Doble codificación de walkthroughs

## Cobertura

- Corpus total: 76 fragmentos.
- Subconjunto común: 16 fragmentos.
- Cobertura: 21,05 %.
- Campo principal para el acuerdo: `Categoria`.
- Campo secundario de diagnóstico: `Codigo_Axial`.
- Coeficiente: Cohen's kappa.
- Intervalo de confianza: IC95 % mediante bootstrap percentil con semilla reproducible.

## Archivos

- `01_subconjunto_congelado_16_de_76.csv`: subconjunto común de 16 fragmentos.
- `02_codificacion_mora.xlsx` / `.csv`: hoja de revisión asignada a Mora.
- `03_codificacion_ponce.xlsx` / `.csv`: hoja de revisión asignada a Ponce.
- `calcular_kappa_ic.py`: script reproducible para calcular kappa e IC95 %.
- `resultado_kappa_categoria.csv`: resultado principal.
- `resultado_kappa_categoria_detalle.csv`: acuerdo/desacuerdo por fragmento.
- `resultado_kappa_codigo_axial.csv`: análisis secundario.
- `resultado_kappa_codigo_axial_detalle.csv`: detalle secundario.

## Procedimiento

Las dos hojas usan el mismo subconjunto de 16 fragmentos. Para que estas hojas puedan acreditarse como evidencia A7 producida por los dos integrantes, cada integrante debe revisar y confirmar personalmente la hoja que le corresponde antes de incorporarla como evidencia propia al repositorio.

El cálculo de acuerdo no se escribe a mano. Se reproduce con:

```bash
python calcular_kappa_ic.py 02_codificacion_mora.csv 03_codificacion_ponce.csv --campo Categoria --salida resultado_kappa_categoria.csv
python calcular_kappa_ic.py 02_codificacion_mora.csv 03_codificacion_ponce.csv --campo Codigo_Axial --salida resultado_kappa_codigo_axial.csv
```

La selección del subconjunto se fijó antes del cálculo de kappa y cubre las seis sesiones de walkthrough.
