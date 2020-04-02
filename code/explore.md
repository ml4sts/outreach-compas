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

In particular, as in the ProPublica analysis, we are interested in the implications for the treatment of different groups as defined by some **sensitive data attributes**. In particular we will consider race as the protected attribute in our analysis. Next we look at the number of entries for each race.


<font color=red> Another interesting fairness analysis might be to consider group outcomes by gender or age. In fact, a [2017 appeal to the US Supreme Court](https://en.wikipedia.org/wiki/Loomis_v._Wisconsin) challenged the role of gender in determining COMPAS scores.</font>

1. Use `value_counts` to look at how much data is available for each race
2. filter to keep data from the two larges groups (help via `%load filter`)

Next step: `mdshow(code/dist.md)`
