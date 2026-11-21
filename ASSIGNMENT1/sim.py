import math
import numpy as np

def erlang_b(A, c):
    B = 1.0
    for k in range(1, c + 1):
        B = A * B / (k + A * B)
    return B

def erlang_cap(c, gos=0.02):
    lo, hi = 0.0, c * 2.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if erlang_b(mid, c) > gos:
            hi = mid
        else:
            lo = mid
    return lo

def sir_analytic(N, n=3.0, interferers=6):
    Q = math.sqrt(3 * N)
    return 10 * math.log10(Q ** n / interferers)

def main():
    print('Assignment 1 — Mobile Computing CO1')
    print('S1 N=12 omni :', round(sir_analytic(12), 2), 'dB')
    print('S2a N=7 120deg:', round(sir_analytic(7, 3, 2), 2), 'dB')
    print('S2b N=4 60deg :', round(sir_analytic(4, 3, 1), 2), 'dB')
    print('\nErlang-B traffic at 2% blocking:')
    for c in (14, 16, 28, 48, 84, 336):
        print(c, 'channels ->', round(erlang_cap(c), 2), 'Erlang')

if __name__ == '__main__':
    main()
