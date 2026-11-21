# Task 2 — Architecture Assumptions vs Measured Reality

The benchmark uses a 2048×2048 image blur and a tiny-task counter-example on a heterogeneous 4-performance + 4-efficiency-core SoC.

Reference result: main-thread blur ≈1,850 ms with 112 janky frames; four workers ≈520 ms with 2 janky frames. A 200-thread locked counter is a counter-example: ≈38 ms versus ≈0.02 ms single-threaded.