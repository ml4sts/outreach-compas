The difference looks much smaller than before. The problem of the above calibration measure is that it depends on the threshold on which we quantized the scores $S_Q$.

In order to mitigate this, ine might use a variation of this measure called *predictive parity.* In this example, we define predictive parity as

$$\mathsf{PP}(s) \triangleq \frac{\mathbb{P}\left(Y=1\mid S\geq s,R=\mbox{African-American} \right)}{\mathbb{P}\left(Y=1 \mid S\geq s,R=\mbox{Caucasian} \right)},$$
where $S$ is the original score.

We plot $\mathsf{PP}(s) $ for $s$ from 1 to 10. Note how predictive parity depends significantly on the threshold.

Try this out with `%load code/pp`

Then try the next metric with `mdshow('code/eq.md')`
