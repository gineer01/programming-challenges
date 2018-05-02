import fileinput


def main():
    f = fileinput.input()
    for l in f:
        n, b, h, w = [int(x) for x in l.split()]
        choice = []
        for i in range(h):
            cost = int(next(f))
            beds = [int(x) for x in next(f).split()]
            if any(True for b in beds if b >= n):
                choice.append(cost * n)

        if choice and min(choice) <= b:
            print(min(choice))
        else:
            print("stay home")


main()