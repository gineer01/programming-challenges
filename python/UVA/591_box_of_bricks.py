import fileinput


def solve(n, heights):
    avg = sum(heights) // n
    moves = sum(h - avg for h in heights if h > avg)
    return moves


def main():
    f = fileinput.input()
    set = 0
    n = int(next(f))
    while n != 0:
        set += 1
        heights = [int(x) for x in next(f).split()]
        print("Set #{}".format(set))
        print("The minimum number of moves is {}.".format(solve(n, heights)))
        print()

        n = int(next(f))


main()
