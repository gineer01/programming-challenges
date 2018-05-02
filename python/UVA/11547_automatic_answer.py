import fileinput



def solve(n):
    r = n * 63
    r += 7492
    r *= 5
    r -= 498
    return str(r)[-2]


assert solve(637) == "1"


def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        n = int(next(f))
        print(solve(n))

main()
