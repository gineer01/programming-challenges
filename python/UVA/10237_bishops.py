import fileinput
import collections

f = fileinput.input()


def build_count(vals):
    n = len(vals)
    r = [[0 for i in range(n + 1)] for j in range(n + 1)]
    r[1][1] = vals[0]
    r[1][0] = 1

    for i in range(2, n + 1):
        r[i][0] = 1
        for k in range(1, i + 1):
            r[i][k] = r[i - 1][k] + r[i - 1][k - 1] * (vals[i - 1] - k + 1)

    return r[-1]


def build(n):
    if n == 1:
        return [1, 1]

    diagonals = collections.Counter(i + j for i in range(n) for j in range(n)).most_common()
    diagonals.reverse()
    black = [v for k,v in diagonals if k % 2 == 0]
    white = [v for k,v in diagonals if k % 2 == 1]

    black_count = build_count(black)
    while_count = build_count(white)

    re = []
    for k in range(2*n):
        count = 0
        for i in range(k + 1):
            b = black_count[i] if i < len(black_count) else 0
            j = k - i
            w = while_count[j] if j < len(while_count) else 0
            count += w * b
        re.append(count)
    # print(re)
    return re

cache = [build(i) for i in range(1, 31)]

def solve(n, k):
    if k >= 2*n:
        return 0

    return cache[n - 1][k]

assert solve(2, 1) == 4
assert solve(1, 0) == 1
assert solve(1, 1) == 1


for l in f:
    n, k = map(int, l.split())
    if n == 0 and k == 0:
        break
    print(solve(n, k))

