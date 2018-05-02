r = [[0 for i in range(151)] for j in range(151)]


def cal(n, d):
    if n == 0:
        return 0
    if d == 0:
        return 0
    if d > n:
        return 0
    if d == 1:
        return 1

    count = r[d - 1][n - 1]
    for k in range(d, n):
        for e in range(1, d + 1):
            count += r[d - 1][k - 1] * r[e][n - k]

    count += r[d][n - 1]
    for e in range(2, d):
        for k in range(d, n - e + 1):
            count += r[e - 1][n - k - 1] * r[d][k]
    return count


for d in range(151):
    for n in range(151):
        r[d][n] = cal(n, d)

import sys
for l in sys.stdin:
    l = l.strip()
    if l:
        n, d = map(int, l.split())
        if n % 2 == 0:
            print(r[d][n//2])
        else:
            print(0)

