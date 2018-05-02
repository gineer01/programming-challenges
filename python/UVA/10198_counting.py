import sys

r = [0, 2, 5, 13]

for i in range(4, 1001):
    s = 2 * r[i - 1] + r[i - 2] + r[i - 3]
    r.append(s)

for l in sys.stdin:
    print(r[int(l)])

