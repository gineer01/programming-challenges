import fileinput
import itertools


def solve_three(s):
    a0 = s[0] + s[1] - s[2]
    a1 = s[0] - s[1] + s[2]
    a2 = -s[0] + s[1] + s[2]

    a = [a0, a1, a2]
    if all(i % 2 == 0 for i in a):
        return [i//2 for i in a]
    else:
        return None


def add_verify(r, sums):
    n = len(sums)
    assert n == len(r), (r, sums)
    sums.sort()
    r.sort()
    result = [sums[i] - r[i] for i in range(n)]
    c = result[0]
    if all(result[i] == c for i in range(n)):
        r.append(c)
        return r
    else:
        return None


def solve_eight(r, sums):
    l = len(sums)
    positions = set(range(l))
    for c in itertools.combinations(positions, 6):
        d = set(c)

        sub_problem = [sums[i] for i in d]
        other_sums = [sums[i] for i in (positions - d)]
        temp = r[:]
        temp = add_verify(temp, sub_problem)
        if temp:
            temp = add_verify(temp, other_sums)
            if temp:
                yield temp


def solve_nine(r, sums):
    l = len(sums)
    positions = set(range(l))
    for c in itertools.combinations(positions, 3):
        d = set(c)

        sub_problem = [sums[i] for i in d]

        r2 = solve_three(sub_problem)
        if r2:
            other_sums = [sums[i] for i in (positions - d)]
            try:
                for x in r:
                    for y in r2:
                        other_sums.remove(x + y)
            except ValueError:
                continue

            if len(other_sums) == 0:
                yield r + r2


def solve(n, sums):
    sums.sort()

    if n == 3:
        r = solve_three(sums)
        if r:
            yield r
    elif n < 6:
        l = len(sums)
        positions = set(range(2, l - 2))
        k = (n - 1)*(n - 2)//2
        for c in itertools.combinations(positions, k - 2):
            d = set(c) | {0, 1}

            sub_problem = [sums[i] for i in d]
            other_sums = [sums[i] for i in ((positions - d) | {l - 2, l - 1})]
            for r in solve(n - 1, sub_problem):
                r = add_verify(r, other_sums)
                if r:
                    yield r
    else:
        for i in sorted(set(sums[2:-2])):
            sums_copy = sums[2:-2]
            sums_copy.remove(i)
            for j in sorted(set(sums_copy), reverse=True):
                r1 = solve_three(sums[:2] + [i])
                if not r1:
                    continue
                r2 = solve_three([j] + sums[-2:])
                if not r2:
                    continue

                sums_copy = sums[2:-2]
                sums_copy.remove(i)
                sums_copy.remove(j)

                try:
                    for x in r1:
                        for y in r2:
                            sums_copy.remove(x + y)
                except ValueError:
                    continue

                r = r1 + r2
                if len(sums_copy) == 0:
                    yield r
                elif n == 7:
                    r = add_verify(r, sums_copy)
                    if r:
                        yield r
                elif n == 8:
                    yield from solve_eight(r, sums_copy)
                elif n == 9:
                    yield from solve_nine(r, sums_copy)




    return None

# a = [39953, 39971, 39979, 39983]
# for i in range(4):
#     for j in range(i + 1, 4):
#         print(a[i] + a[j])
# print()
b = []
# a = [39960, 39964, 39972, 39990, 100, 1000, 2000, 5000, 10000]
a = [1] * 9
for i in range(9):
    for j in range(i + 1, 9):
        b.append(a[i] + a[j])

# print(*b)

f = fileinput.input()
for l in f:
    line = list(map(int, l.split()))
    n = line[0]
    sums = line[1:]
    try:
        r = next(solve(n, sums))
        if r:
            r = sorted(r)
            print(*r)
    except StopIteration as e:
        print("Impossible")

