# Select features that will be analyzed
features_to_keep = ['age', 'c_charge_degree', 'race', 'age_cat', 'score_text', 'sex', 'priors_count',
                    'days_b_screening_arrest', 'decile_score', 'is_recid', 'two_year_recid', 'c_jail_in', 'c_jail_out']
df = df[features_to_keep]
df = clean_compas(df)
df.head()
print("\ndataset shape (rows, columns)", df.shape)
