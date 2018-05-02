import sys
import math


def solve(n, k, coef):
    numer = math.factorial(n)
    denom = 1
    for i in range(k):
        if coef[i] > 0:
            denom *= math.factorial(coef[i])
    return numer//denom


for l in sys.stdin:
    n, k = map(int, l.split())
    coef = list(map(int, next(sys.stdin).split()))
    print(solve(n, k, coef))

