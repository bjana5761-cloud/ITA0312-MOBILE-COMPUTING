# Task 4 — Secure Mobile Application Audit

The SecureNotes audit uses STRIDE against permissions, data stores, network endpoints and exported components. Major defects include over-requested permissions, plaintext login token storage, unverified update source and cleartext HTTP.

Repairs: least privilege/runtime permission requests, Keystore-protected tokens, verified same-signer updates and TLS 1.3 with certificate pinning. Regression testing must preserve legitimate contact attachment and secure sync.