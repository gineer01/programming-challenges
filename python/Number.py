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



# From https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0
