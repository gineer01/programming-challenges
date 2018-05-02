import fileinput
import math

f = fileinput.input()

t = int(next(f))

def in_sector(p, x, y):
    sector = p * 2* math.pi / 100
    theta = math.pi/2 - math.atan2(y, x)
    if theta < 0:
        theta += 2 * math.pi 
    return theta <= sector

assert in_sector(25, 1, 1)
assert in_sector(25, 1, 0)
assert in_sector(50, 0, -1)
assert in_sector(75, -1, -1)
assert in_sector(75, -1, 0)
assert in_sector(99, -1, 2)


def solve(p, x, y):
    x -= 50
    y -= 50
    radius2 = 50 ** 2
    r = x**2 + y**2
    if p > 0 and r <= radius2 and in_sector(p, x, y):
        return "black"
    return "white"


for i in range(t):
    line = map(int, next(f).strip().split())
    print("Case #{}: {}".format(i + 1, solve(*line)))

