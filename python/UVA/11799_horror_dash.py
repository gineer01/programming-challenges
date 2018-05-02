import fileinput



def solve(f):
    l = [int(x) for x in next(f).split()]
    return max(l[1:])



def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        print("Case %s: %s" % (i + 1, solve(f)))


main()
