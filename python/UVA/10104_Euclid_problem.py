def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


import sys

for l in sys.stdin:
    a, b = map(int, l.split())
    g, x, y = egcd(a, b)

    if x < y:
        x2 = x + b//g
        y2 = y - a//g
    else:
        x2 = x - b//g
        y2 = y + a//g

    s1 = abs(x) + abs(y)
    s2 = abs(x2) + abs(y2)
    if s1 < s2:
        print(x, y, g)
    elif s2 < s1:
        print(x2, y2, g)
    else:
        if x > y:
            x = x2
            y = y2
        print(x, y, g)


