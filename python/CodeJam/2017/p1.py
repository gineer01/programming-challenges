from functools import lru_cache
import fileinput
import sys

sys.setrecursionlimit(3000)

f = fileinput.input()
t = int(next(f))

def opposite(side):
    if side == '+':
        return '-'
    elif side == '-':
        return '+'
    else:
        raise Exception("What?")


def flip(p):
    return "".join(opposite(c) for c in p)

assert flip("+-+") == "-+-"

@lru_cache(maxsize=None)
def get_flips(pancake, k):
    if len(pancake) < k:
        if all(c == '+' for c in pancake):
            return 0
        else:
            return None

    if len(pancake) == k:
        if pancake == '+' * k:
            return 0
        elif pancake == '-' * k:
            return 1
        else:
            return None

    if pancake[0] == '+':
        return get_flips(pancake[1:], k)
    else:
        r = get_flips(flip(pancake[1:k]) + pancake[k:], k)
        if r is None:
            return r
        else:
            return r + 1

assert get_flips("-+-+-", 4) is None
assert get_flips("+++++", 4) == 0
assert get_flips("++", 4) == 0
assert get_flips("---+-++-", 3) == 3


def get_output(s, k):
    # print(s, k)
    result = get_flips(s, k)
    if result is None:
        return "IMPOSSIBLE"
    else:
        return result


for i in range(t):
    s, k = next(f).split()
    k = int(k)
    print("Case #%s: %s" % (i + 1, get_output(s, k)))