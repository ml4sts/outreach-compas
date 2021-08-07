---
jupytext:
  formats: md:myst,ipynb
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

# Replicating Propbulica's COMPAS Audit

## Why COMPAS?


Propublica started the COMPAS Debate with the article [Machine Bias](#References).  With their article, they also released details of their methodology and their [data and code](https://github.com/propublica/compas-analysis).  This presents a real data set that can be used for research on how data is used in a criminal justice setting without researchers having to perform their own requests for information, so it has been used and reused a lot of times.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from sklearn.metrics import roc_curve
import warnings
warnings.filterwarnings('ignore')
```

## Propublica COMPAS Data

The dataset consists of COMPAS scores assigned to defendants over two years 2013-2014 in Broward County, Florida. These scores are determined by a proprietary algorithm designed to evaluate a persons recidivism risk - the likelihood that they will reoffend. Risk scoring algorithms are widely used by judges to inform their scentencing and bail decisions in the criminal justice system in the United States. The original ProPublica analysis identified a number of fairness concerns around the use of COMPAS scores, including that ''black defendants were nearly twice as likely to be misclassified as higher risk compared to their white counterparts.'' Please see the full article for further details.

```{code-cell} ipython3
df_pp = pd.read_csv("https://github.com/propublica/compas-analysis/raw/master/compas-scores-two-years.csv",
                 header=0).set_index('id')

print(list(df))
print(df.head())
```


### Data Cleaning

For this analysis, we will restrict ourselves to only a few features, and clean the dataset according to the methods using in the original ProPublica analysis, we can import that copy version of the data directly.


```{code-cell} ipython3
df = pd.read_csv('https://raw.githubusercontent.com/ml4sts/outreach-compas/main/data/compas_c.csv')
```

## Data Exploration

Next we provide a few ways to look at the relationships between the attributes in the dataset. Here is an explanation of these values:

* `age`: defendant's age
* `c_charge_degree`: degree charged (Misdemeanor of Felony)
* `race`: defendant's race
* `age_cat`: defendant's age quantized in "less than 25", "25-45", or "over 45"
* `score_text`: COMPAS score: 'low'(1 to 5), 'medium' (5 to 7), and 'high' (8 to 10).
* `sex`: defendant's gender
* `priors_count`: number of prior charges
* `days_b_screening_arrest`: number of days between charge date and arrest where defendant was screened for compas score
* `decile_score`: COMPAS score from 1 to 10 (low risk to high risk)
* `is_recid`: if the defendant recidivized
* `two_year_recid`: if the defendant within two years
* `c_jail_in`: date defendant was imprisoned
* `c_jail_out`: date defendant was released from jail
* `length_of_stay`: length of jail stay

In particular, as in the ProPublica analysis, we are interested in the implications for the treatment of different groups as defined by some **protected attribute**. In particular we will consider race as the protected attribute in our analysis. Next we look at the number of entries for each race.


1. Use `value_counts` to look at how much data is available for each race
2. filter to keep data from the two larges groups (help via `%load filter`)

```{code-cell} ipython3
df['race'].value_counts()
```

```{code-cell} ipython3
df = df.loc[df['race'].isin(['African-American','Caucasian'])]
```

### COMPAS score distribution

Let's look at the COMPAS score distribution between African-Americans and Caucasians (matches the one in the ProPublica article).

hint: (use shift + tab for help in any function)
```
race_score_table = df.groupby([]).size().reset_index().pivot(index='',columns='',values=0)

# print percentage of defendants in each score category
(100*/.sum()).transpose()
```

then make a bar plot (quickest way is to use pandas plot with `figsize=[12,7]` to make it bigger, plot type is indicated by the `kind` parameter)


```{code-cell} ipython3
race_score_table = df.groupby(['race','decile_score']).size().reset_index().pivot(
                                index='decile_score',columns='race',values=0)

# percentage of defendants in each score category
(100*race_score_table/race_score_table.sum()).transpose()
```

```{code-cell} ipython3
race_score_table.plot(kind='bar')
```

As you can observe, there is a large discrepancy. Does this change when we condition on other variables?

1. Look at how priors are distributed. Follow what you did above for score by race (or continue for help)
1. Look at how scores are distributed for those with more than two priors
1. What about with less than two priors ?(you can copy or import again the above and modify it)
1. Look at first time (use `priors_count`) felons (`c_charge_degree` of `F`) under 25. How is this different?

```{code-cell} ipython3
priors = df.groupby(['race','priors_count']).size().reset_index().pivot(index='priors_count',columns='race',values=0)
priors.plot(kind='bar',figsize=[12,7])
```

```{code-cell} ipython3
df_2priors = df.loc[df['priors_count']>=2]
score_2priors = df_2priors.groupby(['race','decile_score']).size().reset_index().pivot(
    index='decile_score',columns='race',values=0)
score_2priors.plot(kind='bar',figsize=[15,7])
```

## What happens when we take actual 2-year recidivism values into account? Are the predictions fair?

First, we're going to load a different version of the data, it's quantized. Then look at the correlation between the quantized score, the decile score and the actual recidivism.


The correlation is not that high. How can we evaluate whether the predictions made by the COMPAS scores are fair, especially considering that they do not predict recidivism rates well?

```{code-cell} ipython3
dfQ = pd.load_csv('https://raw.githubusercontent.com/ml4sts/outreach-compas/main/data/compas_cq.csv')
```

```{code-cell} ipython3
# measure with high-low score
dfQ[['two_year_recid','score_text']].corr()
```

```{code-cell} ipython3
# measure with decile_score
dfQ[['two_year_recid','decile_score']].corr()
```

##  Fairness Metrics

The question of how to determine if an algorithm is *fair* has seen much debate recently (see this tutorial from the Conference on Fairness, Acountability, and Transparency titled [21 Fairness Definitions and Their Politics](https://fatconference.org/2018/livestream_vh220.html).

And in fact some of the definitions are contradictory, and have been shown to be mutually exclusive [2,3] https://www.propublica.org/article/bias-in-criminal-risk-scores-is-mathematically-inevitable-researchers-say

Here we will cover 3 notions of fairness and present ways to measure them:

1. **Disparate Impact** [4](#References)
[The 80% rule](https://en.wikipedia.org/wiki/Disparate_impact#The_80.25_rule)

2. **Calibration** [6](#References)

4. **Equalized Odds** [5](#References)

For the rest of our analysis we will use a binary outcome - COMPAS score <= 4 is LOW RISK, >4 is HIGH RISK.

### Disparate Impact

Disparate impact is a legal concept used to describe situations when an entity such as an employer *inadvertently* discriminates gainst a certain protected group. This is distinct from *disparate treatment* where discrimination is intentional.

To demonstrate cases of disparate impact, the Equal Opportunity Commission (EEOC) proposed "rule of thumb" is known as the [The 80% rule](https://en.wikipedia.org/wiki/Disparate_impact#The_80.25_rule).

Feldman et al. [4](#References) adapted a fairness metric from this  principle. For our application, it states that the percent of defendants predicted to be high risk in each protected group (in this case whites and African-Americans) should be within 80% of each other.

Let's evaluate this standard for the COMPAS data.

```{code-cell} ipython3
#  Let's measure the disparate impact according to the EEOC rule
means_score = dfQ.groupby(['score_text','race']).size().unstack().reset_index()
means_score = means_score/means_score.sum()
means_score
# split this cell for the above to print
# compute disparate impact
AA_with_high_score = means_score.loc[1,'African-American']
C_with_high_score = means_score.loc[1,'Caucasian']

C_with_high_score/AA_with_high_score
```

This ratio is below .8, so there is disparate impact by this rule.  (Taking the priveleged group and the undesirable outcome instead of the disadvantaged group and the favorable outcome).

What if we apply the same rule to the **true** two year rearrest instead of the quantized COMPAS score?

```{code-cell} ipython3
means_2yr = dfQ.groupby(['two_year_recid','race']).size().unstack()
means_2yr = means_2yr/means_2yr.sum()
means_2yr

# compute disparte impact
AA_with_high_score = means_2yr.loc[1,'African-American']
C_with_high_score = means_2yr.loc[1,'Caucasian']
C_with_high_score/AA_with_high_score
```

There is a difference in re-arrest, but not as high as assigned by the COMPAS scores. This is still a disparate impact of the actual arrests (since this not necessarily accurate as a recidivism rate, but it is true rearrest).

Now let's measure the difference in scores when we consider both the COMPAS output and true recidivism.

### Calibration

A discussion of using calibration to verify the fairness of a model can be found in Northpoint's (now: Equivant) response to the ProPublica article [6](#References).

The basic idea behind calibrating a classifier is that you want the confidence of the predictor to reflect the true outcomes. So, in a well-calibrated classifier, if 100 people are assigned 90% confidence of being in the positive class, then in reality, 90 of them should actually have had a positive label.

To use calibration as a fairness metric we compare the calibration of the classifier for each group.  The smaller the difference, the more fair the calssifier.

In our problem this can be expressed as given $Y$ indicating two year recidivism, $S_Q$ indicating score (0=low, 1=high medium), and $R$ indicating race, we measure

$$\mathsf{cal} \triangleq \frac{\mathbb{P}\left(Y=1\mid S_Q=s,R=\mbox{African-American} \right)}{\mathbb{P}\left(Y=1 \mid S_Q=s,R=\mbox{Caucasian} \right)},$$ for different scores $s$. Considering our quantized scores, we look at the calibration for $s=1$.


#### Discuss
1. Do you think this is close enough?
1. Which metric do you think is better so far?

```{code-cell} ipython3
# compute averages
dfAverage = dfQ.groupby(['race','score_text'])['two_year_recid'].mean().unstack()

num = dfAverage.loc['African-American',1]
denom = dfAverage.loc['Caucasian',1]
cal = num/denom
calpercent = 100*(cal-1)
print('Calibration: %f' % cal)
print('Calibration in percentage: %f%%' % calpercent)
```

The difference looks much smaller than before. The problem of the above calibration measure is that it depends on the threshold on which we quantized the scores $S_Q$.

In order to mitigate this, ine might use a variation of this measure called *predictive parity.* In this example, we define predictive parity as

$$\mathsf{PP}(s) \triangleq \frac{\mathbb{P}\left(Y=1\mid S\geq s,R=\mbox{African-American} \right)}{\mathbb{P}\left(Y=1 \mid S\geq s,R=\mbox{Caucasian} \right)},$$
where $S$ is the original score.

We plot $\mathsf{PP}(s) $ for $s$ from 1 to 10. Note how predictive parity depends significantly on the threshold.

```{code-cell} ipython3
# aux function for thresh score
def threshScore(x,s):
    if x>=s:
        return 1
    else:
        return 0

ppv_values = []
dfP = dfQ[['race','two_year_recid']].copy()
for s in range(1,11):
    dfP['threshScore'] = dfQ['decile_score'].apply(lambda x: threshScore(x,s))
    dfAverage = dfP.groupby(['race','threshScore'])['two_year_recid'].mean().unstack()
    num = dfAverage.loc['African-American',1]
    denom = dfAverage.loc['Caucasian',1]
    ppv_values.append(100*(num/denom-1))


plt.figure(figsize=[10,10])
plt.plot(range(1,11),ppv_values)
plt.xticks(range(1,11))
plt.xlabel('Score Threshold')
plt.ylabel('Predictive Parity (percentage)')
plt.title('Predictive parity for different thresholds\n(warning: no error bars)')
```

### Equalized Odds

The last fairness metric we consider is based on the difference in *error rates* between groups. Hardt et al. [5](#References) propose to look at the difference in the true positive and false positive rates for each group. This aligns with the analysis performed by Propublica. We can examine these values looking at is the ROC for each group. We normalize the score between 0 and 1. The ROC thresholds produced by `scikitlearn` are the same.



Discuss these results and copmare how these metrics show that there is (or is not) a disparity.

```{code-cell} ipython3
# normalize decile score
max_score = dfQ['decile_score'].max()
min_score = dfQ['decile_score'].min()
dfQ['norm_score'] = (dfQ['decile_score']-min_score)/(max_score-min_score)


plt.figure(figsize=[10,10])
#plot ROC curve for African-Americans
y = dfQ.loc[dfQ['race']=='African-American',['two_year_recid','norm_score']].values
fpr1,tpr1,thresh1 = roc_curve(y_true = y[:,0],y_score=y[:,1])
plt.plot(fpr1,tpr1)

#plot ROC curve for Caucasian
y = dfQ.loc[dfQ['race']=='Caucasian',['two_year_recid','norm_score']].values
fpr2,tpr2,thresh2 = roc_curve(y_true = y[:,0],y_score=y[:,1])
plt.plot(fpr2,tpr2)
l = np.linspace(0,1,10)
plt.plot(l,l,'k--')

plt.xlabel('False Positive Rate')
plt.ylabel('True Postitive Rate')
plt.title('ROC')
plt.legend(['African-American','Caucasian'])
```

# Extension: CORELS


COPMAS has also been criticized for being a generally opaque system. Some machine learning models are easier to understand than others, for example a rule list is easy to understand.
The [CORELS system](https://corels.eecs.harvard.edu/corels/run.html) learns a rule list from the ProPublica data and reports similar accuracy.

```
if ({Prior-Crimes>3}) then ({label=1})
else if ({Age=18-22}) then ({label=1})
else ({label=0})
```

Let's investigate how that score compares.
1. Write a function that takes one row of the data frame and computes the corels function
1. Use `df.apply` to apply your function and add a column to the data frame with the corels score
1. Evaluate the CORELS prediction with respect to accuracy, and fairnss follwing the above

```{code-cell} ipython3
df['age_cat'].value_counts()
```

```{code-cell} ipython3
# %load code/corels

def corels_rule(row):
    if row['priors_count'] > 3:
        return True
    elif row['age'] == 'Less than 25':
        return True
    else:
        return False

df['corels'] = df.apply(corels_rule,axis=1)

#  Let's measure the disparate impact according to the EEOC rule
means_corel = df.groupby(['corels','race']).size().unstack().reset_index()
means_corel = means_corel/means_corel.sum()
means_corel
```
