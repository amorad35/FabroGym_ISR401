#!/usr/bin/env python3
import argparse
import csv
import random
from collections import Counter
from pathlib import Path

def normalizar(v):
    return (v or "").strip().casefold()

def leer(path, campo):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit(f"{path}: archivo sin datos")
    for col in ("ID_Registro", campo):
        if col not in rows[0]:
            raise SystemExit(f"{path}: falta columna {col}")
    out = {}
    for r in rows:
        rid = r["ID_Registro"].strip()
        lab = normalizar(r[campo])
        if not lab:
            raise SystemExit(f"{path}: {campo} vacío en {rid}")
        if rid in out:
            raise SystemExit(f"{path}: ID duplicado {rid}")
        out[rid] = lab
    return out

def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    etiquetas = set(ca) | set(cb)
    pe = sum((ca[e]/n)*(cb[e]/n) for e in etiquetas)
    val = (po-pe)/(1-pe) if abs(1-pe) > 1e-15 else float("nan")
    return po, pe, val

def percentil(vals, p):
    vals = sorted(v for v in vals if v == v)
    pos = (len(vals)-1)*p
    lo = int(pos)
    hi = min(lo+1, len(vals)-1)
    f = pos-lo
    return vals[lo]*(1-f)+vals[hi]*f

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("hoja_mora")
    ap.add_argument("hoja_ponce")
    ap.add_argument("--campo", default="Categoria")
    ap.add_argument("--bootstrap", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=4012026)
    ap.add_argument("--salida", default=None)
    args = ap.parse_args()

    A = leer(args.hoja_mora, args.campo)
    B = leer(args.hoja_ponce, args.campo)
    if set(A) != set(B):
        raise SystemExit("Las dos hojas no contienen exactamente el mismo subconjunto")

    ids = sorted(A)
    aa = [A[i] for i in ids]
    bb = [B[i] for i in ids]
    po, pe, kap = kappa(aa, bb)

    rng = random.Random(args.seed)
    boots = []
    n = len(ids)
    for _ in range(args.bootstrap):
        idx = [rng.randrange(n) for _ in range(n)]
        _, _, kb = kappa([aa[i] for i in idx], [bb[i] for i in idx])
        if kb == kb:
            boots.append(kb)

    lo = percentil(boots, .025)
    hi = percentil(boots, .975)
    stem = args.campo.strip().lower().replace(" ", "_")
    out = Path(args.salida or f"resultado_kappa_{stem}.csv")
    detalle = out.with_name(out.stem + "_detalle.csv")

    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Campo","N","Acuerdo_observado","Acuerdo_esperado","Kappa","IC95_inferior","IC95_superior","Bootstrap","Seed"])
        w.writerow([args.campo,n,f"{po:.6f}",f"{pe:.6f}",f"{kap:.6f}",f"{lo:.6f}",f"{hi:.6f}",len(boots),args.seed])

    with detalle.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID_Registro",f"{args.campo}_Mora",f"{args.campo}_Ponce","Acuerdo"])
        for rid in ids:
            w.writerow([rid,A[rid],B[rid],"SI" if A[rid] == B[rid] else "NO"])

    print(f"N={n}")
    print(f"Acuerdo observado={po:.4f}")
    print(f"Acuerdo esperado={pe:.4f}")
    print(f"Kappa={kap:.4f}")
    print(f"IC95%=[{lo:.4f}, {hi:.4f}]")
    print(f"Resultado={out}")
    print(f"Detalle={detalle}")

if __name__ == "__main__":
    main()
