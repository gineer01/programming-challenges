import fileinput

f = fileinput.input()


def flip(cakes, n, i):
    end_index = n - i + 1
    flipped = cakes[:end_index]
    flipped.reverse()
    cakes[:end_index] = flipped


def solve(n, sorted_cakes, cakes):
    result = []
    for i in range(1, n + 1):
        if i == n:
            result.append(0)

        if sorted_cakes[-i] == cakes[-i]:
            continue
        else:
            to_bottom = sorted_cakes[-i]
            pos = cakes.index(to_bottom)
            if pos == 0:
                flip(cakes, n, i)
                result.append(i)
            else:
                flip(cakes, n, n - pos)
                result.append(n - pos)
                flip(cakes, n, i)
                result.append(i)

    assert cakes == sorted_cakes, cakes
    return result



for l in f:
    cakes = list(map(int, l.strip().split()))
    print(*cakes)

    n = len(cakes)
    result = solve(n, list(sorted(cakes)), cakes)

    print(*result)

