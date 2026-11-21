# Task 5 — Power Management Reasoning

The task replaces a permanent CPU wake lock with a four-state power model: ACTIVE, IDLE, SUSPENDED and MAINTENANCE/Doze. The key design is to use sensor-hub batching so the application processor can remain suspended.

Reference comparison over 30 minutes: permanent wake lock ≈36 mAh, compliant Doze policy ≈8.4 mAh, deep batching ≈4.1 mAh. A conflicting app with an allow-list, permanent wake lock and exact alarms reached ≈41 mAh and about 212 wake-ups.