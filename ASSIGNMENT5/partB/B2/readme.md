# B2 — Adversarial Workload

Two adversarial cases stress the scheduler: connectivity flapping and permission revocation. The important observation is that the scheduler must defer work when the network disappears and cancel sensitive work after consent is revoked.

The assignment's T3b result: 25 items delivered and 15 cancelled after permission revocation; critical delivery was 4/8 because later critical items arrived after revocation.