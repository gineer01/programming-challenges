import sys


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


primes = list(sieve(2**16))


def exp_fact(n, p, x):
    count = 0

    p_pow = p

    while n // p_pow > 0:
        count += n // p_pow
        p_pow *= p
        if count >= x:
            return True

    return count >= x


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



def is_divide(n, m):
    if n >= m:
        return True

    for p, x in prime_factor(m, primes):
        if not exp_fact(n, p, x):
            return False

    return True

assert is_divide(19277445, 153071487)

for l in sys.stdin:
    n, m = map(int, l.split())
    if is_divide(n, m):
        print("{} divides {}!".format(m, n))
    else:
        print("{} does not divide {}!".format(m, n))
