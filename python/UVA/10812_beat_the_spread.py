import fileinput



def solve(s, d):
    if (s + d) % 2 != 0:
        return False

    a = (s + d) // 2
    b = s - a
    if a >= 0 and b >= 0:
        r = reversed(sorted((a, b)))
        # print(*r)
        return r
    else:
        return False


assert tuple(solve(40, 20)) == (30,10)
assert solve(20, 40) == False
assert solve(21, 40) == False


def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        s, d = [int(x) for x in next(f).split()]
        result = solve(s, d)
        if result:
            print(*result)
        else:
            print("impossible")


main()