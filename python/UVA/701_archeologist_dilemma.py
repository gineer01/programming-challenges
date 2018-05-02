import fileinput
import functools
import math

f = fileinput.input()

@functools.lru_cache(maxsize=None)
def prefix(i):
    return str(2**i)[:11]


def solve(l):
    n = len(l) + 1
    lg_l = math.log2(int(l))
    lg_l1 = math.log2(int(l) + 1)
    lg_10 = math.log2(10)

    i = lg_l + n * lg_10
    j = lg_l1 + n * lg_10
    while True:
        x = math.ceil(i)
        if i < x < j:
            for k in range(math.ceil(i), math.floor(j) + 1):
                # print(k, prefix(k))
                if prefix(k).startswith(l):
                    return k

        n += 1
        i = lg_l + n * lg_10
        j = lg_l1 + n * lg_10
        # print(i, j)
    return i

for l in f:
    r = solve(l.strip())
    if r:
        print(r)
    else:
        print("no power of 2")

