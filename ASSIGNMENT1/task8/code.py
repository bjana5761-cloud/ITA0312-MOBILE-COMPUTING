# Task 8
import math

def erlang_b(A,c):
    B=1.0
    for k in range(1,c+1): B=A*B/(k+A*B)
    return B

for c,A in [(14,8.20),(16,9.83),(28,20.15)]:
    print(c,"channels,",A,"E ->",round(erlang_b(A,c)*100,3),"% blocking")
