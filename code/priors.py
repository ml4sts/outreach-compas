priors = df.groupby(['race','priors_count']).size().reset_index().pivot(index='priors_count',columns='race',values=0)
priors.plot(kind='bar',figsize=[12,7])
