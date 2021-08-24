# Additional Reading

## COMPAS Debate

This activity replicates the findings of the piece [Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) by Julia Angwin et al at Propublica.
They also published a more detailed [technical description](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm) and their [data and code](https://github.com/propublica/compas-analysis).

Northpointe, the people who developed the tool wrote [a response to ProPublica](https://www.equivant.com/response-to-propublica-demonstrating-accuracy-equity-and-predictive-parity/) and ProPublica wrote [a response to Northpointe](https://www.propublica.org/article/technical-response-to-northpointe).

Researchers then used this dataset to do a lot of different studies a few highlights include:

- [Fairness definitions are incompatible](https://www.propublica.org/article/bias-in-criminal-risk-scores-is-mathematically-inevitable-researchers-say) more on this in the [Fair Machine Learning Textbook Classification Chapter](https://fairmlbook.org/classification.html)
- [COMPAS is only as accurate and fair as untrained people](https://advances.sciencemag.org/content/4/1/eaao5580) [same paper via URI library access](https://advances-sciencemag-org.uri.idm.oclc.org/content/4/1/eaao5580)
- [CORELS](https://corels.eecs.harvard.edu/index.html) is a system that produces a list of rules to predict an outcome, when applied to this data it learns a similarly accurate model with only 3 rules (label=1 is predict recidivism)
```
if ({Prior-Crimes>3}) then ({label=1})
else if ({Age=18-22}) then ({label=1})
else ({label=0})
```

There are, however, risks to drawing conclusions from this dataset.
- [it's COMPASlicated](https://arxiv.org/abs/2106.05498)


## Data Analysis, Python,

For more on general data analysis with python, see Data Carpentry's [Social Sciences](https://datacarpentry.org/python-socialsci/) or [Ecology](https://datacarpentry.org/python-ecology-lesson/) lesson.

The [code](https://github.com/ml4sts/outreach-compas) for this activity is hosted on [GitHub](https://github.com/) if you make an account, you can [contribute](https://github.com/ml4sts/outreach-compas/issues) back your ideas or comment on others' ideas or suggestions.
