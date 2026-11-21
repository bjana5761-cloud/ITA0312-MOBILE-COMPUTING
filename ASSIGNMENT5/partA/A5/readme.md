# A5 — UI Approximation Design

The exact search guarantees the minimum model cost but grows with the product of parameter ranges. The adaptive tuner uses local moves, a cache-ceiling probe and measured QoS to reach a good configuration quickly.

The assignment reports that the tuner matched the exact optimum on 178/200 instances (89%) and missed 22/200 (11%). The worst counter-example was seed 254, where the adaptive cost was 83.07 versus an exact optimum of 24.34 (241% worse).