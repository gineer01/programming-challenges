import sys


def solve(x):
    i = 1
    mod = 9*x
    while pow(10, i, mod) != 1:
        i += 1
    return i


for l in sys.stdin:
    print(solve(int(l)))

