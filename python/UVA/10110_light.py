import sys


def solve(n):
    def is_square(n):
        import math
        sqrt = math.floor(math.sqrt(n))
        return n == sqrt ** 2

    if is_square(n):
        return "yes"
    else:
        return "no"


for l in sys.stdin:
    n = int(l)
    if n == 0:
        break
    else:
        print(solve(n))

