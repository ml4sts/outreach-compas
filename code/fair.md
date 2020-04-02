

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

Feldman et al. [4](#References) adapted a fairness metric from this  principle. For our application, it states that the percent of defendants predicted to be high risk in each protected group (in this case whites and african-americans) should be within 80% of each other.

Let's evaluate this standard for the COMPAS data.

`%load code/di` then `mdshow('code/evaldi.md')`
