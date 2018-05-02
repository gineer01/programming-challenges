import sys


def solve(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1

    v = n * (n - 1) * (n - 2) * (n - 3) // 24 + n
    e = ((n - 1) * (n - 2) * (n - 3) // 6 + n - 1) * n // 2 + n
    f = 1 + e - v
    return f

s = int(next(sys.stdin))

for i in range(s):
    n = int(next(sys.stdin))
    print(solve(n))

