---
jupyter:
  jupytext:
    formats: md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.10.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```{code-cell} ipython3
pip install ../.
```

```{code-cell} ipython3
import compaslab
tut= compaslab.LiveTutorial('stem_academy.ipynb')
```

```{code-cell} ipython3
for i,curb in enumerate(tut.block_list):
    print(' '.join([str(i),curb,'\n -']),'\n - '.join(list(tut.blocks[curb].keys())))
```

```{code-cell} ipython3
tut.close()
```

```{code-cell} ipython3

```
