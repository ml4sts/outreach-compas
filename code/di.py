#  Let's measure the disparate impact according to the EEOC rule
means_score = dfQ.groupby(['score_text','race']).size().unstack().reset_index()
means_score = means_score/means_score.sum()
means_score
# split this cell for the above to print
# compute disparate impact
AA_with_high_score = means_score.loc[1,'African-American']
C_with_high_score = means_score.loc[1,'Caucasian']

C_with_high_score/AA_with_high_score
