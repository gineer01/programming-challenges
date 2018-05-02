import fileinput


def solve(f):
    l = [int(x) for x in next(f).split()]
    c = l[0]
    grades = l[1:]
    average = sum(grades) / c
    above = sum(1 for x in grades if x > average)
    return (100 * above) / c


def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        print("{:.3f}%".format(solve(f)))


main()

