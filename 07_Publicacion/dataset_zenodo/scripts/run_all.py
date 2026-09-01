#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FabroGym — Entrega 4 (2B), Fase 2
Entrada única reproducible del análisis empírico.

Principios:
- usa únicamente datos versionados en 06_Experimento/datos_crudos/;
- no inventa observaciones, puntuaciones, perfiles, hashes ni pruebas;
- no convierte preguntas generales de encuesta en Likert de explicabilidad;
- documenta como NO APLICABLE cualquier inferencia no soportada.
"""
from pathlib import Path
import json, math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.power import TTestPower, TTestIndPower
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "datos_crudos"
PROC = ROOT / "datos_procesados"
RES = ROOT / "resultados"
TAB = RES / "tablas"
FIG = RES / "figuras"
for p in (PROC, RES, TAB, FIG):
    p.mkdir(parents=True, exist_ok=True)

FINAL_MAP = {
    "RNF-EXP-C01": "RNF-EXP-01",
    "RNF-EXP-C02": "RNF-EXP-02",
    "RNF-EXP-C03": "RNF-EXP-03",
    "RNF-EXP-C04": "RNF-EXP-04",
}

def hms_to_seconds(v):
    h, m, s = map(int, str(v).split(":"))
    return h * 3600 + m * 60 + s

def fmt_hms(x):
    x = int(x)
    return f"{x//3600:02d}:{(x%3600)//60:02d}:{x%60:02d}"

def savefig(base_name):
    plt.tight_layout()
    plt.savefig(FIG / f"{base_name}.png", dpi=220)
    plt.savefig(FIG / f"{base_name}.svg")
    plt.close()

def read_inputs():
    survey = pd.read_csv(RAW / "encuesta_clientes_anonimizada.csv", encoding="utf-8-sig")
    # Normalización de cabeceras por posición; los valores permanecen intactos.
    public_cols = [
        "timestamp","consent","attendance_freq","membership_tenure","membership_check",
        "expiry_difficulty","payment_wait","notice_preference","registration_ease","plan_clarity",
        "staff_satisfaction","entry_method","routine_consult","future_info","purchase_difficulty",
        "improve_first","privacy_importance","comment","change_experience","future_function"
    ]
    legacy_cols = public_cols + ["participant_name","col21"]
    if len(survey.columns) == len(public_cols):
        survey.columns = public_cols
        survey["participant_name"] = np.nan
        survey["col21"] = np.nan
    elif len(survey.columns) == len(legacy_cols):
        survey.columns = legacy_cols
    else:
        raise ValueError(f"Unexpected questionnaire column count: {len(survey.columns)}")
    sessions = pd.read_csv(RAW / "sesiones_multimedia_desde_ficha_v3_1.csv", encoding="utf-8-sig")
    coding = pd.read_csv(RAW / "codificacion_walkthroughs.csv", encoding="utf-8-sig")
    curve = pd.read_csv(RAW / "curva_codigos_nuevos_walkthroughs_fuente.csv", encoding="utf-8-sig")
    axial = pd.read_csv(RAW / "estabilizacion_categorias_axiales_fuente.csv", encoding="utf-8-sig")
    profile = pd.read_csv(RAW / "comparacion_perfiles_walkthroughs_fuente.csv", encoding="utf-8-sig")
    candidates = pd.read_csv(RAW / "candidatos_RNF_explicabilidad_member_checked.csv", encoding="utf-8-sig")
    fragments = pd.read_csv(RAW / "fragmentos_pertinentes_explicabilidad.csv", encoding="utf-8-sig")
    mc = pd.read_csv(RAW / "member_checking_estructurado.csv", encoding="utf-8-sig")
    return survey, sessions, coding, curve, axial, profile, candidates, fragments, mc

def analyze_multimedia(sessions):
    s = sessions.copy()
    s["audio_segundos"] = s["audio_duracion"].map(hms_to_seconds)
    s["video_segundos"] = s["video_duracion"].map(hms_to_seconds)
    s["audio_hash_formato_64hex"] = s["audio_sha256"].astype(str).str.fullmatch(r"[0-9a-fA-F]{64}")
    s["video_hash_formato_64hex"] = s["video_sha256"].astype(str).str.fullmatch(r"[0-9a-fA-F]{64}")
    vt, at = int(s["video_segundos"].sum()), int(s["audio_segundos"].sum())
    s.to_csv(PROC / "sesiones_multimedia_verificadas.csv", index=False, encoding="utf-8-sig")
    s.drop(columns=["audio_segundos","video_segundos"]).to_csv(
        TAB / "tabla_identificadores_ficha_tecnica.csv", index=False, encoding="utf-8-sig")
    summary = pd.DataFrame([{
        "sesiones_unicas": len(s),
        "entrevistas_ENTR": int(s["codigo_sesion"].str.startswith("ENTR-").sum()),
        "walkthroughs_WALK": int(s["codigo_sesion"].str.startswith("WALK-").sum()),
        "walkthroughs_tecnicos": int(s["codigo_sesion"].str.startswith("WALK-TEC-").sum()),
        "walkthroughs_no_tecnicos": int(s["codigo_sesion"].str.startswith("WALK-NTEC-").sum()),
        "audios": int(s["audio_archivo"].notna().sum()),
        "videos": int(s["video_archivo"].notna().sum()),
        "duracion_total_video": fmt_hms(vt),
        "duracion_total_audio": fmt_hms(at),
        "duracion_video_minutos": round(vt/60, 3),
        "cumple_16_videos": bool(len(s) >= 16),
        "cumple_240_min_video": bool(vt >= 240*60),
        "hashes_audio_formato_valido": bool(s["audio_hash_formato_64hex"].all()),
        "hashes_video_formato_valido": bool(s["video_hash_formato_64hex"].all()),
        "nota_hashes": "Se valida formato SHA-256 (64 hex). La coincidencia con multimedia requiere rehashear los archivos reales de la zona restringida."
    }])
    summary.to_csv(TAB / "tabla_cumplimiento_multimedia.csv", index=False, encoding="utf-8-sig")
    return vt, at

def analyze_survey(survey):
    survey.to_csv(PROC / "encuesta_clientes_limpia.csv", index=False, encoding="utf-8-sig")
    categorical = [
        "attendance_freq","membership_tenure","membership_check","expiry_difficulty","payment_wait",
        "notice_preference","registration_ease","plan_clarity","staff_satisfaction","entry_method",
        "routine_consult","future_info","purchase_difficulty","improve_first","privacy_importance"
    ]
    rows = []
    for c in categorical:
        for value, count in survey[c].fillna("(vacío)").value_counts(dropna=False).items():
            rows.append({"variable":c,"categoria":value,"conteo":int(count),
                         "porcentaje":round(100*count/len(survey),3)})
    pd.DataFrame(rows).to_csv(TAB / "tabla_encuesta_frecuencias.csv", index=False, encoding="utf-8-sig")

    maps = {
        "expiry_difficulty":{"Nunca":1,"Casi nunca":2,"A veces":3,"Casi siempre":4,"Siempre":5},
        "payment_wait":{"Nunca":1,"Casi nunca":2,"A veces":3,"Casi siempre":4,"Siempre":5},
        "registration_ease":{"Muy difícil":1,"Difícil":2,"Ni fácil ni difícil":3,"Fácil":4,"Muy fácil":5},
        "plan_clarity":{"Muy poco clara":1,"Poco clara":2,"Ni clara ni poco clara":3,"Clara":4,"Muy clara":5},
        "staff_satisfaction":{"Muy insatisfecho(a)":1,"Insatisfecho(a)":2,"Ni satisfecho(a) ni insatisfecho(a)":3,"Satisfecho(a)":4,"Muy satisfecho(a)":5},
        "privacy_importance":{"Nada importante":1,"Poco importante":2,"Moderadamente importante":3,"Importante":4,"Muy importante":5},
    }
    rng = np.random.default_rng(401)
    out = []
    for c, mp in maps.items():
        x = survey[c].map(mp).dropna().astype(float).to_numpy()
        boot = np.array([rng.choice(x, size=len(x), replace=True).mean() for _ in range(10000)])
        out.append({
            "variable":c,"n":len(x),"media_indice_1a5":round(float(x.mean()),3),
            "mediana":round(float(np.median(x)),3),"desv_est":round(float(x.std(ddof=1)),3),
            "IC95_boot_media_inf":round(float(np.quantile(boot,.025)),3),
            "IC95_boot_media_sup":round(float(np.quantile(boot,.975)),3),
            "interpretacion":"Índice descriptivo ordinal; NO es escala Likert de explicabilidad."
        })
    pd.DataFrame(out).to_csv(TAB / "tabla_encuesta_indices_ordinales.csv", index=False, encoding="utf-8-sig")

    pd.DataFrame([{
        "n_respuestas":len(survey),
        "consentimientos_aceptados":int(survey["consent"].str.contains("Acepto participar", na=False).sum()),
        "campo_perfil_tecnico_no_tecnico_presente":False,
        "items_likert_explicabilidad_presentes":False,
        "nombre_participante_no_vacio":int(survey["participant_name"].notna().sum()),
        "columna_auxiliar_no_vacia":int(survey["col21"].notna().sum()),
        "uso_valido":"Descriptivo para necesidades generales del gimnasio; no para comparar perfiles ni medir satisfacción de explicabilidad."
    }]).to_csv(TAB / "tabla_alcance_encuesta.csv", index=False, encoding="utf-8-sig")

    n_one = TTestPower().solve_power(effect_size=.5, alpha=.05, power=.80, alternative="two-sided")
    n_ind = TTestIndPower().solve_power(effect_size=.5, alpha=.05, power=.80, ratio=1, alternative="two-sided")
    pd.DataFrame([
        {"escenario":"Una muestra o diferencia pareada estandarizada","Cohen_d":0.5,"alpha":0.05,"potencia":0.80,
         "n_requerido_continuo":round(float(n_one),3),"n_requerido_redondeado":math.ceil(n_one),
         "aplicabilidad_FabroGym":"Referencia de sensibilidad; n=70 supera este mínimo, pero el cuestionario no contiene una escala de explicabilidad."},
        {"escenario":"Dos grupos independientes de igual tamaño","Cohen_d":0.5,"alpha":0.05,"potencia":0.80,
         "n_requerido_continuo":round(float(n_ind),3),"n_requerido_redondeado":math.ceil(n_ind),
         "aplicabilidad_FabroGym":"Requeriría ~64 por grupo (128 total). El cuestionario no registra perfil técnico/no técnico."}
    ]).to_csv(TAB / "tabla_power_calculation.csv", index=False, encoding="utf-8-sig")

    imp = survey["improve_first"].value_counts()
    plt.figure(figsize=(8,5)); plt.bar(imp.index, imp.values)
    plt.xticks(rotation=30, ha="right"); plt.xlabel("Aspecto"); plt.ylabel("Respuestas")
    plt.title("Prioridad de mejora indicada por clientes (n=70)"); savefig("encuesta_prioridades_mejora")

    order_priv = ["Nada importante","Poco importante","Moderadamente importante","Importante","Muy importante"]
    priv = survey["privacy_importance"].value_counts().reindex(order_priv, fill_value=0)
    plt.figure(figsize=(8,5)); plt.bar(priv.index, priv.values)
    plt.xticks(rotation=25, ha="right"); plt.xlabel("Importancia"); plt.ylabel("Respuestas")
    plt.title("Importancia percibida de privacidad (n=70)"); savefig("encuesta_privacidad")
    return n_one, n_ind

def analyze_walkthroughs(coding, curve, axial, profile):
    coding.to_csv(PROC / "codificacion_walkthroughs.csv", index=False, encoding="utf-8-sig")
    profile.to_csv(PROC / "comparacion_perfiles_walkthroughs.csv", index=False, encoding="utf-8-sig")
    profile.to_csv(TAB / "tabla_comparacion_perfiles_walkthroughs.csv", index=False, encoding="utf-8-sig")

    curve = curve.copy(); axial = axial.copy()
    curve["Codigos_acumulados"] = curve["Codigos_nuevos"].cumsum()
    curve["Porcentaje_nuevos_sobre_total_final"] = 100 * curve["Codigos_nuevos"] / curve["Codigos_nuevos"].sum()
    axial["Categorias_acumuladas"] = axial["Categorias_axiales_nuevas"].cumsum()
    curve.to_csv(PROC / "curva_saturacion_codigos_walkthroughs.csv", index=False, encoding="utf-8-sig")
    axial.to_csv(PROC / "curva_estabilizacion_categorias_axiales.csv", index=False, encoding="utf-8-sig")
    curve.to_csv(TAB / "tabla_saturacion_codigos_walkthroughs.csv", index=False, encoding="utf-8-sig")
    axial.to_csv(TAB / "tabla_estabilizacion_categorias_axiales.csv", index=False, encoding="utf-8-sig")

    total = int(curve["Codigos_nuevos"].sum()); avg3 = float(curve.tail(3)["Codigos_nuevos"].mean())
    pct = 100 * avg3 / total
    total_a = int(axial["Categorias_axiales_nuevas"].sum()); avg3a = float(axial.tail(3)["Categorias_axiales_nuevas"].mean())
    pcta = 100 * avg3a / total_a
    pd.DataFrame([
        {"nivel":"Códigos_normalizados","total_acumulado":total,"promedio_nuevos_ultimas_3":round(avg3,3),
         "porcentaje_criterio":round(pct,3),"umbral_rubrica_pct":5.0,"cumple_umbral":bool(pct<=5),
         "conclusion":"No alcanza estrictamente el <=5%; existe inflexión visible desde la cuarta sesión."},
        {"nivel":"Categorías_axiales","total_acumulado":total_a,"promedio_nuevas_ultimas_3":round(avg3a,3),
         "porcentaje_criterio":round(pcta,3),"umbral_referencia_pct":5.0,"cumple_umbral":bool(pcta<=5),
         "conclusion":"Se estabilizan; evidencia complementaria, no sustituto del criterio por códigos."}
    ]).to_csv(TAB / "tabla_resumen_saturacion.csv", index=False, encoding="utf-8-sig")

    pd.DataFrame([{
        "sesiones_tecnicas":3,"sesiones_no_tecnicas":3,
        "fragmentos_tecnicos":int((coding["Perfil"]=="Tecnico").sum()),
        "fragmentos_no_tecnicos":int((coding["Perfil"]=="No tecnico").sum()),
        "categorias_tematica_total":int(coding["Categoria"].nunique()),
        "codigos_normalizados_total":int(coding["Codigo_Normalizado"].nunique()),
        "tipo_comparacion":"Descriptiva/cualitativa",
        "mann_whitney":"NO APLICABLE: no existe resultado cuantitativo por participante preregistrado; n=3 por perfil."
    }]).to_csv(TAB / "tabla_resumen_perfiles.csv", index=False, encoding="utf-8-sig")

    plt.figure(figsize=(9,5)); plt.plot(curve["Codigo_Sesion"], curve["Codigos_nuevos"], marker="o", label="Códigos nuevos")
    plt.plot(curve["Codigo_Sesion"], curve["Codigos_acumulados"], marker="o", label="Códigos acumulados")
    plt.xticks(rotation=30, ha="right"); plt.xlabel("Sesión walkthrough"); plt.ylabel("Número de códigos")
    plt.title("Curva de códigos normalizados — walkthroughs FabroGym"); plt.legend(); savefig("curva_saturacion_codigos_walkthroughs")

    plt.figure(figsize=(9,5)); plt.plot(axial["Codigo_Sesion"], axial["Categorias_axiales_nuevas"], marker="o", label="Categorías nuevas")
    plt.plot(axial["Codigo_Sesion"], axial["Categorias_acumuladas"], marker="o", label="Categorías acumuladas")
    plt.xticks(rotation=30, ha="right"); plt.xlabel("Sesión walkthrough"); plt.ylabel("Número de categorías")
    plt.title("Estabilización de categorías axiales — FabroGym"); plt.legend(); savefig("curva_estabilizacion_categorias_axiales")
    return total, avg3, pct, total_a, avg3a, pcta

def analyze_explainability(coding, candidates, fragments, mc):
    exp = coding[coding["Aplicable_Explicabilidad"].astype(str).str.strip().str.lower().isin(["si","sí"])].copy()
    exp.to_csv(PROC / "fragmentos_explicabilidad_desde_codificacion.csv", index=False, encoding="utf-8-sig")
    fragments.to_csv(PROC / "fragmentos_pertinentes_explicabilidad.csv", index=False, encoding="utf-8-sig")
    mc.to_csv(PROC / "member_checking.csv", index=False, encoding="utf-8-sig")

    dims = []
    for v in exp["Dimension_Explicabilidad"].dropna():
        for token in str(v).split("/"):
            token = token.strip().lower()
            if token: dims.append(token)
    dim_counts = pd.Series(dims).value_counts().rename_axis("dimension_observada").reset_index(name="fragmentos")
    dim_counts["porcentaje_sobre_9_fragmentos"] = round(100*dim_counts["fragmentos"]/len(exp),3)
    dim_counts["nota"] = "Frecuencia descriptiva de etiquetas observadas; no equivale a cobertura porcentual del marco completo."
    dim_counts.to_csv(TAB / "tabla_dimensiones_explicabilidad_observadas.csv", index=False, encoding="utf-8-sig")

    final = candidates.copy()
    final.insert(0, "ID_RNF_Final", final["ID_RNF"].map(FINAL_MAP))
    final.rename(columns={"ID_RNF":"ID_Candidato"}, inplace=True)
    final["Estado_requisito"] = "ESPECIFICADO"
    final["Estado_componente_recomendacion"] = "PROPUESTO"
    final["Implementado_en_MVP"] = "NO"
    final.to_csv(PROC / "RNF_explicabilidad_final.csv", index=False, encoding="utf-8-sig")
    cols = ["ID_RNF_Final","ID_Candidato","Enunciado_RNF","Que_se_explica","A_quien","Formato","Momento",
            "Metrica","Umbral","Metodo_Comprobacion","Fuentes","Resultado_Member_Checking","Decision_Final",
            "Fecha_Member_Checking","Nota_Member_Checking","Estado_requisito","Estado_componente_recomendacion","Implementado_en_MVP"]
    final[cols].to_csv(TAB / "tabla_RNF_explicabilidad_final.csv", index=False, encoding="utf-8-sig")

    complete = final[["Metrica","Umbral","Metodo_Comprobacion"]].notna().all(axis=1)
    pd.DataFrame([{
        "fragmentos_codificados_total":len(coding),"fragmentos_pertinentes_explicabilidad":len(exp),
        "fragmentos_explicabilidad_tecnicos":int((exp["Perfil"]=="Tecnico").sum()),
        "fragmentos_explicabilidad_no_tecnicos":int((exp["Perfil"]=="No tecnico").sum()),
        "candidatos_RNF_revisados":len(candidates),"RNF_finales_incorporables":len(final),
        "RNF_con_metrica_umbral_metodo":int(complete.sum()),
        "porcentaje_operacionalizacion_completa":round(100*complete.mean(),3),
        "cobertura_porcentaje_marco_explicabilidad":"NO CALCULABLE",
        "motivo_cobertura":"El protocolo exige denominador y clasificación verificables; la evidencia usa etiquetas compuestas y no fija un universo cerrado."
    }]).to_csv(TAB / "tabla_resumen_explicabilidad.csv", index=False, encoding="utf-8-sig")

    counts = mc["Resultado"].value_counts().reindex(["Confirmado","Ajustado","No confirmado"], fill_value=0)
    mcs = pd.DataFrame([{"Resultado":k,"Conteo":int(v),"Porcentaje":round(100*v/len(mc),3)} for k,v in counts.items()])
    mcs.to_csv(TAB / "tabla_member_checking_resumen.csv", index=False, encoding="utf-8-sig")
    mc.to_csv(TAB / "tabla_member_checking_decisiones.csv", index=False, encoding="utf-8-sig")
    rows = []
    for cid, g in mc.groupby("ID"):
        c = g["Resultado"].value_counts()
        decision = candidates.loc[candidates["ID_RNF"]==cid, "Decision_Final"].iloc[0]
        rows.append({"ID_Candidato":cid,"ID_RNF_Final":FINAL_MAP.get(cid,""),
                     "Confirmado":int(c.get("Confirmado",0)),"Ajustado":int(c.get("Ajustado",0)),
                     "No_confirmado":int(c.get("No confirmado",0)),"Decision_final":decision})
    pd.DataFrame(rows).to_csv(TAB / "tabla_member_checking_por_RNF.csv", index=False, encoding="utf-8-sig")

    plt.figure(figsize=(7,4.5)); plt.bar(mcs["Resultado"], mcs["Conteo"])
    plt.xlabel("Decisión"); plt.ylabel("Conteo"); plt.title("Member checking de cuatro candidatos RNF")
    savefig("member_checking_decisiones")
    return final, exp, counts

def write_applicability():
    pd.DataFrame([
        {"metrica_prueba":"Satisfacción Likert por dimensión de explicabilidad + IC95%","estado":"NO APLICABLE",
         "justificacion":"El cuestionario real no contiene ítems Likert de explicabilidad por dimensión. Los índices ordinales son generales y descriptivos."},
        {"metrica_prueba":"Fleiss kappa entre rondas de validación","estado":"NO CALCULADO",
         "justificacion":"No existen dos rondas equivalentes de clasificación; el protocolo v1.4 preregistró decisión nominal de member checking y excluyó kappa."},
        {"metrica_prueba":"U de Mann-Whitney técnico vs no técnico","estado":"NO APLICABLE",
         "justificacion":"Hay tres walkthroughs por perfil y no existe resultado cuantitativo independiente por participante preregistrado."},
        {"metrica_prueba":"Shapiro-Wilk / Levene","estado":"NO APLICABLE",
         "justificacion":"No se ejecuta una hipótesis inferencial sobre una variable cuantitativa del Enfoque 3."},
        {"metrica_prueba":"Bootstrap IC95% de índices ordinales generales de encuesta","estado":"APLICADO DESCRIPTIVAMENTE",
         "justificacion":"Solo describe seis preguntas ordinales generales; no se interpreta como explicabilidad ni como prueba de hipótesis."}
    ]).to_csv(TAB / "tabla_aplicabilidad_pruebas_estadisticas.csv", index=False, encoding="utf-8-sig")

def write_summary(survey, sessions, coding, final, exp, counts, vt, at, sat):
    total, avg3, pct, total_a, avg3a, pcta = sat
    summary = {
        "proyecto":"FabroGym","fase":"2B - Fase 2 análisis empírico reproducible",
        "sesiones":{"total":len(sessions),"entrevistas":10,"walkthroughs":6,"walkthroughs_tecnicos":3,"walkthroughs_no_tecnicos":3,
                    "video_total":fmt_hms(vt),"audio_total":fmt_hms(at)},
        "encuesta":{"n":len(survey),"perfil_tecnico_no_tecnico_disponible":False,"items_likert_explicabilidad":False},
        "walkthroughs":{"fragmentos":len(coding),"tecnicos":int((coding["Perfil"]=="Tecnico").sum()),
                        "no_tecnicos":int((coding["Perfil"]=="No tecnico").sum()),
                        "codigos_normalizados":int(coding["Codigo_Normalizado"].nunique()),"categorias":int(coding["Categoria"].nunique())},
        "explicabilidad":{"fragmentos_pertinentes":len(exp),"candidatos":len(final),"rnf_finales":len(final),
                          "cobertura_marco_porcentaje":None,"razon_no_porcentaje":"No existe denominador cerrado verificable en instrumento/codificación."},
        "member_checking":{"participantes":["MC-P01","MC-P02","MC-P03"],"fecha":"2026-08-29","decisiones":int(counts.sum()),
                           "confirmado":int(counts["Confirmado"]),"ajustado":int(counts["Ajustado"]),
                           "no_confirmado":int(counts["No confirmado"]),"grabacion_audiovisual":False},
        "saturacion":{"codigos_total":total,"promedio_nuevos_ultimas_3":round(avg3,3),"porcentaje":round(pct,3),
                      "umbral_pct":5.0,"cumple_codigos":bool(pct<=5),"categorias_axiales_total":total_a,
                      "porcentaje_categorias_ultimas_3":round(pcta,3),"cumple_categorias":bool(pcta<=5)}
    }
    (RES / "resumen_resultados.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    md = f"""# Resultados empíricos terminales — FabroGym\n\n## Evidencia multimedia\nLa ficha técnica v3.1 identifica 16 sesiones únicas: 10 `ENTR-*`, 3 `WALK-TEC-*` y 3 `WALK-NTEC-*`. La suma de los 16 videos es **{fmt_hms(vt)}** ({vt/60:.3f} min), por encima de 240 min; los audios suman **{fmt_hms(at)}**. No se suman audio y video como si fueran sesiones distintas.\n\n## Encuesta\nSe analizaron **{len(survey)} respuestas**. Las columnas directas finales de identificación están vacías en las 70 filas. El cuestionario no contiene un campo técnico/no técnico ni ítems Likert de explicabilidad; se reportan frecuencias e índices ordinales generales con IC95% bootstrap, sin reinterpretarlos como explicabilidad.\n\n## Walkthroughs\nSe analizaron **{len(coding)} fragmentos codificados**: {int((coding['Perfil']=='Tecnico').sum())} técnicos y {int((coding['Perfil']=='No tecnico').sum())} no técnicos, con {coding['Codigo_Normalizado'].nunique()} códigos normalizados y {coding['Categoria'].nunique()} categorías. La comparación entre perfiles es descriptiva/cualitativa conforme al protocolo v1.4.\n\n## Explicabilidad y member checking\nSe identificaron **{len(exp)} fragmentos pertinentes** y **{len(final)} RNF terminales**. El member checking con `MC-P01`, `MC-P02` y `MC-P03` produjo {int(counts.sum())} decisiones: {int(counts['Confirmado'])} confirmaciones, {int(counts['Ajustado'])} ajustes y {int(counts['No confirmado'])} no confirmaciones. Los RNF se terminalizan como `RNF-EXP-01` a `RNF-EXP-04`; el componente recomendador permanece **PROPUESTO**, no implementado.\n\nNo se calcula porcentaje de cobertura del marco de explicabilidad: no existe un denominador cerrado verificable.\n\n## Saturación\nEn las últimas tres sesiones aparecen en promedio **{avg3:.3f}** códigos nuevos sobre **{total}** acumulados: **{pct:.3f}%**. El criterio estricto <=5% **no se alcanza**, aunque la curva presenta inflexión visible desde la cuarta sesión. A nivel axial, las últimas tres sesiones representan **{pcta:.3f}%** de categorías nuevas; se informa solo como evidencia complementaria de estabilización.\n\n## Pruebas no aplicadas\nNo se fabrican Fleiss kappa, Mann-Whitney, Shapiro-Wilk ni Levene donde los datos/protocolo no los soportan. Consulte `tabla_aplicabilidad_pruebas_estadisticas.csv`.\n"""
    (RES / "RESUMEN_FASE2.md").write_text(md, encoding="utf-8")
    return summary

def write_osf_deviations(summary):
    sat = summary["saturacion"]
    text = f"""# Deviations from preregistration — FabroGym\n\nRegistro OSF: https://osf.io/62ysc/  \nDOI OSF: 10.17605/OSF.IO/62YSC  \nProtocolo: v1.4  \nFecha del registro publicada: 2026-08-29\n\n## D1. Cronología de los walkthroughs\nLas seis sesiones WALK (`WALK-TEC-01..03` y `WALK-NTEC-01..03`) ocurrieron antes del registro OSF. Se mantienen como evidencia previa/formativa; no se presentan como datos confirmatorios recogidos después del sello temporal.\n\n## D2. Normalización de identificadores\nDocumentos tempranos usaron `WT-T01..03` y `WT-NT01..03`. La versión terminal normaliza a `WALK-TEC-01..03` y `WALK-NTEC-01..03`, manteniendo correspondencia directa por número y perfil. El PDF documental de member checking se conserva sin alterar.\n\n## D3. Análisis inferencial sugerido por la rúbrica\nEl protocolo v1.4 no preregistra hipótesis inferenciales para seis walkthroughs y excluye crear puntuaciones Likert, coeficientes de acuerdo o variables cuantitativas inexistentes. Por ello no se calculan Fleiss kappa ni Mann-Whitney; el contraste por perfil es descriptivo/cualitativo.\n\n## D4. Cuestionario\nEl CSV real contiene 70 respuestas, pero no registra perfil técnico/no técnico ni ítems de explicabilidad por dimensión. Se analiza descriptivamente y no se reinterpreta ninguna pregunta general como escala de explicabilidad.\n\n## D5. Saturación\nLa curva acumula {sat['codigos_total']} códigos. El promedio nuevo de las últimas tres sesiones equivale a {sat['porcentaje']:.3f}% del total, ligeramente por encima del umbral <=5%; por tanto no se declara saturación estricta de códigos. A nivel axial se observa {sat['porcentaje_categorias_ultimas_3']:.3f}%, reportado solo como evidencia complementaria de estabilización.\n\n## D6. Member checking\nLa actividad está documentada con `MC-P01`, `MC-P02` y `MC-P03`, fecha 2026-08-29, con 12 decisiones: 4 confirmaciones y 8 ajustes. No existe grabación audiovisual; esta ausencia se declara como riesgo frente a la redacción literal de la rúbrica y no se fabrica material inexistente.\n\n## D7. Ficha técnica y duración\nLa ficha v3.1 conserva `ENTR-01..10`, `WALK-TEC-01..03` y `WALK-NTEC-01..03`. Los 16 videos suman {summary['sesiones']['video_total']} y los audios {summary['sesiones']['audio_total']}; se usa una sola duración por sesión para el mínimo temporal.\n"""
    (ROOT / "osf_deviations.md").write_text(text, encoding="utf-8")

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleCenter2", parent=styles["Title"], alignment=TA_CENTER, fontSize=15, leading=18, spaceAfter=10))
    styles.add(ParagraphStyle(name="BodyX", parent=styles["BodyText"], fontSize=9.4, leading=12.7, spaceAfter=6))
    styles.add(ParagraphStyle(name="H2X", parent=styles["Heading2"], fontSize=10.8, leading=13, spaceBefore=6, spaceAfter=3))
    doc = SimpleDocTemplate(str(ROOT / "osf_deviations.pdf"), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm)
    story = [Paragraph("FabroGym — Deviations from preregistration", styles["TitleCenter2"]),
             Paragraph("Entrega 4 (2B) — Enfoque 3: Explicabilidad como Requisito No Funcional", styles["BodyX"])]
    meta = [["Campo","Valor"],["Registro OSF","https://osf.io/62ysc/"],["DOI OSF","10.17605/OSF.IO/62YSC"],["Protocolo","v1.4"],["Fecha publicada","29-08-2026"]]
    t = Table(meta, colWidths=[42*mm,120*mm], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.lightgrey),("GRID",(0,0),(-1,-1),.4,colors.grey),
                           ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTNAME",(0,1),(0,-1),"Helvetica-Bold"),
                           ("FONTSIZE",(0,0),(-1,-1),8.4),("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
                           ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
    story += [t, Spacer(1,6)]
    sections = [
        ("D1. Cronología de los walkthroughs", "Las seis sesiones WALK (WALK-TEC-01..03 y WALK-NTEC-01..03) ocurrieron antes del registro OSF. Se mantienen como evidencia previa/formativa y no se presentan como datos confirmatorios posteriores al sello temporal."),
        ("D2. Normalización de identificadores", "Documentos tempranos usaron WT-T01..03 y WT-NT01..03. La versión terminal adopta WALK-TEC-01..03 y WALK-NTEC-01..03. El PDF documental de member checking se conserva sin alterar; las tablas procesadas usan los identificadores terminales."),
        ("D3. Análisis inferencial", "El protocolo v1.4 no preregistra hipótesis inferenciales para los seis walkthroughs y excluye crear variables inexistentes. No se calculan Fleiss kappa ni Mann-Whitney; el contraste técnico/no técnico es descriptivo y cualitativo."),
        ("D4. Cuestionario", "El archivo real contiene 70 respuestas, pero no registra perfil técnico/no técnico ni ítems de explicabilidad por dimensión. Se conserva como evidencia descriptiva; ninguna pregunta general se reinterpreta como Likert de explicabilidad."),
        ("D5. Saturación", f"La curva acumula {sat['codigos_total']} códigos normalizados. El promedio nuevo de las últimas tres sesiones equivale a {sat['porcentaje']:.3f}% del total, ligeramente superior al umbral <=5%. No se declara saturación estricta de códigos. A nivel axial se observa {sat['porcentaje_categorias_ultimas_3']:.3f}%, como evidencia complementaria de estabilización."),
        ("D6. Member checking", "La actividad está documentada con MC-P01, MC-P02 y MC-P03, fechada 29-08-2026, con 12 decisiones: 4 confirmaciones y 8 ajustes. No existe grabación audiovisual. Esta ausencia se declara como riesgo frente a la redacción literal de la rúbrica y no se fabrica una grabación inexistente."),
        ("D7. Ficha técnica y duración", f"La ficha v3.1 conserva ENTR-01..10, WALK-TEC-01..03 y WALK-NTEC-01..03. Los 16 videos suman {summary['sesiones']['video_total']} y los audios {summary['sesiones']['audio_total']}. Para el mínimo temporal se usa una sola duración por sesión, evitando doble conteo.")
    ]
    for h,b in sections:
        story.append(Paragraph(h, styles["H2X"])); story.append(Paragraph(b, styles["BodyX"]))
    story.append(Spacer(1,5)); story.append(Paragraph("<b>Principio de transparencia.</b> Este documento no modifica fechas, firmas, respuestas ni evidencia primaria. Las limitaciones se reportan para mantener coherencia entre OSF, evidencia, ERS/SRS y manuscrito.", styles["BodyX"]))
    doc.build(story)

def main():
    survey, sessions, coding, curve, axial, profile, candidates, fragments, mc = read_inputs()
    vt, at = analyze_multimedia(sessions)
    analyze_survey(survey)
    sat = analyze_walkthroughs(coding, curve, axial, profile)
    final, exp, counts = analyze_explainability(coding, candidates, fragments, mc)
    write_applicability()
    summary = write_summary(survey, sessions, coding, final, exp, counts, vt, at, sat)
    write_osf_deviations(summary)
    print("OK — FabroGym Fase 2 regenerada")
    print(f"Sesiones: {len(sessions)}; video total: {fmt_hms(vt)}; audio total: {fmt_hms(at)}")
    print(f"Encuesta: n={len(survey)}; sin perfil técnico/no técnico; sin Likert de explicabilidad")
    print(f"Walkthroughs: {len(coding)} fragmentos; códigos={coding['Codigo_Normalizado'].nunique()}; categorías={coding['Categoria'].nunique()}")
    print(f"Saturación códigos últimas 3: {sat[2]:.3f}% -> {'CUMPLE' if sat[2] <= 5 else 'NO CUMPLE ESTRICTAMENTE'}")
    print(f"Member checking: {int(counts.sum())} decisiones; RNF terminales={len(final)}")

if __name__ == "__main__":
    main()
