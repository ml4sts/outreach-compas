---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# How to fix common errors


## Fix it yourself


1. If you see something like `pd is not defined` look for a cell that includes
`import pandas as pd` and make sure that is has been run.
1. If you see `NameError` Check that all of the code cells have a number to the left that says that they have run. If they have not, click on each one that has not yet run, and run that one again.

    ```{code-cell} ipython3
    # this cell is run and has output
    4+3
    ```
    ```{code-cell} ipython3
    # this cell is run and has no output
    ```

    ```
    # this cell is not run
    4+3
    ```
1. If you see output like `<bound method ...` check that you used `tut.next()`
with the `()`
1. To go back, use `tut.previous()` or `tut.previous(3)` to go back 3 steps, you
can go back any number of steps
1. To repeat a step use `tut.repeat()`



## Useful cells to copy

These bits are common lines that are useful to copy, but knowing when to use
them might require the advice of a a TA or helper.

original dataset:
```
df_pp = pd.read_csv("https://github.com/propublica/compas-analysis/raw/master/compas-scores-two-years.csv", header=0).set_index('id')
```

clean dataset:

```
df = pd.read_csv('https://raw.githubusercontent.com/ml4sts/outreach-compas/main/data/compas_c.csv')
```

quantized dataset:

```
dfQ = pd.read_csv('https://raw.githubusercontent.com/ml4sts/outreach-compas/main/data/compas_cq.csv')
```
