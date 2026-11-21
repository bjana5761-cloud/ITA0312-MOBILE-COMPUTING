import math

def shared_slots(devices, report_bits=1600, slot_rate=24700):
    aggregate=devices*report_bits/60
    return max(1,math.ceil(aggregate/slot_rate))

for n in (500,1000,2000,5000):
    print(f'{n} devices -> approx shared slots needed per minute: {shared_slots(n)}')
print('Redesign principle: short reports share a small pool; devices contend/reserve instead of owning one dedicated channel each.')
