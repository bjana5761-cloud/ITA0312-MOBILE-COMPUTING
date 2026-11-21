# Task 3 — Runtime Behaviour Under Changing Execution Conditions

RuntimeBench covers CPU-bound prime counting, allocation-heavy object creation and a UI list. The task also develops the Android launch sequence and compares interpretation/JIT/AOT across Android ART, iOS and Windows.

Reference cold/warm start: 742 ms / 281 ms. Allocation-heavy workload grows the heap from about 11 MB to 27 MB and falls back to about 12 MB after GC, which is consistent with healthy collection rather than monotonic leak growth.