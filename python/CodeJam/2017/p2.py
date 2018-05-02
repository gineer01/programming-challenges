import fileinput
from functools import lru_cache

f = fileinput.input()
t = int(next(f))


@lru_cache()
def get_output(n):
    l = len(n)
    first_digit = n[0]
    if int(first_digit * l) < int(n):
        return first_digit + get_output(n[1:])
    elif int(first_digit * l) == int(n):
        return n
    else:
        return next_largest(first_digit, l)


def next_largest(first_digit, l):
    c = int(first_digit) - 1
    if c > 0:
        return str(c) + '9' * (l - 1)
    else:
        return '9' * (l - 1)


assert get_output('1000') == '999'
assert get_output('7') == '7'
assert get_output('112233445566778899') == '112233445566778899'


for i in range(t):
    n = next(f).strip()
    print("Case #%s: %s" % (i + 1, get_output(n)))

