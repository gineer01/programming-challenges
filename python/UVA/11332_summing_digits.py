import fileinput


def solve(n):
    while n > 9:
        n = sum(int(x) for x in str(n))

    return n


def main():
    f = fileinput.input()
    for l in f:
        n = int(l)
        if n > 0:
            print(solve(n))


main()
