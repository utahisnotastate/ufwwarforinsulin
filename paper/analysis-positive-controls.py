# -*- coding: utf-8 -*-
"""Specificity analysis for the neutral re-query arm.

Experiment 2 probed seven concepts whose correct outcome answer was "no" and got 6/6
(one probe terminated on a safety classifier). External peer review correctly observed
that this measures sensitivity without specificity: a model with a blanket sceptical
prior toward novel therapies scores 6/6 knowing nothing.

Experiment 6 probed seven concepts whose correct outcome answer is "yes", matched in
format, framing, model and isolation, pre-registered, with ground truth committed first.

Run:  python analysis-positive-controls.py
"""
from math import comb, sqrt

# Experiment 2 — correct answer is "no". Scored in RESULTS.md.
NEGATIVE = {
    "C-peptide":                  "no",
    "Glucose-responsive insulin": "no",
    "Hepato-preferential":        "no",
    "Transdifferentiation":       "no",
    "Non-insulin disposal":       "no",
    "Decentralised manufacture":  "no",
}
# Experiment 6 — correct answer is "yes". Scored in data-positive-controls-scoring.md.
POSITIVE = {
    "Stem-cell islets":    "yes",
    "Teplizumab":          "yes",
    "Metabolic surgery":   "yes",
    "Hybrid closed loop":  "yes",
    "CGM":                 "yes",
    "Intensive control":   "yes",
    "SGLT2 inhibitors":    "yes",
}

def hyp(a, b, c, d):
    return comb(a + b, a) * comb(c + d, c) / comb(a + b + c + d, a + c)

def fisher(a, b, c, d):
    obs = hyp(a, b, c, d); r1, r2, c1 = a + b, c + d, a + c; p = 0.0
    for i in range(0, min(r1, c1) + 1):
        j, k = r1 - i, c1 - i; l = r2 - k
        if j < 0 or k < 0 or l < 0:
            continue
        pr = hyp(i, j, k, l)
        if pr <= obs + 1e-12:
            p += pr
    return p

def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))

# a = negative-direction questions answered "no" (correct)
a = sum(1 for v in NEGATIVE.values() if v == "no")
b = len(NEGATIVE) - a
d = sum(1 for v in POSITIVE.values() if v == "yes")
c = len(POSITIVE) - d

print("=" * 78)
print("Question direction x answer direction")
print("=" * 78)
print("                               answered no   answered yes")
print("  correct answer is no  (n=%d)       %2d            %2d" % (len(NEGATIVE), a, b))
print("  correct answer is yes (n=%d)       %2d            %2d" % (len(POSITIVE), c, d))
print()

lo, hi = wilson(a, len(NEGATIVE))
print("  sensitivity  %d/%d = %3.0f%%   (Wilson 95%% CI %2.0f-%3.0f%%)"
      % (a, len(NEGATIVE), 100 * a / len(NEGATIVE), 100 * lo, 100 * hi))
lo, hi = wilson(d, len(POSITIVE))
print("  specificity  %d/%d = %3.0f%%   (Wilson 95%% CI %2.0f-%3.0f%%)"
      % (d, len(POSITIVE), 100 * d / len(POSITIVE), 100 * lo, 100 * hi))
n = len(NEGATIVE) + len(POSITIVE)
lo, hi = wilson(a + d, n)
print("  overall     %2d/%d = %3.0f%%   (Wilson 95%% CI %2.0f-%3.0f%%)"
      % (a + d, n, 100 * (a + d) / n, 100 * lo, 100 * hi))
print()

p = fisher(a, b, c, d)
print("  Fisher's exact, two-sided p = %.5f" % p)
print("    = 2/C(%d,%d) = 2/%d, the floor of this design." % (n, len(NEGATIVE), comb(n, len(NEGATIVE))))
print("    Perfect separation; the p-value carries no information beyond that.")
print()
print("  H0: the model answers 'no' by default (blanket scepticism).")
print("      Under H0, expected correct on the positive controls = 0/%d." % len(POSITIVE))
print("      Observed %d/%d. Exact binomial, one-sided, generous H0 (p_yes <= 0.5): p = %.5f"
      % (d, len(POSITIVE), 0.5 ** len(POSITIVE)))
print("      H0 is excluded.")
print()
print("  Residual alternative NOT excluded: the model may discriminate 'established' from")
print("  'speculative' rather than tracking evidence. Every negative concept was a failed")
print("  programme; every positive one is in guidelines. Separating these requires concepts")
print("  that are established-but-ineffective or unestablished-but-effective. None was probed.")
