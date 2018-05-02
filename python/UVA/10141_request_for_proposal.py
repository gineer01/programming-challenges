import fileinput


def solve(proposals):
    proposals.sort()
    return proposals[0][3]


def main():
    f = fileinput.input()
    count = 1

    n, p = [int(x) for x in next(f).split()]
    while n > 0 :
        requirements = [next(f).strip() for i in range(n)]
        proposals = []
        for i in range(p):
            name = next(f).strip()
            d, r = next(f).split()
            d = float(d)
            r = int(r)
            met = [next(f).strip() for i in range(r)]

            proposals.append((-r, d, i, name))

        if count > 1:
            print()
        print("RFP #%s" % (count))
        print(solve(proposals))

        n, p = [int(x) for x in next(f).split()]
        count += 1

main()
