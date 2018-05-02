import fileinput


def solve(l, train):
    swap = 0
    for i in range(l):
        carriage = l - i
        position = train.index(carriage)
        expected = carriage - 1
        swap += expected - position
        train.remove(carriage)

    return swap


def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        l = int(next(f))
        train = [int(x) for x in next(f).split()]
        print("Optimal train swapping takes %d swaps." % (solve(l, train)))

main()
