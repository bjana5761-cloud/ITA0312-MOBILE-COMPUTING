# A2 — Safe Incremental Synchronisation

Synchronise only dirty records, order by priority and size, and choose Upload / Defer / Conflict Resolution. Unsafe sensitive records, unavailable network, low battery, budget limits and stale server versions cause pruning or deferral.

Important offline-first correction: never discard a local operation merely because the remote copy is newer; retain an operation log/version information and reconcile safely when connectivity returns.