import sys


def dot(a, b):
    assert len(a) == len(b)
    return sum(a[i] * b[i] for i in range(len(a)))


def cross(a):
    return -a[1], a[0]


def found_possible(q, p):
    any_up = q[1] or p[0]
    any_down = q[2] or p[1]
    return any_up and any_down


def found_impossible(q, p):
    any_up = q[0] or q[1] or p[0]
    any_down = q[2] or q[3] or p[1]
    if any_down ^ any_up:
        return True

    any_left = q[1] or q[2]
    if not any_left:
        return True


def solve(n, vectors):
    V_I = [(v[1] - v[0], v[2] - v[0]) for v in vectors]

    x_axis = V_I[0]

    while x_axis:
        y_axis = cross(x_axis)

        q = [False] * 4
        p = [False] * 2
        temp = [None] * 2

        for v in V_I:
            v_x = dot(v, x_axis)
            v_y = dot(v, y_axis)

            if v_x == 0:
                if v_y < 0:
                    p[1] = True
                elif v_y > 0:
                    p[0] = True
                else:
                    pass # ignore: 0 vector
            elif v_x > 0:
                if v_y > 0:
                    q[0] = True
                    temp[0] = v
                elif v_y < 0:
                    q[3] = True
                else:
                    pass # ignore: same direction as x_axis
            else:
                if v_y > 0:
                    q[1] = True
                    temp[1] = v
                elif v_y < 0:
                    q[2] = True
                else:
                    return True # found the opposite vector to x_axis

            if found_possible(q, p):
                return True

        if found_impossible(q, p):
            return False

        assert temp[1] or temp[0]
        if temp[1]:
            x_axis = temp[1]
        else:
            x_axis = temp[0]

    return True

assert solve(4, [[1, 2, 3], [1, 11, 5], [9, 4, 3], [2, 3, 2]])
# print(solve(4, [[1, 2, 3], [1, 11, 5], [9, 4, 3], [2, 3, 2]]))

assert solve(3, [[5, 3, 1], [1, 2, 2], [2, 1, 1]])
# print(solve(3, [[5, 3, 1], [1, 2, 2], [2, 1, 1]]))

assert not solve(4, [[1, 3, 3], [1, 11, 5], [9, 4, 3], [2, 3, 2]])
# print( solve(4, [[1, 3, 3], [1, 11, 5], [9, 4, 3], [2, 3, 2]]))

assert solve(2, [[1, 2, 2], [2, 1, 1]])
# print(solve(2, [[1, 2, 2], [2, 1, 1]]))


for l in sys.stdin:
    n = int(l)
    if n == 0:
        break

    packages = [list(map(int, next(sys.stdin).split())) for i in range(n)]

    if solve(n, packages):
        print("Yes")
    else:
        print("No")

