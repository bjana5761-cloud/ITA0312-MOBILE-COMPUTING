# Task 7
import math

def split_rounds(demand, capacity):
    if demand <= capacity: return 0
    return math.ceil(math.log(demand/capacity,4))

for D,C in [(100,50),(500,50),(1000,50),(2500,50)]:
    print("Demand",D,"Capacity",C,"-> rounds",split_rounds(D,C))
