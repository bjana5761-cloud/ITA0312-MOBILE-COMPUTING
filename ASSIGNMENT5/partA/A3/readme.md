# A3 — Mobile-background Design Pattern

The three problems are background sensor collection, offline data synchronisation and push-notification delivery. All share the same pattern: persisted state, candidate actions, feasibility checks, resource budgets, pruning/deferral, execution and UNDO/cancellation.

UNDO is essential because Doze, network loss, low battery, permission changes or process death can stop work after partial state changes.