# Corels

COPMAS has also been critcized for being a generally opaque system.

We saw during the interpretability class, the [CORELS system](https://corels.eecs.harvard.edu/corels/run.html). It learns a rule list from the Propulica data and reports similar accuracy.

```
if ({Prior-Crimes>3}) then ({label=1})
else if ({Age=18-22}) then ({label=1})
else ({label=0})
```

Let's investigate how that score compares.
1. Write a function that takes one row of the data frame and computes the corels function
1. Use `df.apply` to apply your function and add a column to the data frame with the corels score
1. Evaluate the CORELS prediction with respect to accuracy, and fairnss follwing the above

Starter code is in `%load code/corels`
