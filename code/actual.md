## What happens when we take actual 2-year recidivism values into account? Are the predictions fair?

First quantize the data
`%load code/quantize`

First, let's look at the correlation between the quantized score, the decile score and the actual recidivism.

```
# measure with high-low score
print(dfQ[['two_year_recid','score_text']].corr())

# measure with decile_score
print(dfQ[['two_year_recid','decile_score']].corr())
```

The correlation is not that high. How can we evaluate whether the predictions made by the COMPAS scores are fair, especially considering that they do not predict recidivism rates well? `mdshow('code/fair.md')`
