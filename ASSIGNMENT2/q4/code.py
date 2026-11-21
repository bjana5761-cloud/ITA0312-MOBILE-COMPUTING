import numpy as np

def jain(x):
    x=np.asarray(x,dtype=float)
    return (x.sum()**2)/(len(x)*(x@x))

rates=np.array([10,8,12,9,11],float)
print('Baseline rates:',rates)
print('Sum throughput:',rates.sum())
print('Jain fairness:',round(jain(rates),4))
print('Design idea: assign each user its strongest available subcarriers while maintaining a minimum-rate constraint.')
