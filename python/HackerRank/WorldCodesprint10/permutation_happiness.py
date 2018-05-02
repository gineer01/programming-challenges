#!/bin/python3


MODULUS = 1000000007

peaks = [[0]*1501 for j in range(3001)]

for n in range(1, 3001):
    for k in range(1, (n + 1)//2 + 1):
        if n == 1:
            if k == 1:
                peaks[n][k] = 1
                continue
            else:
                peaks[n][k] = 0
                continue

        if k > (n + 1)//2:
            peaks[n][k] = 0
            continue

        same_peaks = 2 * k * peaks[n - 1][k]
        add_peak = peaks[n - 1][k - 1] * (n - 2 * k + 2)
        peaks[n][k] = (same_peaks + add_peak) % MODULUS


def peak(n, k):
    if n == 1:
        if k == 1:
            return 1
        else:
            return 0

    if k > (n + 1)//2:
        return 0
    if k <= 0:
        return 0

    return peaks[n][k]


def query(n, k):
    result = 0
    for i in range(1, n - k + 1):
        result += peak(n, i)
    return result % MODULUS


# print(query(3000, 1500))
# assert query(500, 250) == 2**500
# print(peaks[2])
assert peak(2, 1) == 2
assert peak(2, 0) == 0
assert peak(2, 2) == 0

assert peak(3, 2) == 2
assert peak(3, 0) == 0
assert peak(3, 3) == 0
assert peak(3, 1) == 4

# assert peak(4, 2) == 16
# for i in range(5):
#     print(i, query(4, i))
#     print('peak', i, peak(4, i))
assert query(4, 3) == 8
assert query(4, 2) == 24
assert query(3, 2) == 4
assert query(10, 7) == 1433856

q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    # Find the number of ways to arrange 'n' people such that at least 'k' of them will be happy
    # The return value must be modulo 10^9 + 7
    print(query(n, k))
