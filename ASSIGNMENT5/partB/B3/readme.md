# B3 — Exact vs Approximate UI Optimisation

The exact method evaluates every configuration. The adaptive method performs local search and probes larger cache sizes. On the 4×5×5 grid there are 100 configurations.

Three fixed small instances (seeds 101–103) all reached the exact configuration `(3,5,1)` with the adaptive tuner while evaluating 15 configurations instead of 100. Across seeds 200–399, the tuner matched 178/200 and missed 22/200 (11%).