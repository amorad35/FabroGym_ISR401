# FabroGym 2B Replication Package — README_dataset

## Dataset title
**Replication package for Explainability Requirements for Fitness Routine Recommendations: A Field Case Study in Ecuador**

## Status
This directory preserves the local snapshot of the dataset published on Zenodo as version **2.0.0**, DOI **10.5281/zenodo.22237884**. The later RF/RNF normalization in the repository is not claimed to be byte-identical to that published snapshot. Software Heritage SWHID and F-UJI score remain unclaimed.

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
- 4 evidence-derived explainability RNFs, normalized in the repository as RNF-16 … RNF-19.
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

## Relationship to the published deposit
The Zenodo record is already published at https://doi.org/10.5281/zenodo.22237884. This local directory is retained as the version-2.0.0 publication snapshot and is not modified during ERS/ID normalization. A later corrective Zenodo version must be evaluated separately and must repeat manifest, checksum, privacy and reproducibility validation.

## Preregistration and deviations
OSF record: https://osf.io/62ysc/  
OSF DOI: 10.17605/OSF.IO/62YSC

The six WALK sessions occurred before OSF registration. They are not represented as post-registration confirmatory data. The deviations artifact documents this chronology and the non-applicability of inferential metrics that the actual instruments do not support.

## Licenses
- Public anonymized dataset/documentation: CC BY 4.0.
- Analysis scripts: MIT.
- Identifiable/restricted evidence: excluded and never included in this package.

## Citation
Cite the published dataset with DOI **10.5281/zenodo.22237884** and the OSF preregistration separately; do not substitute one DOI for the other.
