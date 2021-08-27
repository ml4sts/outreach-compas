---
jupytext:
  formats: md:myst
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

# Instructor Notes

## Preparation

Always, remember to uninstall first so that you install the same version as the
learners



## Key points Notebook Tour

- edit/command modes
- run vs not run cells
- code cells vs markdown cells
- add, delete, restart, run





## Activity Outlines for Live tutorials

```
pip uninstall compaslab
```

```{code-cell} ipython3
pip install ../.
```

```{code-cell} ipython3
import compaslab
```

### STEM Academy
```{code-cell} ipython3
tut= compaslab.LiveTutorial('stem_academy.ipynb')

for i,curb in enumerate(tut.block_list):
    print(' '.join([str(i),curb,'\n -']),'\n - '.join(list(tut.blocks[curb].keys())))
```

```{code-cell} ipython3
tut= compaslab.LiveTutorial('stem_academy_hints.ipynb')

for i,curb in enumerate(tut.block_list):
    print(' '.join([str(i),curb,'\n -']),'\n - '.join(list(tut.blocks[curb].keys())))
```


Wrap up
```{code-cell} ipython3
tut.close()
```
