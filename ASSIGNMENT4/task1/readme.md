# Task 1 — Analyse and Validate a Mobile OS Model

The task maps Android, iOS and Windows architecture, validates lifecycle/process behaviour and tests a boundary case. Android uses Linux/GKI, ART and zygote; iOS uses XNU and native Objective-C/Swift runtime; Windows uses NT/WinRT.

Boundary test: process death while a dialog contains unsaved text. The recommended repair is SavedStateHandle/rememberSaveable and lifecycle-scoped work.