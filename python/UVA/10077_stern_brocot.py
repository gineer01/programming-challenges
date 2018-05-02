import sys


def solve(m, n):
    target = (m, n)
    if m < n:
        left = (0, 1)
        right = (1, 1)
    else:
        left = (1, 1)
        right = (1, 0)

    result =[]
    p = (1, 1)
    while p != (m, n):
        if p[0]*target[1] < target[0] * p[1]:
            new_p = (p[0] + right[0], p[1] + right[1])
            left = p
            p = new_p
            result.append("R")
        else:
            new_p = (p[0] + left[0], p[1] + left[1])
            right = p
            p = new_p
            result.append("L")

    return "".join(result)


for l in sys.stdin:
    m, n = map(int, l.split())
    if m == 1 and n == 1:
        break
    else:
        print(solve(m, n))

