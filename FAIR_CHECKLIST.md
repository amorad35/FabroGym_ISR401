# FAIR_CHECKLIST — FabroGym 2B (pre-Zenodo)

**Important:** this is a readiness checklist, **not** a F-UJI score. No percentage is claimed before the real Zenodo DOI exists and F-UJI is executed.

| FAIR area | Check | Evidence prepared | Status before Phase 6 |
|---|---|---|---|
| F | Persistent identifier | Zenodo metadata draft | POST-ZENODO |
| F | Rich title/description/creators/keywords | `ZENODO_METADATA_DRAFT.json` | READY |
| F | Machine-readable citation | `CITATION.cff` v1.2.0 | READY, DOI pending |
| F | Repository discoverability | GitHub + OSF URLs documented | READY |
| A | Public data accessible without identifiable evidence | anonymized package only | READY subject to final scan |
| A | Restricted evidence excluded | `ANONYMIZATION.md`, `ETHICS.md`, LICENSE | READY |
| A | License explicit | CC BY 4.0 data/docs, MIT code | READY |
| I | Open tabular/structured formats | CSV, JSON, TXT/MD | READY |
| I | Stable identifiers across artifacts | ENTR/WALK/MC/RNF IDs | READY |
| I | Data dictionary | `DATA_DICTIONARY.md` | READY |
| R | Provenance | `provenance/` + OSF deviations | READY |
| R | Reproducible scripts | `scripts/run_all.py` + requirements | READY |
| R | Versioning | VERSION + CHANGELOG + manifest/checksums | READY/PRE-FINAL |
| R | Citation metadata | CFF + Zenodo draft metadata | READY, DOI pending |
| R | External FAIR assessment | F-UJI PDF | POST-ZENODO |

## Acceptance sequence
1. Complete Phase 6.
2. Run final Zenodo builder and privacy validator.
3. Publish Zenodo and obtain the real DOI.
4. Apply DOI/SWHID to metadata.
5. Archive final GitHub state in Software Heritage.
6. Run F-UJI against the Zenodo DOI and save the exported assessment as `fair_assessment.pdf` in repository root.
7. Confirm the actual F-UJI aggregate score is >=60%; if not, correct metadata and reassess. Never fabricate the value.
