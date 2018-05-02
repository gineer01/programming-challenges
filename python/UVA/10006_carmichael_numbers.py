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


p = set(sieve(65000))
# print(p)

def is_carmichael(n):
    if n in p:
        return False

    for i in range(n):
        if pow(i, n, n) != i:
            return False

    return True


for l in sys.stdin:
    n = int(l)
    if n == 0:
        break
    else:
        if is_carmichael(n):
            print("The number {} is a Carmichael number.".format(n))
        else:
            print("{} is normal.".format(n))
