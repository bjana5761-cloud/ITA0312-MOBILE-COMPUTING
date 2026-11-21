import random

# Simplified reproducible store-and-forward experiment from Q1.
def simulate(availability, readings=2000, seed=7, buffer_size=50):
    random.seed(seed)
    immediate_lost=0
    delivered=0
    queue=[]
    delays=[]
    for minute in range(readings):
        online=random.random() < availability
        if online:
            delivered += len(queue)
            delays.extend([1]*len(queue))
            queue.clear()
            delivered += 1
        else:
            immediate_lost += 1
            if len(queue)<buffer_size:
                queue.append(minute)
    return immediate_lost, delivered, len(queue)

for a in (0.90,0.60,0.30):
    lost, delivered, queued=simulate(a)
    print(f"Availability {a:.0%}: immediate lost={lost}, queued-delivered={delivered}, buffer remaining={queued}")
