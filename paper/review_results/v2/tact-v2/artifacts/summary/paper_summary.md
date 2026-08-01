# Paper Summary: TACT: Trust-Anchored Confidence Tempering for\\ Self-Consistency Voting in Large Language Models

## Research Question
- Confidence-weighted self-consistency (CISC and its successors) improves on majority voting when a frozen large language model's self-reported confidence is calibrated in direction

## Core Thesis
- This paper presents (Trust-Anchored Confidence Tempering), which replaces the fixed confidence exponent with one derived from the measured, signed, within-item discrimination of the channel: a pooled van~Elteren Somers' rank statistic with an item-clustered standard error, passed through positive-part James--Stein shrinkage and a Bayes-discriminant link.

## Headline Claims
- This paper presents (Trust-Anchored Confidence Tempering), which replaces the fixed confidence exponent with one derived from the measured, signed, within-item discrimination of the channel: a pooled van~Elteren Somers' rank statistic with an item-clustered standard error, passed through positive-part James--Stein shrinkage and a Bayes-discriminant link.
- This paper frames the problem as estimating one scalar: the signed within-item discrimination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent.

## Section Map
- abstract (31-33): 371 words
- introduction (39-54): 706 words
- related (55-64): 272 words
- experiment (206-244): 441 words
- result (245-507): 2203 words
- discussion (508-548): 517 words
- conclusion (549-643): 626 words

## Closure Targets
- Second, an aggregation gain of the size reported on the synthetic harness is not measurable on a benchmark of a few hundred items at these window widths, which is why the real-trace claim in this paper is confined to the premise (the channel exists and is signed) and to the abstention behaviour, and does not extend to accuracy.