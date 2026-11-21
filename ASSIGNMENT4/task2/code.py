single_ms=1850
workers_ms=520
print('4-worker speedup:',round(single_ms/workers_ms,2),'x')
print('Main-thread janky frames: 112; worker design: 2')
print('Tiny task: single 0.02 ms; 200 threads + one lock 38 ms')
print('Lesson: parallelism granularity matters; thread creation and lock contention can dominate useful work.')
