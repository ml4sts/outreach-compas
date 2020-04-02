means_2yr = dfQ.groupby(['two_year_recid','race']).size().unstack()
means_2yr = means_2yr/means_2yr.sum()
means_2yr

# compute disparte impact
AA_with_high_score = means_2yr.loc[1,'African-American']
C_with_high_score = means_2yr.loc[1,'Caucasian']
C_with_high_score/AA_with_high_score
