# B4 — Multimedia Framework Decision

For a 15-second clip, choose resolution, bitrate and upload timing. The production strategy is O(1): timing first, then highest resolution whose low-bitrate encode time is ≤12 s, then highest bitrate whose upload time is ≤20 s and battery impact is within the threshold.

Timing rule: battery <15% and not charging → wait for charging; otherwise if non-Wi-Fi link <5 Mbit/s → wait for Wi-Fi; otherwise upload now.

The exhaustive model evaluates 4 resolutions × 3 bitrates × 3 timing choices. The heuristic is designed for thousands of devices because it avoids a full search per device.