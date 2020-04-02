df = pd.read_csv("https://github.com/propublica/compas-analysis/raw/master/compas-scores-two-years.csv",
                 header=0).set_index('id')

print(list(df))
print(df.head())
