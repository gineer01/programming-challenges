import sys
import math


def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def solve(n, c1, c2, a, b):
    g, x, y = egcd(a, b)
    if n % g != 0:
        return None

    swap = False
    if y < 0:
        a, b = b, a
        x, y = y, x
        c1, c2 = c2, c1
        swap = True

    t = n // g

    x *= t
    y *= t

    kx = math.ceil((-x) * g / b)
    ky = math.floor((y) * g / a)
    if ky < kx:
        return None
    if c1/a > c2/b:
        k = kx
    else:
        k = ky
    r = x + (k * b // g), y - (k * a // g)
    if swap:
        return r[::-1]

    return r

assert solve(43, 2, 1, 4, 3) == (1, 13)
assert solve(6, 1, 1, 3, 3) == (2, 0)
assert solve(43, 1, 2, 3, 4) == (13, 1)
assert solve(9990, 3, 88, 3, 89) == (37, 111)

for l in sys.stdin:
    n = int(l)
    if n == 0:
        break
    c1, n1 = map(int, next(sys.stdin).split())
    c2, n2 = map(int, next(sys.stdin).split())
    r = solve(n, c1, c2, n1, n2)
    if r:
        print(*r)
    else:
        print("failed")

