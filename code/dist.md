### COMPAS score distribution

Let's look at the COMPAS score distribution between African-Americans and Caucasians (matches the one in the ProPublica article).

hint: (use shift + tab for help in any function)
```
race_score_table = df.groupby([]).size().reset_index().pivot(index='',columns='',values=0)

# print percentage of defendants in each score category
(100*/.sum()).transpose()
```

_or get more help with `%load code/racetable`_

then make a bar plot (quickest way is to use pandas plot with `figsize=[12,7]` to make it bigger, plot type is indicated by the `kind` parameter)

Next steps at `mdshow('code/gapexplore')`
