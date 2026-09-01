# ANONYMIZATION

## Objective
This package contains only material intended for the public [P] zone. Direct identifiers and identifiable audiovisual evidence are excluded from the Zenodo package.

## Applied transformations
1. Interview transcripts use participant codes/pseudonyms instead of personal names.
2. WALK sessions retain only stable session identifiers (`WALK-TEC-*`, `WALK-NTEC-*`) and anonymized roles/profiles.
3. Member-checking records use `MC-P01`, `MC-P02`, and `MC-P03`.
4. The public questionnaire removes the two empty direct-identification columns (`Nombre de participante`, `Columna 21`) before packaging.
5. Audio/video, faces, voices, original signatures, ID numbers, personal emails, phones, IP addresses and original consents are not copied into the package.
6. The multimedia technical table may contain file names, durations, codecs/hashes and session codes, but not the multimedia bytes.

## Data minimization
Only fields needed to reproduce the published analysis are retained. Questions that are not explainability measures are not relabeled as explainability scores.

## Final pre-publication check
Run:
```bash
python scripts_release/validate_public_release.py 07_Publicacion/dataset_zenodo
```
Then manually inspect all new/transferred files. Automated scanning is a safeguard, not a substitute for human review.
