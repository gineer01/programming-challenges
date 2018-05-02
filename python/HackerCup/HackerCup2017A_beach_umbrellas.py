import fileinput
import itertools
import functools
import math

f = fileinput.input()

t = int(next(f))

MODULUS = 1000000007


@functools.lru_cache(maxsize=2**11)
def fact(n):
    if n <= 10:
        return math.factorial(n) % MODULUS
    r = 1
    for i in range(n):
        r *= i + 1
        r %= MODULUS
    return r

assert fact(100) == 437918130


@functools.lru_cache(maxsize=2**11)
def choose(n, k):
    k = min(n - k, k)
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)

    return r % MODULUS

assert choose(6, 3) == math.factorial(6)//math.factorial(3)//math.factorial(3) % MODULUS
assert choose(100, 45) == math.factorial(100)//math.factorial(45)//math.factorial(55) % MODULUS


def cal_val(n, m, M):
    base_case = 2 * fact(n - 2)
    return base_case * choose(n + M - m, M - m)


def solve(n, M, radiuses):
    # print(n, m, radiuses)
    if n == 1:
        return M

    total = 1 + 2 * sum(radiuses)
    count = 0
    for pair in itertools.combinations(radiuses, 2):
        m = total - sum(pair)
        if m > M:
            continue

        count += cal_val(n, m, M)
        count %= MODULUS
    return count


for i in range(t):
    n, m = map(int, next(f).split())
    radiuses = [int(next(f)) for i in range(n)]
    print("Case #{}: {}".format(i + 1, solve(n, m, radiuses)))

