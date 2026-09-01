# FabroGym 2B — Replication Package

## Dataset title
**Replication package for Explainability Requirements for Fitness Routine Recommendations: A Field Case Study in Ecuador**

## Release status
This package is the final public replication package associated with Zenodo DOI **10.5281/zenodo.22237884**. It contains the anonymized materials required to reproduce the empirical results and inspect the requirements-engineering traceability.

## Study scope
FabroGym is a requirements-engineering field case study in the local-gym domain. The empirical focus is explainability as a non-functional requirement for a **proposed** fitness-routine recommendation component. The recommendation/AI component is not presented as implemented in the MVP.

Stable identifiers preserved in the package:
- `ENTR-01` … `ENTR-10`: 10 initial semi-structured interviews.
- `WALK-NTEC-01` … `WALK-NTEC-03`: 3 non-technical walkthroughs.
- `WALK-TEC-01` … `WALK-TEC-03`: 3 technical walkthroughs.
- `MC-P01`, `MC-P02`, `MC-P03`: member-checking respondents.

All **16 anonymized session transcripts** are included under `transcripciones/`.

## Primary reproducible facts
- 16 accumulated audiovisual session records in the technical table.
- Total video duration: **06:18:08**; total audio duration: **06:18:14**.
- Client questionnaire: **n=70**; no technical/non-technical profile field and no explainability Likert scale.
- General interview coding (`ENTR-01..10`): **59 coded fragments** supporting elicitation and requirement consolidation.
- Walkthrough coding: **76 coded fragments**; 49 technical and 27 non-technical, used for the terminal explainability analysis.
- **37 normalized codes** and **18 thematic categories**.
- **9 explainability-pertinent fragments**.
- **4 final explainability RNFs**: `RNF-EXP-01` … `RNF-EXP-04`.
- Member checking: **12 decisions** (4 Confirmado, 8 Ajustado, 0 No confirmado).
- Strict code-saturation criterion over the last three WALK sessions: **6.306%**; the <=5% threshold is **not claimed as met**.
- Axial-category stabilization: **1.852%**, reported only as complementary evidence.

## Package structure
```text
dataset_zenodo/
├── README_dataset.md
├── DATA_DICTIONARY.md
├── REPRODUCIBILITY.md
├── ANONYMIZATION.md
├── ETHICS.md
├── LICENSE_DATASET.txt
├── CITATION.cff
├── VERSION.txt
├── ZENODO_METADATA_READY.md
├── ZENODO_METADATA_READY.json
├── MANIFEST.csv
├── checksums.sha256
├── transcripciones/
│   ├── entrevistas/          # ENTR-01 .. ENTR-10
│   └── walkthroughs/         # 3 WALK-NTEC + 3 WALK-TEC
├── encuesta/
├── requisitos/
├── trazabilidad/
├── codificacion/
│   ├── entrevistas_generales/ # 59 coded ENTR fragments + dictionary + descriptive curve
│   └── [walkthrough files]    # 76 WALK fragments + explainability/member checking
├── datos_crudos/
├── datos_procesados/
├── resultados/
├── scripts/
├── paper/                    # manuscript source, PDF, tables, figures, bibliography
├── srs/                      # ERS/SRS v2.0 snapshot and figures
└── provenance/
```

## Reproduction
Recommended Python: 3.11+.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
# source .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/run_all.py
```

A successful run reproduces the headline empirical results listed above. Statistical procedures not supported by the actual instrument are explicitly marked as not applicable rather than manufactured.

## Preregistration and deviations
- OSF record: https://osf.io/62ysc/
- OSF DOI: `10.17605/OSF.IO/62YSC`
- Protocol: v1.4

The six WALK sessions occurred before OSF registration. They are reported transparently as pre-registration/formative evidence. `osf_deviations.pdf` and `osf_deviations.md` document this chronology and the non-applicability of unsupported inferential metrics.

## Privacy boundary
This package contains no audio/video bytes, original signed consent forms, identity documents, faces, voices, handwritten signatures, personal emails, phone numbers, IP addresses, or restricted evidence containers. The multimedia technical table contains only public metadata such as session code, file name, duration and declared hash.

## Licenses
- Public anonymized data and documentation: **CC BY 4.0**.
- Analysis scripts: **MIT**.
- Identifiable/restricted evidence: **excluded from this package and not licensed for public redistribution**.

## Citation and Zenodo DOI
`CITATION.cff` contains the authors, ORCID identifiers, title, version and Zenodo DOI. Dataset DOI: **10.5281/zenodo.22237884** (https://doi.org/10.5281/zenodo.22237884). The OSF DOI remains the preregistration identifier and must not be substituted for the dataset DOI.


## ERS/SRS and UML final
The package includes ERS/SRS 2B v2.2 and the definitive 54-diagram UML set under `srs/` and `modelado/`.
