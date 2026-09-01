# REPRODUCIBILITY

## Environment
Recommended: Python 3.11+.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
# source .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/run_all.py
```

## Expected headline outputs
A successful run must reproduce:
- questionnaire n=70;
- 16 session metadata records;
- total video duration 06:18:08 and audio duration 06:18:14;
- 76 coded walkthrough fragments;
- 37 normalized codes;
- 18 thematic categories;
- 9 explainability-pertinent fragments;
- 4 final `RNF-EXP` requirements;
- member checking: 4 Confirmado, 8 Ajustado, 0 No confirmado;
- strict code-saturation value 6.306% (therefore not <=5%).

No inferential result is introduced where the empirical instrument lacks the necessary variable or repeated rating structure.


## Corpus ENTR histórico
La carpeta `codificacion/entrevistas_generales/` conserva la codificación temática de las 10 entrevistas iniciales (59 fragmentos). Se incluye para auditabilidad de la elicitación y trazabilidad. `scripts/run_all.py` reproduce el análisis terminal basado en los seis walkthroughs; no mezcla el corpus ENTR con el corpus WALK para producir las cifras del manuscrito.
