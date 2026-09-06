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
import json, math, subprocess, sys
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
    "RNF-EXP-C01": "RNF-16",
    "RNF-EXP-C02": "RNF-17",
    "RNF-EXP-C03": "RNF-18",
    "RNF-EXP-C04": "RNF-19",
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
    survey.columns = [
        "timestamp","consent","attendance_freq","membership_tenure","membership_check",
        "expiry_difficulty","payment_wait","notice_preference","registration_ease","plan_clarity",
        "staff_satisfaction","entry_method","routine_consult","future_info","purchase_difficulty",
        "improve_first","privacy_importance","comment","change_experience","future_function",
        "participant_name","col21"
    ]
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
        {"metrica_prueba":"Tamaño del efecto técnico vs no técnico por categorías WALK","estado":"APLICADO DESCRIPTIVAMENTE",
         "justificacion":"Correlación biserial por rangos pareada + IC95% bootstrap sobre 18 categorías; tres sesiones por perfil. No se interpreta como inferencia poblacional."},
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
    md = f"""# Resultados empíricos terminales — FabroGym\n\n## Evidencia multimedia\nLa ficha técnica v3.1 identifica 16 sesiones únicas: 10 `ENTR-*`, 3 `WALK-TEC-*` y 3 `WALK-NTEC-*`. La suma de los 16 videos es **{fmt_hms(vt)}** ({vt/60:.3f} min), por encima de 240 min; los audios suman **{fmt_hms(at)}**. No se suman audio y video como si fueran sesiones distintas.\n\n## Encuesta\nSe analizaron **{len(survey)} respuestas**. Las columnas directas finales de identificación están vacías en las 70 filas. El cuestionario no contiene un campo técnico/no técnico ni ítems Likert de explicabilidad; se reportan frecuencias e índices ordinales generales con IC95% bootstrap, sin reinterpretarlos como explicabilidad.\n\n## Walkthroughs\nSe analizaron **{len(coding)} fragmentos codificados**: {int((coding['Perfil']=='Tecnico').sum())} técnicos y {int((coding['Perfil']=='No tecnico').sum())} no técnicos, con {coding['Codigo_Normalizado'].nunique()} códigos normalizados y {coding['Categoria'].nunique()} categorías. La comparación entre perfiles sigue siendo descriptiva/exploratoria; se añade tamaño del efecto por categorías con correlación biserial por rangos pareada e IC95% bootstrap, sin p-valor ni inferencia por participante.\n\n## Explicabilidad y member checking\nSe identificaron **{len(exp)} fragmentos pertinentes** y **{len(final)} RNF terminales**. El member checking con `MC-P01`, `MC-P02` y `MC-P03` produjo {int(counts.sum())} decisiones: {int(counts['Confirmado'])} confirmaciones, {int(counts['Ajustado'])} ajustes y {int(counts['No confirmado'])} no confirmaciones. Los RNF se terminalizan como `RNF-16` a `RNF-19`; el componente recomendador permanece **PROPUESTO**, no implementado.\n\nNo se calcula porcentaje de cobertura del marco de explicabilidad: no existe un denominador cerrado verificable.\n\n## Saturación\nEn las últimas tres sesiones aparecen en promedio **{avg3:.3f}** códigos nuevos sobre **{total}** acumulados: **{pct:.3f}%**. El criterio estricto <=5% **no se alcanza**, aunque la curva presenta inflexión visible desde la cuarta sesión. A nivel axial, las últimas tres sesiones representan **{pcta:.3f}%** de categorías nuevas; se informa solo como evidencia complementaria de estabilización.\n\n## Pruebas no aplicadas\nNo se fabrican Fleiss kappa, Mann-Whitney, Shapiro-Wilk ni Levene donde los datos/protocolo no los soportan. Consulte `tabla_aplicabilidad_pruebas_estadisticas.csv`.\n"""
    (RES / "RESUMEN_FASE2.md").write_text(md, encoding="utf-8")
    return summary

def write_osf_deviations(summary):
    text = """# Registro de desviaciones reales del protocolo — FabroGym

## 1. Propósito

Este archivo registra únicamente diferencias reales y verificables entre el procedimiento efectivamente seguido por FabroGym y el protocolo/prerregistro OSF v1.4.

No se modifican retrospectivamente fechas, respuestas, instrumentos, evidencias ni resultados para hacerlos coincidir con el protocolo. Las condiciones metodológicas que son limitaciones, pero no cambios del procedimiento previsto, se separan explícitamente de las desviaciones.

**Registro OSF:** `https://osf.io/62ysc/`  
**DOI OSF:** `10.17605/OSF.IO/62YSC`  
**Protocolo:** v1.4  
**Fecha de publicación del registro:** 29/08/2026

---

## 2. Registro resumido

| ID | Fecha/periodo | Desviación real | Motivo | Impacto | Tratamiento | Estado |
|---|---|---|---|---|---|---|
| DEV-OSF-01 | 12/08/2026–29/08/2026 | Las seis sesiones WALK ocurrieron antes de la publicación del prerregistro OSF. | El prerregistro se formalizó después de ejecutar las sesiones. | Los WALK no pueden presentarse como datos confirmatorios recogidos bajo un protocolo previamente registrado. | Se conserva la cronología real y los WALK se tratan como evidencia previa/formativa; el análisis posterior se declara como posterior al registro. | DOCUMENTADA |
| DEV-AN-02 | 05/09/2026 | Se añadió al cierre 2B una verificación de acuerdo intercodificador mediante doble codificación sobre un subconjunto superior al 20 %, con Cohen's kappa e IC95 %. | La guía terminal exige doble codificación y medida de acuerdo con intervalo de confianza; el procedimiento no formaba parte del análisis preregistrado v1.4. | El resultado debe interpretarse como análisis adicional de cierre y no como prueba preregistrada. | Se conservan el subconjunto, las dos hojas de codificación, el script y los resultados del acuerdo; no se reescribe el protocolo histórico. | DOCUMENTADA |
| DEV-AN-03 | 05/09/2026 | Se añadió tamaño del efecto + IC95 % para la comparación técnico vs no técnico. | La guía terminal específica lo exige, mientras que el pipeline previo trataba la comparación por perfiles como descriptiva/cualitativa y no aplicaba una prueba inferencial por participante. | El análisis adicional no debe presentarse como hipótesis confirmatoria preregistrada ni como inferencia poblacional. | Se usa una medida descriptivo-exploratoria por categorías, generada por script, con IC95 % bootstrap y sin p-valor por participante. | DOCUMENTADA |

---

# 3. DEV-OSF-01 — Walkthroughs anteriores al prerregistro

## Condición esperada

Una actividad que se presente como confirmatoria bajo un prerregistro debe ejecutarse después del sello temporal del registro correspondiente.

## Situación real

Las sesiones `WALK-TEC-01..03` y `WALK-NTEC-01..03` se realizaron entre el 12 y el 22 de agosto de 2026. El registro OSF se publicó el 29 de agosto de 2026.

## Impacto y tratamiento

Las sesiones conservan valor como evidencia empírica previa/formativa, pero no se presentan como recolección confirmatoria posterior al prerregistro. Se mantiene la secuencia real:

**WALK → protocolo v1.4 → registro OSF → sistematización/análisis posterior.**

## Evidencia

- `02_Evidencias/Validacion_walkthrough/`
- `06_Experimento/datos_crudos/sesiones_multimedia_desde_ficha_v3_1.csv`
- `06_Experimento/protocolo.tex`
- `06_Experimento/osf_registration.pdf`
- DOI `10.17605/OSF.IO/62YSC`

---

# 4. DEV-AN-02 — Doble codificación y acuerdo intercodificador añadidos en cierre 2B

## Condición previa

El pipeline previo no trataba una medida de acuerdo intercodificador como análisis preregistrado aplicable.

## Situación real

Durante el cierre terminal 2B se incorporó una comprobación adicional sobre un subconjunto común superior al 20 % del corpus WALK, con dos hojas de codificación y cálculo reproducible de Cohen's kappa con IC95 %.

## Motivo

La guía específica de cierre exige doble codificación de al menos el 20 % y una medida de acuerdo acompañada de intervalo de confianza.

## Impacto y tratamiento

El resultado se informa como **análisis adicional de cierre**, no como análisis confirmatorio preregistrado. No se modifica la versión histórica del protocolo para simular que el procedimiento estaba previsto desde el inicio.

## Evidencia terminal

La evidencia correspondiente se conserva en el bloque de doble codificación preparado para `10_Autoria/doble_codificacion/`, incluyendo las dos hojas, el subconjunto común, el script de kappa y sus resultados.

---

# 5. DEV-AN-03 — Tamaño del efecto técnico vs no técnico añadido en cierre 2B

## Condición previa

Antes del cierre terminal, la comparación entre los tres WALK técnicos y los tres no técnicos se trataba como descriptiva/cualitativa y no se aplicaba una prueba inferencial por participante.

## Situación real

En F3-04 se añadió una medida de tamaño del efecto con IC95 % sobre las categorías temáticas comparables entre perfiles.

## Motivo

La guía específica de cierre exige reportar tamaño del efecto e intervalo de confianza para la comparación técnico vs no técnico.

## Impacto y tratamiento

Se incorpora como análisis **descriptivo-exploratorio**, no como prueba confirmatoria preregistrada. La unidad del cálculo es la categoría temática pareada y no una puntuación independiente por participante. No se genera un p-valor ni se afirma una diferencia poblacional.

## Evidencia terminal

- `06_Experimento/scripts_analisis/calcular_efecto_perfiles.py`
- `06_Experimento/resultados/F3-04_TAMANIO_EFECTO.md`
- `06_Experimento/resultados/tablas/tabla_efecto_perfiles.csv`
- espejo reproducible correspondiente en `07_Datos/`

---

# 6. Condiciones metodológicas registradas que NO se clasifican como nuevas desviaciones

Estas condiciones deben seguir reportándose por transparencia, pero no se presentan como cambios posteriores del protocolo salvo que exista evidencia específica de ello:

- **Normalización de identificadores WALK:** es una corrección de nomenclatura y trazabilidad, no una nueva recolección ni un nuevo análisis.
- **Cuestionario:** el conjunto analítico oficial permanece en `n=70`; no contiene perfil técnico/no técnico ni una escala de explicabilidad por dimensión, por lo que se analiza únicamente dentro del alcance real de sus variables.
- **Saturación:** si el criterio estricto no se alcanza, se reporta como resultado/limitación y no se transforma en una desviación.
- **Member checking sin grabación audiovisual:** la ausencia de grabación se declara como limitación documental; no se fabrica evidencia.
- **Normalización terminal RF/RNF/RD:** es una corrección de especificación y trazabilidad, no una modificación retrospectiva de la evidencia primaria.
- **Corte y proveniencia del cuestionario:** la muestra analítica permanece congelada en el corte documentado; esto se trata como procedencia del conjunto analítico, no como una desviación adicional mientras no contradiga una regla explícita del protocolo.

---

# 7. Regla para futuras actualizaciones

Solo se añadirá una nueva entrada cuando exista:

1. una condición prevista explícitamente por el protocolo;
2. una diferencia real frente a esa condición;
3. una fecha o periodo verificable;
4. un motivo sustentable;
5. evidencia del impacto y del tratamiento aplicado.

Las actividades pendientes no se registran como si ya hubieran ocurrido. Las entradas históricas no se eliminan para hacer coincidir retrospectivamente el protocolo con el estado final.
"""
    text = text.replace("__DEVIATIONS_MD__", "") if False else text
    (ROOT / "osf_deviations.md").write_text(text, encoding="utf-8")
    if ROOT.name == "07_Datos":
        (ROOT / "desviaciones.md").write_text(text, encoding="utf-8")

    reg = pd.DataFrame([
        {
            "ID":"DEV-OSF-01",
            "Fecha_o_periodo":"2026-08-12/2026-08-29",
            "Tipo":"Temporalidad del prerregistro",
            "Condicion_prevista":"Prerregistro formalizado antes de la recolección que se pretenda presentar como confirmatoria",
            "Situacion_real":"Las seis sesiones WALK ocurrieron antes de la publicación OSF del 29/08/2026",
            "Motivo":"El prerregistro se formalizó después de ejecutar las sesiones",
            "Impacto":"Los WALK no se interpretan como datos confirmatorios recogidos bajo protocolo previamente registrado",
            "Tratamiento":"Conservar cronología real; clasificar WALK como evidencia previa/formativa; separar recolección original de análisis posterior",
            "Evidencia":"02_Evidencias/Validacion_walkthrough/ | 06_Experimento/datos_crudos/sesiones_multimedia_desde_ficha_v3_1.csv | 06_Experimento/osf_registration.pdf",
            "Estado":"DOCUMENTADA",
        },
        {
            "ID":"DEV-AN-02",
            "Fecha_o_periodo":"2026-09-05",
            "Tipo":"Análisis adicional de cierre",
            "Condicion_prevista":"Pipeline/prerregistro v1.4 sin medida de acuerdo intercodificador terminal",
            "Situacion_real":"Se incorpora doble codificación >20% y Cohen's kappa con IC95% durante el cierre 2B",
            "Motivo":"Exigencia de la guía terminal específica",
            "Impacto":"No debe presentarse como prueba confirmatoria preregistrada",
            "Tratamiento":"Conservar hojas, subconjunto, script y resultados; declarar el análisis como adicional de cierre",
            "Evidencia":"10_Autoria/doble_codificacion/",
            "Estado":"DOCUMENTADA",
        },
        {
            "ID":"DEV-AN-03",
            "Fecha_o_periodo":"2026-09-05",
            "Tipo":"Análisis adicional de cierre",
            "Condicion_prevista":"Comparación técnico/no técnico tratada previamente como descriptiva/cualitativa sin inferencia por participante",
            "Situacion_real":"Se incorpora tamaño del efecto + IC95% por categorías durante F3-04",
            "Motivo":"Exigencia de la guía terminal específica",
            "Impacto":"No debe interpretarse como hipótesis confirmatoria preregistrada ni como inferencia poblacional",
            "Tratamiento":"Correlación biserial por rangos pareada + IC95% bootstrap; sin p-valor por participante",
            "Evidencia":"06_Experimento/scripts_analisis/calcular_efecto_perfiles.py | 06_Experimento/resultados/F3-04_TAMANIO_EFECTO.md",
            "Estado":"DOCUMENTADA",
        },
    ])
    reg.to_csv(ROOT / "desviaciones_registro.csv", index=False, encoding="utf-8-sig")

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleCenter2", parent=styles["Title"], alignment=TA_CENTER, fontSize=15, leading=18, spaceAfter=10))
    styles.add(ParagraphStyle(name="BodyX", parent=styles["BodyText"], fontSize=9.4, leading=12.7, spaceAfter=6))
    styles.add(ParagraphStyle(name="H2X", parent=styles["Heading2"], fontSize=10.8, leading=13, spaceBefore=6, spaceAfter=3))
    doc = SimpleDocTemplate(str(ROOT / "osf_deviations.pdf"), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm)
    story = [
        Paragraph("FabroGym — Registro de desviaciones reales", styles["TitleCenter2"]),
        Paragraph("Entrega 4 (2B) — protocolo v1.4 / OSF 10.17605/OSF.IO/62YSC", styles["BodyX"]),
    ]
    for row in reg.to_dict("records"):
        story.append(Paragraph(f"{row['ID']} — {row['Tipo']}", styles["H2X"]))
        story.append(Paragraph(f"<b>Fecha/periodo:</b> {row['Fecha_o_periodo']}", styles["BodyX"]))
        story.append(Paragraph(f"<b>Situación real:</b> {row['Situacion_real']}", styles["BodyX"]))
        story.append(Paragraph(f"<b>Motivo:</b> {row['Motivo']}", styles["BodyX"]))
        story.append(Paragraph(f"<b>Impacto:</b> {row['Impacto']}", styles["BodyX"]))
        story.append(Paragraph(f"<b>Tratamiento:</b> {row['Tratamiento']}", styles["BodyX"]))
    story.append(Spacer(1,5))
    story.append(Paragraph("<b>Principio de transparencia.</b> Las limitaciones que no constituyen diferencias reales frente al protocolo se reportan por separado y no se inflan como desviaciones.", styles["BodyX"]))
    doc.build(story)

def main():
    survey, sessions, coding, curve, axial, profile, candidates, fragments, mc = read_inputs()
    vt, at = analyze_multimedia(sessions)
    analyze_survey(survey)
    sat = analyze_walkthroughs(coding, curve, axial, profile)
    effect_script = Path(__file__).with_name("calcular_efecto_perfiles.py")
    subprocess.run([sys.executable, str(effect_script)], check=True)
    final, exp, counts = analyze_explainability(coding, candidates, fragments, mc)
    write_applicability()
    summary = write_summary(survey, sessions, coding, final, exp, counts, vt, at, sat)
    write_osf_deviations(summary)
    print("OK — FabroGym Fase 2 regenerada")
    print(f"Sesiones: {len(sessions)}; video total: {fmt_hms(vt)}; audio total: {fmt_hms(at)}")
    print(f"Encuesta: n={len(survey)}; sin perfil técnico/no técnico; sin Likert de explicabilidad")
    print(f"Walkthroughs: {len(coding)} fragmentos; códigos={coding['Codigo_Normalizado'].nunique()}; categorías={coding['Categoria'].nunique()}")
    print("F3-04: tamaño del efecto técnico/no técnico + IC95% regenerado")
    print(f"Saturación códigos últimas 3: {sat[2]:.3f}% -> {'CUMPLE' if sat[2] <= 5 else 'NO CUMPLE ESTRICTAMENTE'}")
    print(f"Member checking: {int(counts.sum())} decisiones; RNF terminales={len(final)}")

if __name__ == "__main__":
    main()
