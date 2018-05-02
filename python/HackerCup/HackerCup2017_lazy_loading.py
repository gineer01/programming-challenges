import fileinput
import math

f = fileinput.input()

t = int(next(f))


def solve(n, weights):
    weights.sort(reverse=True)
    count = 0
    items = 0
    i = 0
    while i < n:
        w = weights[i]
        to_carry = math.ceil(50 / w)

        if items + to_carry <= n:
            count += 1
            items += to_carry
            i += 1
            continue
        else:
            return count

    return count


def solve_case(f):
    n = int(next(f))
    weights = [int(next(f)) for i in range(n)]
    return solve(n, weights)


for i in range(t):
    print("Case #{}: {}".format(i + 1, solve_case(f)))

