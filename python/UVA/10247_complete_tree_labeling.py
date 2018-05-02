from math import factorial

r = [[0 for i in range(22)] for j in range(22)]


def cal(k, d):
    if k == 1:
        return 1
    if d == 0:
        return 1

    n = (k ** (d + 1) - 1) // (k - 1)

    c = factorial(n - 1) // (factorial((n - 1)//k) ** k)

    return c * pow(r[d - 1][k], k)


for k in range(1, 22):
    max_d = 21//k
    for d in range(max_d + 1):
        r[d][k] = cal(k, d)

import sys
for l in sys.stdin:
    l = l.strip()
    if l:
        k, d = map(int, l.split())
        print(r[d][k])

