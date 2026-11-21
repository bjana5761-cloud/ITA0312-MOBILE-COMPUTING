# A1 — Constraint-aware Intent & Service Architecture

Model the background-work problem as a persisted constrained search. The scheduler checks network, battery, permission, Doze, data sensitivity, encryption, deadline and concurrency constraints before starting work.

The trace in the assignment contains four work items R1, R2, R3 and A1. At the end: R1 and A1 succeed, R2/R3 are cancelled after policy change, 150 KB is wasted, and the critical deadline is met.