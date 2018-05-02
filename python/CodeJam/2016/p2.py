from functools import lru_cache


file = open("B-large.in")
no_test = int(file.readline())


def opposite(side):
    if side == '+':
        return '-'
    elif side == '-':
        return '+'
    else:
        raise Exception("WTF")

@lru_cache(maxsize=None)
def get_flips(pancake, side):
    if len(pancake) == 0:
        return 0

    if pancake[-1] == side:
        return get_flips(pancake[:-1], side)
    else:
        return get_flips(pancake[:-1], opposite(side)) + 1

def get_output(s):
    return get_flips(s, '+')


for i in range(0, no_test):
    line = file.readline().strip()
    print("Case #%s: %s" % (i + 1, get_output(line)))