### Equalized Odds

The last fairness metric we consider is based on the difference in *error rates* between groups. Hardt et al. [5](#References) propose to look at the difference in the true positive and false positive rates for each group. This aligns with the analysis performed by Propublica. WE can examine these values looking at is the ROC for each group. We normalize the score between 0 and 1. The ROC thresholds produced by `scikitlearn` are the same.

`%load code/eq`
