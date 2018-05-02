import fileinput

f = fileinput.input()


def solve(l):
    a, b = list(map(int, l.split()))
    return a*b*2


for l in f:
    print(solve(l))
