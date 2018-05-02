import sys
import math


def solve(x):
    if 2 <= x <= 9:
        return "Stan wins."
    elif 10 <= x <= 18:
        return "Ollie wins."
    else:
        return solve(math.ceil(x / 18))

for l in sys.stdin:
    print(solve(int(l)))

