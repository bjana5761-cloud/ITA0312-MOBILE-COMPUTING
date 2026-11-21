def start_mode(mode):
    steps={'cold':10,'warm':7,'hot':3}
    print(mode,'start path steps:',steps[mode])
for m in ('cold','warm','hot'): start_mode(m)
print('Reference cold start: 742 ms')
print('Reference warm start: 281 ms')
print('Heap: 11 MB -> 27 MB -> 12 MB after GC')
