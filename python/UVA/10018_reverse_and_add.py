import fileinput

f = fileinput.input()

cases = int(next(f))

def solve(p):
    count = 0
    s = str(p)
    r = s[::-1]
    while s != r:
        p += int(r)
        count += 1

        s = str(p)
        r = s[::-1]

    return count, p


for i in range(cases):
    print(*solve(int(next(f))))

