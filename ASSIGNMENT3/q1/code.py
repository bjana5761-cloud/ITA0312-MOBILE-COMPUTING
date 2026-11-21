packet_rate=50
interruptions=[0.1,0.2,0.3,0.5]
for t in interruptions:
    print(f'{t:.1f} s interruption -> {packet_rate*t:.0f} packets potentially lost')
