import fileinput
import re

f = fileinput.input()

t = int(next(f))

pattern = re.compile(r"(\d+)d(\d+)(([+-])(\d+))?")

lookup = {}


def value_s_n_dice_x(s, n, x):
    import math

    def C(n, k):
        f = math.factorial
        assert n >= 0, n
        assert k >= 0, k
        return f(n) // f(k) // f(n - k)

    sum = 0
    sum_range = (s - n) // x
    for k in range(sum_range + 1):
        temp = s - x * k - 1
        assert temp >= 0, (temp, s, n, x, sum_range, k)
        sum += (-1)**k * C(n, k) * C(temp, n - 1)

    return sum

assert value_s_n_dice_x(13, 4, 6) == 140
assert value_s_n_dice_x(1, 1, 6) == 1
assert value_s_n_dice_x(6, 1, 6) == 1

for x in range(1, 21):
    for y in [4, 6, 8, 10, 12, 20]:
        total = y ** x
        for z in range(x*y, x - 1, -1):
            lookup[(z, x, y)] = value_s_n_dice_x(z, x, y) / total + lookup.get((z + 1, x, y), 0)

assert (4, 4, 4) in lookup

def get_probability(target, x, y):
    if target > x * y:
        return 0

    if target <= x:
        return 1

    return lookup[(target, x, y)]


def get_chance(h, s):
    match = pattern.match(s)
    if match:
        x, y, op, z = match.group(1, 2, 4, 5)
    else:
        raise Exception("Wrong regex")

    target = h
    if op == '+':
        target -= int(z)
    elif op == '-':
        target += int(z)

    return get_probability(target, int(x), int(y))


def solve(h, spells):
    return max(get_chance(h, s) for s in spells)


def solve_case(f):
    h, s = map(int, next(f).split())
    spells = next(f).strip().split()
    return solve(h, spells)


for i in range(t):
    print("Case #{}: {:.06f}".format(i + 1, solve_case(f)))

