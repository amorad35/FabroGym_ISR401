#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FabroGym — F3-04
Tamaño del efecto + IC95% para comparación técnico vs no técnico.

Entrada canónica:
datos_crudos/comparacion_perfiles_walkthroughs_fuente.csv

Unidad de análisis:
la misma categoría temática observada en ambos perfiles (pares).

Medida:
correlación biserial por rangos pareada (r_rb).

Intervalo:
bootstrap percentil 95%, 10 000 réplicas, semilla reproducible.

Alcance:
descriptivo-exploratorio. No genera p-valores ni afirma diferencias
poblacionales a partir de solo tres walkthroughs por perfil.
"""

from pathlib import Path
import argparse
import csv
import random
import math


def rank_average(values):
    """Rangos promedio para empates. Entrada: lista de valores >= 0."""
    indexed = sorted(enumerate(values), key=lambda x: x[1])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(indexed):
        j = i
        while j + 1 < len(indexed) and indexed[j + 1][1] == indexed[i][1]:
            j += 1
        avg_rank = ((i + 1) + (j + 1)) / 2.0
        for k in range(i, j + 1):
            ranks[indexed[k][0]] = avg_rank
        i = j + 1
    return ranks


def paired_rank_biserial(x, y):
    """r_rb pareada basada en rangos de |x-y|; ceros se excluyen."""
    diffs = [float(a) - float(b) for a, b in zip(x, y)]
    nz = [d for d in diffs if d != 0]
    if not nz:
        return 0.0
    ranks = rank_average([abs(d) for d in nz])
    w_pos = sum(r for r, d in zip(ranks, nz) if d > 0)
    w_neg = sum(r for r, d in zip(ranks, nz) if d < 0)
    denom = w_pos + w_neg
    return 0.0 if denom == 0 else (w_pos - w_neg) / denom


def quantile(sorted_values, p):
    if not sorted_values:
        raise ValueError("No hay valores para calcular cuantiles.")
    pos = (len(sorted_values) - 1) * p
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return sorted_values[lo]
    frac = pos - lo
    return sorted_values[lo] * (1 - frac) + sorted_values[hi] * frac


def bootstrap_ci(x, y, reps=10000, seed=4012026):
    rng = random.Random(seed)
    n = len(x)
    vals = []
    for _ in range(reps):
        idx = [rng.randrange(n) for __ in range(n)]
        xb = [x[i] for i in idx]
        yb = [y[i] for i in idx]
        vals.append(paired_rank_biserial(xb, yb))
    vals.sort()
    return quantile(vals, 0.025), quantile(vals, 0.975)


def read_source(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required = {
        "Categoria",
        "Sesiones_Tecnicas_que_mencionan",
        "Sesiones_NoTecnicas_que_mencionan",
        "Fragmentos_Tecnicos",
        "Fragmentos_NoTecnicos",
    }
    if not rows:
        raise SystemExit("F3-04: el archivo fuente está vacío.")
    missing = sorted(required.difference(rows[0].keys()))
    if missing:
        raise SystemExit(f"F3-04: faltan columnas: {missing}")
    return rows


def main():
    root = Path(__file__).resolve().parents[1]
    default_in = root / "datos_crudos" / "comparacion_perfiles_walkthroughs_fuente.csv"
    default_out = root / "resultados" / "tablas" / "tabla_efecto_perfiles.csv"
    default_detail = root / "resultados" / "tablas" / "tabla_efecto_perfiles_detalle.csv"
    default_md = root / "resultados" / "F3-04_TAMANIO_EFECTO.md"

    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", default=str(default_in))
    ap.add_argument("--salida", default=str(default_out))
    ap.add_argument("--detalle", default=str(default_detail))
    ap.add_argument("--resumen-md", default=str(default_md))
    ap.add_argument("--bootstrap", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=4012026)
    args = ap.parse_args()

    source = Path(args.entrada)
    rows = read_source(source)
    if len(rows) != 18:
        raise SystemExit(
            f"F3-04: se esperaban 18 categorías del archivo canónico; se encontraron {len(rows)}."
        )

    comparisons = [
        (
            "Presencia de categorias por sesiones",
            "Sesiones_Tecnicas_que_mencionan",
            "Sesiones_NoTecnicas_que_mencionan",
        ),
        (
            "Fragmentos codificados por categoria",
            "Fragmentos_Tecnicos",
            "Fragmentos_NoTecnicos",
        ),
    ]

    summary = []
    detail_rows = []

    for label, col_t, col_nt in comparisons:
        x = [float(r[col_t]) for r in rows]
        y = [float(r[col_nt]) for r in rows]
        effect = paired_rank_biserial(x, y)
        ci_lo, ci_hi = bootstrap_ci(x, y, args.bootstrap, args.seed)
        diffs = [a - b for a, b in zip(x, y)]

        summary.append({
            "comparacion": label,
            "unidad_analisis": "Categoria tematica pareada",
            "n_categorias": len(rows),
            "sesiones_por_perfil": 3,
            "medida_efecto": "Correlacion biserial por rangos pareada",
            "efecto_r_rb": f"{effect:.6f}",
            "IC95_bootstrap_inf": f"{ci_lo:.6f}",
            "IC95_bootstrap_sup": f"{ci_hi:.6f}",
            "bootstrap_replicas": args.bootstrap,
            "seed": args.seed,
            "media_diferencia_Tec_menos_NoTec": f"{sum(diffs)/len(diffs):.6f}",
            "mediana_diferencia_Tec_menos_NoTec": f"{sorted(diffs)[len(diffs)//2-1]/2 + sorted(diffs)[len(diffs)//2]/2:.6f}",
            "categorias_Tec_mayor": sum(d > 0 for d in diffs),
            "categorias_NoTec_mayor": sum(d < 0 for d in diffs),
            "categorias_iguales": sum(d == 0 for d in diffs),
            "direccion": "Positivo = mayor presencia/conteo en perfil tecnico",
            "alcance": "Descriptivo-exploratorio; 3 sesiones por perfil; no implica diferencia poblacional."
        })

        for row, tv, ntv, d in zip(rows, x, y, diffs):
            detail_rows.append({
                "comparacion": label,
                "Categoria": row["Categoria"],
                "valor_tecnico": f"{tv:.0f}",
                "valor_no_tecnico": f"{ntv:.0f}",
                "diferencia_Tec_menos_NoTec": f"{d:.0f}",
                "direccion_categoria": (
                    "Tecnico_mayor" if d > 0 else
                    "No_tecnico_mayor" if d < 0 else
                    "Igual"
                )
            })

    out = Path(args.salida)
    detail = Path(args.detalle)
    md = Path(args.resumen_md)
    out.parent.mkdir(parents=True, exist_ok=True)
    detail.parent.mkdir(parents=True, exist_ok=True)
    md.parent.mkdir(parents=True, exist_ok=True)

    summary_headers = list(summary[0].keys())
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=summary_headers)
        w.writeheader()
        w.writerows(summary)

    detail_headers = list(detail_rows[0].keys())
    with detail.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=detail_headers)
        w.writeheader()
        w.writerows(detail_rows)

    a, b = summary
    md.write_text(
        f"""# F3-04 — Tamaño del efecto técnico vs no técnico

## Fuente de datos

`datos_crudos/comparacion_perfiles_walkthroughs_fuente.csv`

La fuente resume las 18 categorías temáticas identificadas en los seis walkthroughs:
tres sesiones técnicas y tres no técnicas.

## Método

La misma categoría se compara entre ambos perfiles, por lo que las 18 categorías se tratan como pares.
Se utiliza la **correlación biserial por rangos pareada (`r_rb`)** como tamaño del efecto.

El intervalo de confianza del 95 % se obtiene mediante **bootstrap percentil de {args.bootstrap} réplicas**
con semilla reproducible `{args.seed}`.

## Resultados

- Presencia de categorías por sesiones:
  `r_rb = {a["efecto_r_rb"]}`, IC95% `[{a["IC95_bootstrap_inf"]}, {a["IC95_bootstrap_sup"]}]`.
- Fragmentos codificados por categoría:
  `r_rb = {b["efecto_r_rb"]}`, IC95% `[{b["IC95_bootstrap_inf"]}, {b["IC95_bootstrap_sup"]}]`.

Un valor positivo indica una tendencia a mayor presencia o conteo en el perfil técnico.

## Alcance y limitación

Este resultado es **descriptivo-exploratorio**. Solo existen tres walkthroughs por perfil.
La unidad de este cálculo es la categoría temática pareada; no es una puntuación independiente por participante.
Por ello no se genera p-valor ni se afirma una diferencia poblacional.

## Reproducibilidad

Desde la raíz de `06_Experimento/`:

```bash
python scripts_analisis/calcular_efecto_perfiles.py
```

Desde la raíz de `07_Datos/`:

```bash
python scripts/calcular_efecto_perfiles.py
```

Los resultados se generan automáticamente en `resultados/tablas/`.
""",
        encoding="utf-8"
    )

    print(f"OK F3-04: {len(rows)} categorías")
    for r in summary:
        print(
            f"{r['comparacion']}: r_rb={r['efecto_r_rb']}, "
            f"IC95=[{r['IC95_bootstrap_inf']}, {r['IC95_bootstrap_sup']}]"
        )
    print(f"Tabla: {out}")
    print(f"Detalle: {detail}")
    print(f"Resumen: {md}")


if __name__ == "__main__":
    main()
