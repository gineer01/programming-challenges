import fileinput

f = fileinput.input()

cases = int(next(f))
next(f)


def solve(n, jobs):
    result = [i + 1 for i in range(n)]
    result.sort(key=lambda i: (jobs[i - 1][0]/jobs[i - 1][1], i))
    print(*result)


def solve_case(f):
    n = int(next(f))
    jobs = [tuple(map(int, next(f).split())) for i in range(n)]
    solve(n, jobs)


for i in range(cases):
    if i > 0:
        print()
        next(f)
    solve_case(f)
