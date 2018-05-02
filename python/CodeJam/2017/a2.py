import fileinput
import functools


def get_kit(candidates):
    import operator
    return functools.reduce(operator.and_, candidates)


def remove_one(packages):
    n = len(packages)
    for p in range(n):
        s = packages[p][0]
        if not s:
            min_p = p
            return tuple(packages[i] if i != min_p else packages[i][1:] for i in range(n))

    min_p = 0
    for p in range(n):
        s = packages[p][0]
        if min(s) < min(packages[min_p][0]):
            min_p = p
    return tuple(packages[i] if i != min_p else packages[i][1:] for i in range(n))


@functools.lru_cache(maxsize=None)
def solve(packages):
    # print(packages)
    if not all(packages):
        return 0
    candidates = [p[0] for p in packages]
    while not get_kit(candidates):
        packages = remove_one(packages)
        if not all(packages):
            return 0
        candidates = [p[0] for p in packages]
    return 1 + solve(tuple(p[1:] for p in packages))



assert solve(((frozenset({3}),), (frozenset(),))) == 0

f = fileinput.input()
t = int(next(f))


def get_serving_range(package, recipe):
    from math import ceil, floor
    lower = (package / recipe) / 1.1
    upper = (package / recipe) / .9
    return ceil(lower), floor(upper) + 1

def get_packages(line, ingredient):
    vals = sorted((get_serving_range(int(s), ingredient) for s in line.split()))
    # print(line, vals)
    return tuple(frozenset(range(*x)) for x in vals if (x[0] < x[1]))

for i in range(t):
    n, p = [int(s) for s in next(f).split()]
    r = [int(s) for s in next(f).split()]
    q = tuple(get_packages(next(f), r[i]) for i in range(n))
    # print(i, r, c, grid)
    print("Case #%s:" % (i + 1), solve(q))

