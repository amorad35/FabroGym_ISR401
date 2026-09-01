# DATA_DICTIONARY

| Field / artifact | Meaning |
|---|---|
| `codigo_sesion` / `Codigo_Sesion` | Stable empirical session identifier. |
| `ENTR-*` | Initial semi-structured interview. |
| `WALK-TEC-*` | Technical walkthrough session. |
| `WALK-NTEC-*` | Non-technical walkthrough session. |
| `Perfil` | Technical/non-technical descriptive grouping for WALK coding. |
| `Categoria` | Thematic/axial category assigned to a coded fragment. |
| `Codigo_Normalizado` | Normalized open code used in the accumulation curve. |
| `Aplicable_Explicabilidad` | Flag identifying a fragment as pertinent to explainability. |
| `Dimension_Explicabilidad` | Multi-label observed explainability labels; not a closed denominator. |
| `RNF-EXP-01..04` | Final explainability non-functional requirements. |
| `MC-P01..03` | Anonymized member-checking respondent identifiers. |
| `Resultado` | Member-checking decision: Confirmado / Ajustado / No confirmado. |
| `privacy_importance` | General questionnaire ordinal privacy item; not an explainability measure. |
| `Metrica`, `Umbral`, `Metodo_Comprobacion` | Operationalization fields for candidate/final explainability RNFs. |
| `audio_sha256`, `video_sha256` | Declared multimedia hashes; matching must be checked against restricted real files before final delivery. |


## Codificación temática: dos corpus complementarios

### `codificacion/entrevistas_generales/codificacion_tematica_entrevistas.csv`
59 fragmentos de `ENTR-01..ENTR-10`. Variables principales: `Fragmento`, `Codigo`, `Tipo_codigo`, `Categoria`, `Requisito_derivado`, `ID_evidencia`, `Transcripcion`, `Participante`, `Rol`, `Lineas`, `Incluir_en_saturacion` y `Estado_revision`. Este corpus sustenta la elicitación general y la trazabilidad de requisitos.

### `codificacion/codificacion_walkthroughs.csv`
76 fragmentos de los seis `WALK-*`. Este corpus sustenta el análisis terminal de perfiles y explicabilidad. Los dos corpus no deben fusionarse para recalcular la métrica terminal de saturación de walkthroughs.
