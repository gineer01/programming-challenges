import sys
import math


def solve(x, y):
    t = y - x
    k = math.floor(math.sqrt(t + .25) - 0.5)
    g = t - (k * (k + 1))
    if g == 0:
        return 2 * k
    elif g <= k + 1:
        return 2 * k + 1
    else:
        return 2 * k + 2

assert solve(0, 1) == 1
assert solve(0, 2) == 2
assert solve(0, 3) == 3
assert solve(0, 4) == 3
assert solve(0, 5) == 4

n = int(next(sys.stdin))
for i in range(n):
    x, y = map(int, next(sys.stdin).split())
    print(solve(x, y))

