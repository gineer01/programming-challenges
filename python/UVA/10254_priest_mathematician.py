f = [0, 1]

partial_sum = []

i = 0
while len(partial_sum) < 10000:
    partial_sum.extend( [2**i] * (i + 1))
    i += 1


def solve(n):
    return f[n - 1] + partial_sum[n - 1]

for i in range(2, 10001):
    f.append(solve(i))

# print(partial_sum)
# print(f)
import sys

for l in sys.stdin:
    n = int(l)
    print(f[n])
