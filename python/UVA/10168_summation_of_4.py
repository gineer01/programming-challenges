import math
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

LIMIT = math.floor(math.sqrt(10000001))
primes = list(sieve(LIMIT))

l_primes = len(primes)
# print(primes)

import sys


def solve(n):
    if n % 2 == 0:
        r1 = (2, 2)
        c = n - 4
    else:
        r1 = (2, 3)
        c = n - 5

    if c < 4:
        return None
    r = solve_pair(primes, c)
    if r:
        return r1 + r

    return None


def is_prime(b):
    for p in primes:
        if p ** 2 > b:
            return True

        if b % p == 0:
            return False

    return True


def solve_pair(pairs, n):
    for p in primes:
        b = n - p
        if is_prime(b):
            return (p, b)

    return None


for l in sys.stdin:
    r = solve(int(l))
    if r:
        print(*r)
    else:
        print("Impossible.")

