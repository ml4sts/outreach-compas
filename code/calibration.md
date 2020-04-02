There is a difference in re-arrest, but not as high as assigned by the COMPAS scores. This is still a disparate impact of the actual arrests (since this not necesarrily accurate as a recidivism rate, but it is true rearrest).

Now let's measure the difference in scores when we consider both the COMPAS output and true recidivism.

### Calibration

A discussion of using calibration to verify the fairness of a model can be found in Northpoint's (now: Equivant) response to the ProPublica article [6](#References).

The basic idea behind calibrating a classifier is that you want the confidence of the predictor to reflect the true outcomes. So, in a well-calibrated classifier, if 100 people are assigned 90% confidence of being in the positive class, then in reality, 90 of them should actually have had a positive label.

To use calibration as a fairness metric we compare the calibration of the classifier for each group.  The smaller the difference, the more fair the calssifier.

In our problem this can be expressed as given $Y$ indicating two year recidivism, $S_Q$ indicating score (0=low, 1=high medium), and $R$ indicating race, we measure

$$\mathsf{cal} \triangleq \frac{\mathbb{P}\left(Y=1\mid S_Q=s,R=\mbox{African-American} \right)}{\mathbb{P}\left(Y=1 \mid S_Q=s,R=\mbox{Caucasian} \right)},$$ for different scores $s$. Considering our quantized scores, we look at the calibration for $s=1$.

compute this with `%load calibration`

#### Discuss
1. Do you think this is close enough?
1. Which metric do you think is better so far?

Next: `mdshow('code/pp.md')`
