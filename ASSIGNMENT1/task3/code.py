# Task 3
import math

def cell_area(R):
    return 2.598 * R * R

def reuse_ratio(N):
    return math.sqrt(3*N)

def sir_db(N, n=3, i0=6):
    return 10*math.log10(reuse_ratio(N)**n/i0)

R=0.62
print("Cell area:", round(cell_area(R),3), "km^2")
for N in [4,7,12]:
    print("N =",N,"Q =",round(reuse_ratio(N),2),"SIR =",round(sir_db(N),2),"dB")
