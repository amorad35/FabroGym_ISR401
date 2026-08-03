#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys

HERE=Path(__file__).resolve().parent
for script in ["validar_dataset.py","analizar_encuestas.py","analizar_codificacion.py"]:
    print(f"\n== {script} ==")
    subprocess.run([sys.executable,str(HERE/script)],check=True)
print("\nAnálisis reproducido correctamente.")
