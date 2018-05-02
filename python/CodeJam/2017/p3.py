import fileinput


def get_output(n, k):
    level = get_level(k)
    leaves = k - level

    slots = level + 1
    remaining = n - level
    small_slot_size = (remaining) // slots

    big_slot = remaining - (slots * small_slot_size)
    # small_slot = slots - big_slot

    if leaves == 0:
        raise Exception("Not possible")

    if leaves > big_slot:
        unoccupied = small_slot_size - 1
    else:
        unoccupied = small_slot_size

    m = unoccupied // 2
    return unoccupied - m, m


def get_level(k):
    c = 0
    while 2 ** (c + 1) - 1 < k:
        c += 1
    return 2 ** c - 1

assert get_output(7, 7) == (0, 0)
assert get_output(14, 7) == (1, 0)
assert get_output(15, 7) == (1, 1)
assert get_output(16, 7) == (1, 1)
assert get_output(1000, 1) == (500, 499)
assert get_output(999, 1) == (499, 499)
assert get_output(1, 1) == (0, 0)
assert get_output(4, 2) == (1, 0)
assert get_output(5, 2) == (1, 0)
assert get_output(6, 2) == (1, 1)
assert get_output(1000, 1000) == (0, 0)
assert get_output(999, 2) == (249, 249)

f = fileinput.input()
t = int(next(f))
for i in range(t):
    n, k = [int(s) for s in next(f).split()]
    print("Case #%s:" % (i + 1), *get_output(n, k))




