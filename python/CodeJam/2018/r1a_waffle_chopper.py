import fileinput


def count_row(row):
    return sum(1 for c in row if c == '@')


def count_chocolate(waffle):
    return sum(count_row(r) for r in waffle)


def transpose(waffle):
    return list(map(list, zip(*waffle)))


def is_divisible(waffle, target):
    row_counts = [count_row(r) for r in waffle]
    total = sum(row_counts)
    if total % target != 0:
        return False

    import itertools
    cum_sum = list(itertools.accumulate(row_counts))

    c = target
    cuts = [0]
    length = len(cum_sum)
    for i in range(length):
        if cum_sum[i] == c:
            cuts.append(i + 1)
            c += target

        if cum_sum[i] > c:
            return False

    return cuts


def solve(r, c, h, v, waffle):
    count = count_chocolate(waffle)
    if count == 0:
        return True
    # print(r, c, h, v, waffle, count)

    if count % (h + 1) * (v + 1) != 0:
        return False

    count_per_row = count // (h + 1)
    row_cuts = is_divisible(waffle, count_per_row)
    if not row_cuts:
        return False

    columns = transpose(waffle)
    count_per_col = count // (v + 1)
    col_cuts = is_divisible(columns, count_per_col)
    if not col_cuts:
        return False

    return check_all_slices(count, row_cuts, col_cuts, h, v, waffle)


def count_chocolate_slice(waffle, row0, row1, col0, col1):
    count = 0
    for i in range(row0, row1):
        for j in range(col0, col1):
            if waffle[i][j] == '@':
                count += 1
    return count


def check_all_slices(count, row_cuts, col_cuts, h, v, waffle):
    count_per_slice = count // ((h + 1) * (v + 1))
    for i in range(h + 1):
        for j in range(v + 1):
            if count_chocolate_slice(waffle, row_cuts[i], row_cuts[i + 1], col_cuts[j], col_cuts[j+1]) != count_per_slice:
                return False

    return True


assert solve(3, 4, 2, 2, [['@', '.', '@', '@'], ['@', '@', '.', '@'], ['@', '.', '@', '@']])
assert solve(3, 6, 1, 1, [['.', '@', '@', '.', '.', '@'], ['.', '.', '.', '.', '.', '@'], ['@', '.', '@', '.', '@', '@']])
assert not solve(4, 4, 1, 1, [['.', '.', '@', '@'], ['.', '.', '@', '@'], ['@', '@', '.', '.'], ['@', '@', '.', '.']])
assert is_divisible([['.', '@', '@', '.', '.', '@'], ['.', '.', '.', '.', '.', '@'], ['@', '.', '@', '.', '@', '@']], 4)


def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        r, c, h, v = [int(x) for x in next(f).split()]
        waffle = [list(next(f).strip()) for i in range(r)]
        answer = "POSSIBLE" if solve(r, c, h, v, waffle) else "IMPOSSIBLE"
        print("Case #%s: %s" % (i + 1, answer))

main()
