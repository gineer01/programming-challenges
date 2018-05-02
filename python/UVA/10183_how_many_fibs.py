import sys
import bisect

f = [1, 2]
a, b = 1, 2
limit = 10 ** 100

while b < limit:
    c = a + b
    f.append(c)
    a = b
    b = c


def solve(a, b):
    left = bisect.bisect_left(f, a)
    right = bisect.bisect_right(f, b)
    return right - left


for l in sys.stdin:
    a, b = map(int, l.split())
    if a == 0 and b == 0:
        break
    else:
        print(solve(a, b))

