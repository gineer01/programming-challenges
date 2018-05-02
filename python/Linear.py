def is_zero(a):
    return all(i == 0 for i in a)


def dot(a, b):
    assert len(a) == len(b)
    return sum(a[i] * b[i] for i in range(len(a)))


def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]


def neg(a):
    return [-i for i in a]


def scale(a, n):
    return [n * i for i in a]

