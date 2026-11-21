# B1 — Instrumented Background Architecture

The simulator models WorkManager-style scheduling with MAXW=3, battery and network constraints, Doze windows, permission changes, retries and exponential back-off.

The priority version uses: `100*[prio=3] + 20*prio + age - size/20`, reserves one lane for critical work, and never relaxes feasibility constraints.

Reported stress result: 40 items; deferral decisions fall from 593 item-ticks (FIFO) to 520 (-12.3%). Wasted KB falls from 600 to 120 on the main workload; over 30 seeds it falls from 375.33 to 259.67.