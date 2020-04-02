
def corels_rule(row):
    if row['priors_count'] > :
        return
    elif row['age'] :
        return
    else:
        return

df['corels'] = df.apply(corels_rule,axis=1)

#  Let's measure the disparate impact according to the EEOC rule
means_corel = df.groupby(['corels','race']).size().unstack().reset_index()
means_corel = means_corel/means_corel.sum()
means_corel
