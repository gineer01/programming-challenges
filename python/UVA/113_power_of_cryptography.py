import fileinput
import math


def solve(n, p):
    return math.floor(math.pow(p, 1/n) + .5)



def main():
    f = fileinput.input()
    for l in f:
        n = int(l)
        p = int(next(f))
        print(solve(n, p))

main()
