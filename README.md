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
- **Il predominio di SQL e Python**: SQL è la competenza più richiesta per i Data Engineer (68%) e i Data Analyst (51%), mentre Python domina incontrastato per i Data Scientist con una percentuale del 72%. Questi due linguaggi si confermano le fondamenta essenziali dell'ecosistema dati.
- **Differenze nei tool secondari**: i Data Analyst fanno grande affidamento su Excel (41%) e strumenti di BI come Tableau, mentre i Data Engineer si focalizzano su infrastrutture cloud come AWS (43%) e tecnologie per big data come Spark.
- **Sovrapposizione tra Data Scientist e Data Analyst**: Solo per i Data Scientist e i Data Analyst compaiono linguaggi orientati all'analisi statistica pura come R (44%) e SAS, evidenziando una sovrapposizione tra questi due ruoli che invece non compare nel profilo più tecnico e infrastrutturale del Data Engineer.

# 2. Qual è il trend di crescita delle competenze più richieste per i Data Analyst negli USA?

Per analizzare il trend di crescita delle competenze più richieste per i Data Analyst negli USA, abbiamo calcolato la percentuale di ogni competenza rispetto al totale dei lavori per i Data Analyst in ogni mese. Successivamente, abbiamo visualizzato i risultati con un grafico a linee che mostra l'andamento delle top 5 competenze nel tempo.

```python
sns.lineplot(data=df_plot, markers=True, palette='tab10', dashes=False)
sns.set_theme(style='ticks')
sns.despine() # rimuove le spine per un look più pulito
plt.title('Trend of Top 5 Skills for Data Analysts in USA', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Percentage of Job Postings', fontsize=12)
for i in range(5):
    plt.text(11.3, df_plot.iloc[-1, i], df_plot.columns[i], color=sns.color_palette('tab10')[i], fontsize=10)
ax = plt.gca()
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
plt.legend().remove()
plt.xticks(rotation=45)
plt.tight_layout()
```
![Trend of Top 5 Skills for Data Analysts in USA](3_Progetto/images/skills_trend_top5.svg)

Insight Principali:
- **Dominio incontrastato di SQL**: SQL si conferma la competenza più richiesta per tutto l'anno, mantenendosi costantemente sopra la soglia del 50% delle offerte di lavoro. Nonostante una leggera flessione verso fine anno, resta il requisito fondamentale del settore.
- **Stabilità e crescita di Excel**: Excel occupa saldamente la seconda posizione. È interessante notare il trend positivo nell'ultimo trimestre (da ottobre a dicembre), dove recupera terreno suggerendo che la padronanza dei fogli di calcolo rimane un pilastro imprescindibile accanto a linguaggi più complessi.
- **Competizione tra Python e Tableau**: Queste due competenze mostrano un andamento quasi sovrapponibile per gran parte dell'anno, oscillando tra il 25% e il 35%. Ciò indica che per un Data Analyst la capacità di programmazione (Python) e quella di visualizzazione dati (Tableau) hanno un peso specifico molto simile sul mercato.
- **Power BI in crescita costante**: Sebbene sia all'ultimo posto tra le "Top 5", Power BI mostra una crescita graduale e una maggiore stabilità rispetto alla volatilità di Python. Questo suggerisce una crescente adozione degli strumenti dell'ecosistema Microsoft nelle aziende americane.