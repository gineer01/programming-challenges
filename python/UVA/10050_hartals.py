import fileinput

f = fileinput.input()

t = int(next(f))

def solve(n, p, parties):
    sim = [False] * n
    for i in range(p):
        hartal = parties[i]
        for j in range(hartal - 1, n, hartal):
            sim[j] = True

    count = 0
    for i in range(n):
        if i % 7 == 5 or i % 7 == 6:
            continue
        if sim[i]:
            count += 1

    return count


def solve_case(f):
    n = int(next(f))
    p = int(next(f))
    parties = [int(next(f)) for i in range(p)]

    print(solve(n, p, parties))


for i in range(t):
    solve_case(f)
