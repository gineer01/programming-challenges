import fileinput

f = fileinput.input()

cases = int(next(f))


def solve(line):
    n = line[0]
    houses = line[1:]
    houses.sort()
    vito = houses[n//2]
    print(sum(map(lambda x: abs(x - vito), houses)))


for i in range(cases):
    solve(list(map(int, next(f).strip().split())))

