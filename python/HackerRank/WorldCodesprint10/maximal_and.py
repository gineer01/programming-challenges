#!/bin/python3

import sys

MODULUS = 1000000007
def choose(n, k):
    k = min(n - k, k)
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)

    return r % MODULUS


def and_sequence(s):
    import functools
    import operator
    return functools.reduce(operator.and_, s)


def solve(n, k, a):
    def solve_max():
        nonlocal a
        for i in range(61):
            mask = 2 ** (60 - i)
            temp = [mask & el for el in a]
            non_zero = [a[i] for i in range(len(a)) if temp[i] > 0]
            if len(non_zero) >= k:
                a = non_zero

        return and_sequence(a), len(a)

    max_a, count = solve_max()
    return max_a, choose(count, k)


assert solve(4, 2, [12, 3, 1, 1]) == (1, 3)
assert solve(3, 2, [3, 5, 6]) == (4, 1)
assert solve(4, 2, [21, 19, 22, 20]) == (20, 3)
# assert solve(100000, 100000, [21, 19, 22, 20]) == (20, 3)

n, k = map(int, input().split())
a = []
i = 0
for i in range(n):
    a.append(int(input()))
result = solve(n, k, a)
print (*result, sep="\n")
