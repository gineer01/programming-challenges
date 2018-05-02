import fileinput


def solve(x, y):
    if x == 0 or y == 0:
        return "divisa"
    elif x > 0:
        if y > 0:
            return "NE"
        else:
            return "SE"
    else:
        if y > 0:
            return "NO"
        else:
            return "SO"


def main():
    f = fileinput.input()
    k = int(next(f))
    while k > 0:
        n, m = [int(x) for x in next(f).split()]
        for i in range(k):
            x, y = [int(x) for x in next(f).split()]
            print(solve(x - n, y - m))

        k = int(next(f))

main()
