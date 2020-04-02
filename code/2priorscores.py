df_2priors = df.loc[df['priors_count']>=2]
score_2priors = df_2priors.groupby(['race','decile_score']).size().reset_index().pivot(index='decile_score',columns='race',values=0)
score_2priors.plot(kind='bar',figsize=[15,7])
