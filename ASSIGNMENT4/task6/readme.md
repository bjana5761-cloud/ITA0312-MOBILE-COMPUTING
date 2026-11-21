# Task 6 — Design Challenge: Platform Strategy for RuralCare

RuralCare must support modern Android, iPhone and J2ME/WML feature phones with hours of offline operation, a 10-hour battery target, device-loss protection and exactly-once server delivery.

## Chosen strategy
Use one server-side sync contract with idempotent, acknowledged encrypted batches, but use a native client per device class:
- Android/Kotlin: Room/SQLCipher, Keystore, WorkManager.
- iOS/Swift: Core Data/SQLite, Keychain/Secure Enclave, BGTaskScheduler.
- J2ME: MIDlet + RMS with application-level encryption.

Retain UUID, device ID, monotonically increasing sequence, record state, last ACK, batch checksum, version and tombstones to prevent loss/duplication.

## Battery-aware policy
Normal, conserve, critical, thermal-hold, offline and charging/Wi-Fi flush states are used. Emergency requirements should override deferral with a priority state.