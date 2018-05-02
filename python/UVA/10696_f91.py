import fileinput


def solve(n):
    if n > 100:
        return n - 10
    else:
        return 91


def main():
    f = fileinput.input()
    for l in f:
        n = int(l)
        if n > 0:
            print("f91({}) = {}".format(n, solve(n)))


main()

for i in range(1, 200):
    print(i, solve(i))
