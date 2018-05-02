import fileinput
import itertools

f = fileinput.input()


def solve(a, b):
    count = 0
    carry = 0
    for x, y in itertools.zip_longest(reversed(a), reversed(b), fillvalue="0"):
        if int(x) + int(y) + carry > 9:
            count += 1
            carry = 1
        else:
            carry = 0

    return count


for l in f:
    a, b = l.strip().split()
    if a == '0' and b == '0':
        break

    r = solve(a, b)
    if r == 0:
        print("No carry operation.")
    elif r == 1:
        print("1 carry operation.")
    else:
        print("{} carry operations.".format(r))

