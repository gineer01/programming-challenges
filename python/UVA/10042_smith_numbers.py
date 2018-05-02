def sieve(n):
    s = [True for i in range(n + 1)]
    p = 2
    while p * p < n:
        for i in range(2 * p, n + 1, p):
            s[i] = False

        p += 1
        while not s[p]:
            p += 1

    for i in range(2, n + 1):
        if s[i]:
            yield i


def prime_factor(m, primes):
    for p in primes:
        if m == 1:
            return

        if p*p > m:
            yield m, 1
            return

        if m % p == 0:
            x = 0
            while m % p == 0:
                m //= p
                x += 1

            yield p, x

    if m > 1:
        yield m, 1


import math
LIMIT = math.floor(math.sqrt(10**9))

primes = list(sieve(LIMIT))


def sum_digits(i):
    r = 0
    while i > 0:
        r += i % 10
        i //= 10
    return r


def is_smith(i):
    factors = list(prime_factor(i, primes))
    if len(factors) == 1 and factors[0][1] == 1:
        return False
    sum_i = sum_digits(i)
    sum_factors = sum(sum_digits(a) * b for a, b in factors)
    return sum_i == sum_factors


def solve(n):
    i = n + 1
    while not is_smith(i):
        # print(i)
        i += 1
    return i

assert solve(9984) == 9985

import fileinput
f = fileinput.input()

t = int(next(f))
for i in range(t):
    n = int(next(f))
    print(solve(n))
