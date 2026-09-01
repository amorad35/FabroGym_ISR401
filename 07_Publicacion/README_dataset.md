# FabroGym 2B Replication Package — README_dataset

## Dataset title
**Replication package for Explainability Requirements for Fitness Routine Recommendations: A Field Case Study in Ecuador**

## Status
This directory is a **pre-deposit release candidate**. The team intentionally will create the Zenodo record **after Phase 6**. Therefore no Zenodo DOI, Software Heritage SWHID, or F-UJI score is claimed yet.

## Study scope
FabroGym is a requirements-engineering field case study in a local-gym domain. The empirical focus is explainability as a non-functional requirement for a **proposed** fitness-routine recommendation component. The recommender is not presented as implemented in the MVP.

The preserved session identifiers are:
- `ENTR-01` … `ENTR-10`: initial semi-structured interviews.
- `WALK-NTEC-01` … `WALK-NTEC-03`: non-technical walkthroughs.
- `WALK-TEC-01` … `WALK-TEC-03`: technical walkthroughs.
- `MC-P01`, `MC-P02`, `MC-P03`: member-checking respondents.

## Primary reproducible facts
- 16 accumulated audiovisual sessions in the technical record.
- Total video duration: 06:18:08; total audio duration: 06:18:14.
- Client questionnaire: n=70; no technical/non-technical profile field and no explainability Likert scale.
- Walkthrough coding: 76 coded fragments; 49 technical and 27 non-technical.
- 37 normalized codes and 18 thematic categories.
- 9 explainability-pertinent fragments.
- 4 final explainability RNFs: RNF-EXP-01 … RNF-EXP-04.
- Member checking: 12 decisions (4 Confirmado, 8 Ajustado, 0 No confirmado).
- Strict code-saturation criterion over the last three WALK sessions: 6.306%, therefore the <=5% threshold is **not claimed as met**.
- Axial-category stabilization: 1.852%, reported only as complementary evidence.

## Directory structure
```text
dataset_zenodo/
├── README_dataset.md
├── ANONYMIZATION.md
├── ETHICS.md
├── LICENSE_DATASET.txt
├── CITATION.cff
├── VERSION.txt
├── ZENODO_METADATA_DRAFT.json
├── DATA_DICTIONARY.md
├── REPRODUCIBILITY.md
├── MANIFEST.csv
├── checksums.sha256
├── transcripciones/
├── encuesta/
├── requisitos/
├── trazabilidad/
├── codificacion/
├── datos_crudos/
├── datos_procesados/
├── resultados/
├── scripts/
├── paper/
└── provenance/
```

## Reproduction
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/run_all.py
```

The script regenerates the empirical tables and figures from the public raw inputs. Statistical procedures that the instrument does not support are explicitly marked as not applicable rather than manufactured.

## Important pre-deposit finalization
The ten `ENTR-*` transcripts already exist in the public repository under `02_Evidencias/Transcripciones/`. They are copied into this package by `scripts_release/build_zenodo_package.py` **after Phase 6**, when the repository state is frozen. The current pre-deposit bundle includes a manifest of those required source paths and the six WALK transcripts already used by the analysis.

Do not publish the Zenodo record until the finalizer reports all 16 transcript identifiers present and the privacy scan passes.

## Preregistration and deviations
OSF record: https://osf.io/62ysc/  
OSF DOI: 10.17605/OSF.IO/62YSC

The six WALK sessions occurred before OSF registration. They are not represented as post-registration confirmatory data. The deviations artifact documents this chronology and the non-applicability of inferential metrics that the actual instruments do not support.

## Licenses
- Public anonymized dataset/documentation: CC BY 4.0.
- Analysis scripts: MIT.
- Identifiable/restricted evidence: excluded and never included in this package.

## Citation
After the final Zenodo publication, use the **real Zenodo DOI** inserted into `CITATION.cff`. Until then, cite the GitHub repository and OSF preregistration separately; do not substitute the OSF DOI for the dataset DOI.
