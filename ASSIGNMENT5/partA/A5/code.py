def greedy_tune(config, neighbours, cost):
    current=config
    while True:
        options=[(cost(n),n) for n in neighbours(current)]
        better=[x for x in options if x[0]<cost(current)]
        if not better: return current,cost(current)
        current=min(better)[1]

print('Adaptive UI tuning: start -> evaluate neighbours -> choose improving move -> stop at local optimum')
