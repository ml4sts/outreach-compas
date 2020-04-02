race_score_table = df.groupby(['race','decile_score']).size().reset_index().pivot(index='decile_score',columns='race',values=0)

# percentage of defendants in each score category
(100*race_score_table/race_score_table.sum()).transpose()
