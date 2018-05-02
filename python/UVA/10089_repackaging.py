import sys


def is_zero(a):
    return all(i == 0 for i in a)

def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]


def neg(a):
    return [-i for i in a]

def scale(a, n):
    return [n * i for i in a]


def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


I = [1, 1, 1]


def solve(n, vectors, target=I):
    t_2 = dot(target, target)

    if t_2 == 0:
        if all(is_zero(v) for v in vectors):
            return [1] * (n + 1)
        else:
            return None

    if n == 2:
        a, b = vectors
        a_x_b = cross(a, b)

        if is_zero(a_x_b):
            if not is_zero(cross(a, target)):
                return None

        if dot(a_x_b, target) == 0:
            a_2 = dot(a, a)
            b_2 = dot(b, b)
            a_b = dot(a, b)
            a_t = dot(a, target)
            b_t = dot(b, target)
            x = a_t * b_2 - a_b * b_t
            y = a_2 * b_t - a_b * a_t
            z = a_2 * b_2 - a_b * a_b

            if z == 0:
                if x == y == 0:
                    if a_t > 0:
                        k1, k2 = get_scale_solution(t_2, a_t)
                        return k1, 0, k2
                    elif b_t > 0:
                        k1, k2 = get_scale_solution(t_2, b_t)
                        return 0, k1, k2
                    else:
                        return None
                else:
                    return None
            if x >= 0 and y >= 0 and z >= 0:
                return x, y, z
            else:
                return None
        else:
            return None

    vectors_t = [cross(v, target) for v in vectors]
    for i in range(n):
        remaining = vectors_t[:i] + vectors_t[i+1:]
        r = solve(n - 1, remaining, target=neg(vectors_t[i]))
        if r:
            total = r[-1] * dot(vectors[i], target)
            total += sum(r[j] * dot(vectors[j], target) for j in range(0, i))
            total += sum(r[j - 1] * dot(vectors[j], target) for j in range(i + 1, n))
            if total <= 0:
                continue

            k1, k2 = get_scale_solution(t_2, total)
            r = scale(r, k1)
            r.insert(i, r[-1])
            r[-1] = k2
            return tuple(r)

    return None


def get_scale_solution(target_2, total):
    g = egcd(total, target_2)[0]
    k1 = target_2 // g
    return k1, (total // g)


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

