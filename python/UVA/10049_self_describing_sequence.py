f = [0, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5]
F = [0, 1]

i = 1
temp = 1
while F[i] < 2000000000:
    i += 1
    if len(f) < (i + 1):
        f_next = f[-1] + 1
        f.extend([f_next] * f[f_next])
    temp += f[i]
    F.append(temp)

print(len(F))
import sys

def solve(n):
    import bisect
    return bisect.bisect_left(F, n)


for l in sys.stdin:
    n = int(l)
    if n == 0:
        break

    print(solve(n))

