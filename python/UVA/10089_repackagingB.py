import sys


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]


I = [1, 1, 1]


def solve(n, vectors, target=I):
    def can_zero_x(n, v, x_axis):
        for i in range(n):
            if dot(x_axis, v[i]) < 0:
                return True
        return False

    def can_zero_y(n, v, x_axis):
        y_axis = cross(x_axis, I)

        has_pos = False
        has_neg = False
        for i in range(n):
            p = dot(v[i], y_axis)
            if p > 0:
                has_pos = True
            elif p < 0:
                has_neg = True
            elif p == 0:
                if dot(x_axis, v[i]) < 0:
                    return True

            if has_pos and has_neg:
                return True
        return not (has_pos ^ has_neg)

    V_x_I = [cross(v, target) for v in vectors]

    for x_axis in V_x_I:
        if not can_zero_x(n, V_x_I, x_axis):
            return False
        if not can_zero_y(n, V_x_I, x_axis):
            return False

    return True

for l in sys.stdin:
    n = int(l)
    if n == 0:
        break

    packages = [list(map(int, next(sys.stdin).split())) for i in range(n)]

    if solve(n, packages):
        print("Yes")
    else:
        print("No")

