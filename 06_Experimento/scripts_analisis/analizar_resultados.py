#!/usr/bin/env python3
"""Calcula métricas, acuerdo y figuras a partir de los datos crudos."""
from __future__ import annotations
import argparse, csv
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, confusion_matrix, cohen_kappa_score
from statsmodels.stats.inter_rater import fleiss_kappa
from statsmodels.stats.contingency_tables import mcnemar

SEED=401

def bootstrap_ci(y_true, y_pred, metric, n=5000):
    rng=np.random.default_rng(SEED); vals=[]; N=len(y_true)
    for _ in range(n):
        idx=rng.integers(0,N,N)
        try: vals.append(metric(y_true[idx],y_pred[idx]))
        except Exception: pass
    return np.quantile(vals,[.025,.975]) if vals else (np.nan,np.nan)

def run(detector_csv:Path, eval_csv:Path, consensus_csv:Path, out_dir:Path):
    out_dir.mkdir(parents=True,exist_ok=True); (out_dir/'figuras').mkdir(exist_ok=True)
    d=pd.read_csv(detector_csv); e=pd.read_csv(eval_csv); c=pd.read_csv(consensus_csv)
    m=d.merge(c,on='rf_id',validate='one_to_one')
    if m['consenso_ambiguo_0_1'].isna().any(): raise ValueError('Hay empates o consensos pendientes.')
    yt=m['consenso_ambiguo_0_1'].astype(int).to_numpy(); yp=m['detector_ambiguo_0_1'].astype(int).to_numpy()
    metrics=[]
    funcs={'precision':lambda a,b:precision_score(a,b,zero_division=0),'recall':lambda a,b:recall_score(a,b,zero_division=0),'f1':lambda a,b:f1_score(a,b,zero_division=0),'exactitud':accuracy_score}
    for name,fn in funcs.items():
        v=fn(yt,yp); lo,hi=bootstrap_ci(yt,yp,fn)
        metrics.append({'metrica':name,'valor':v,'ic95_inf':lo,'ic95_sup':hi})
    pd.DataFrame(metrics).to_csv(out_dir/'metricas_detector.csv',index=False,encoding='utf-8-sig')
    cm=confusion_matrix(yt,yp,labels=[0,1]); tn,fp,fn,tp=cm.ravel()
    pd.DataFrame([{'TN':tn,'FP':fp,'FN':fn,'TP':tp}]).to_csv(out_dir/'matriz_confusion.csv',index=False,encoding='utf-8-sig')
    table=[[tn,fp],[fn,tp]]; mc=mcnemar(table,exact=True)
    pd.DataFrame([{'estadistico':mc.statistic,'p_valor':mc.pvalue,'metodo':'McNemar exacta bilateral'}]).to_csv(out_dir/'prueba_mcnemar.csv',index=False,encoding='utf-8-sig')
    # Pairwise Cohen kappa.
    wide=e.pivot(index='rf_id',columns='evaluador_id',values='ambiguo_0_no_1_si').dropna()
    pairs=[]; cols=list(wide.columns)
    for i in range(len(cols)):
        for j in range(i+1,len(cols)):
            pairs.append({'evaluador_a':cols[i],'evaluador_b':cols[j],'kappa_cohen':cohen_kappa_score(wide[cols[i]],wide[cols[j]]),'n':len(wide)})
    pd.DataFrame(pairs).to_csv(out_dir/'kappa_pares.csv',index=False,encoding='utf-8-sig')
    # Fleiss matrix: rows items, cols categories 0/1 counts.
    mat=[]
    for _,r in wide.iterrows():
        vals=r.astype(int).to_numpy(); mat.append([(vals==0).sum(),(vals==1).sum()])
    fk=float(fleiss_kappa(np.asarray(mat)))
    pd.DataFrame([{'kappa_fleiss':fk,'n_requisitos':len(mat),'n_evaluadores':wide.shape[1]}]).to_csv(out_dir/'kappa_fleiss.csv',index=False,encoding='utf-8-sig')
    # Disagreements.
    dis=m[m['detector_ambiguo_0_1'].astype(int)!=m['consenso_ambiguo_0_1'].astype(int)].copy()
    dis.to_csv(out_dir/'desacuerdos.csv',index=False,encoding='utf-8-sig')
    # Figures.
    md=pd.DataFrame(metrics)
    fig,ax=plt.subplots(figsize=(7,4)); ax.bar(md['metrica'],md['valor']); ax.set_ylim(0,1); ax.set_ylabel('Valor'); ax.set_title('Rendimiento del detector'); fig.tight_layout(); fig.savefig(out_dir/'figuras'/'metricas_detector.png',dpi=200); fig.savefig(out_dir/'figuras'/'metricas_detector.svg'); plt.close(fig)
    fig,ax=plt.subplots(figsize=(5,4)); im=ax.imshow(cm); ax.set_xticks([0,1],labels=['No ambiguo','Ambiguo']); ax.set_yticks([0,1],labels=['No ambiguo','Ambiguo']); ax.set_xlabel('Detector'); ax.set_ylabel('Consenso experto'); ax.set_title('Matriz de confusión');
    for i in range(2):
        for j in range(2): ax.text(j,i,cm[i,j],ha='center',va='center')
    fig.tight_layout(); fig.savefig(out_dir/'figuras'/'matriz_confusion.png',dpi=200); fig.savefig(out_dir/'figuras'/'matriz_confusion.svg'); plt.close(fig)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--detector',type=Path,default=Path('resultados/salida_detector.csv')); ap.add_argument('--evaluaciones',type=Path,default=Path('resultados/evaluaciones_expertos.csv')); ap.add_argument('--consenso',type=Path,default=Path('resultados/consenso_experto.csv')); ap.add_argument('--salida',type=Path,default=Path('resultados')); a=ap.parse_args(); run(a.detector,a.evaluaciones,a.consenso,a.salida)
