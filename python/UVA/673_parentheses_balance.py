import fileinput


def solve(l):
    s = []
    for c in l:
        if c == '(' or c == '[':
            s.append(c)
        else:
            if c == ']':
                if len(s) > 0 and s[-1] == '[':
                    s.pop()
                else:
                    return False
            elif c == ')':
                if len(s) > 0 and s[-1] == '(':
                    s.pop()
                else:
                    return False
            else:
                return False

    return len(s) == 0


def main():
    f = fileinput.input()
    n = int(next(f))
    for i in range(n):
        l = next(f).strip()
        if solve(l):
            print("Yes")
        else:
            print("No")


main()
