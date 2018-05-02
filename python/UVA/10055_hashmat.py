import fileinput

f = fileinput.input()


def solve(l):
    a, b = list(map(int, l.split()))
    return abs(b - a)


for l in f:
    print(solve(l))
    