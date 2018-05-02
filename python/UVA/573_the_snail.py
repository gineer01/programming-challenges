import fileinput
import math


def simulate(h, u, d, F):
    x = u
    day = 1
    while True:
        x -= d
        if x < 0:
            return day

        u -= F
        if u < 0:
            u = 0
        day += 1
        x += u


def solve(h, u, d, fatigue):
    F = u * fatigue / 100
    a = -F / 2
    b = u - d + F/2
    c = d - h

    if a == 0: #not possible, F > 0
        if b > 0:
            x1 = -c/b
            day = math.ceil(x1)
            if day == x1:
                day += 1
            return True, day
        else:
            return False, simulate(h, u, d, F)

    delta = b**2 - 4*a*c
    if delta <= 0:
        return False, simulate(h, u, d, F)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        left = min(x1, x2)
        right = max(x1, x2)
        day = max(math.ceil(left), 1)
        if day == left:
            day += 1
        if left < day < right:
            return True, day
        else:
            return False, simulate(h, u, d, F)

# assert solve(1, 1, 1, 1) == (False, 2)
# assert solve(4, 5, 6, 7) == (True, 1)

def main():
    f = fileinput.input()

    for l in f:
        h, u, d, f = [float(x) for x in l.split()]
        if h > 0:
            success, day = solve(h, u, d, f)
            print("{} on day {}".format("success" if success else "failure", day))
        else:
            return

main()