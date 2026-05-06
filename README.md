# Le analisi

# 1. Quali sono le competenze più richieste per i top 3 titoli di lavoro sui dati negli USA?

Per trovare le competenze più richieste per i top 3 titoli di lavoro sui dati negli USA, abbiamo prima contato il numero di competenze associate a ciascun titolo di lavoro. Successivamente, abbiamo calcolato la percentuale di ogni competenza rispetto al totale dei lavori per quel titolo. Infine, abbiamo visualizzato i risultati con un grafico a barre che mostra la percentuale di ogni competenza per i top 5 lavori associati a ciascun titolo di lavoro.

Puoi vedere il codice completo e i risultati nella sezione [2_Skills_Count.ipynb](3_Progetto/2_Skills_Count.ipynb).

```python
sns.set_theme(style='ticks')
fig, ax = plt.subplots(len(job_titles), 1, figsize=(10, 6))
for i, job_title in enumerate(job_titles):
    df_plot = df_skills_perc[df_skills_perc['job_title_short'] == job_title].head(5)
    sns.barplot(x='skill_perc', y='job_skills', data=df_plot, ax=ax[i], hue='skill_perc', palette = 'dark:b_r', legend=False)
    sns.despine(left=True, bottom=True)
    ax[i].set_title(job_title)
    ax[i].set_xlabel('')
    ax[i].set_ylabel('')
    ax[i].set_xlim(0, 78)
    
    if i < len(job_titles) - 1:
        ax[i].set_xticks([])
    for n, v in enumerate(df_plot['skill_perc']):
        ax[i].text(v + 1, n, f'{v:.0f}%', color='black', va='center')
fig.suptitle('Likelihood of Skills per Job Title in USA', fontsize=16)
fig.tight_layout(h_pad=1)
```

![Skills per Job Title](3_Progetto/images/skills_perc_job_title.svg)

Insight Principali:
- Il predominio di SQL e Python: SQL è la competenza più richiesta per i Data Engineer (68%) e i Data Analyst (51%), mentre Python domina incontrastato per i Data Scientist con una percentuale del 72%. Questi due linguaggi si confermano le fondamenta essenziali dell'ecosistema dati.
- Si nota una netta distinzione nelle skill secondarie: i Data Analyst fanno grande affidamento su Excel (41%) e strumenti di BI come Tableau, mentre i Data Engineer si focalizzano su infrastrutture cloud come AWS (43%) e tecnologie per big data come Spark.
- Solo per i Data Scientist e i Data Analyst compaiono linguaggi orientati all'analisi statistica pura come R (44%) e SAS, evidenziando una sovrapposizione tra questi due ruoli che invece non compare nel profilo più tecnico e infrastrutturale del Data Engineer.