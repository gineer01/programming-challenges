import fileinput
import functools
import math

f = fileinput.input()

t = int(next(f))


def solve(n, m, k):

    @functools.lru_cache(maxsize=None)
    def re_solve(n, m, up, left):
        if n <= k:
            return math.inf
        if m <= k:
            return math.inf

        if up <= -1 and left <= -1:
            return 1

        min_w = 2 * k
        if n <= min_w and m >= (min_w + 3):
            return 2
        if m <= min_w and n >= (min_w + 3):
            return 2

        return min(re_solve(n - k, m, k + 1, left - k), re_solve(n, m - k, up - k, k + 1)) + 1

    re_solve.cache_clear()
    r = re_solve(n, m, m, n)
    if r == math.inf:
        return -1
    else:
        return r

assert solve(6, 6, 1) == 5

for i in range(t):
    n, m, k = map(int, next(f).split())
    print("Case #{}: {}".format(i + 1, solve(n, m, k)))

