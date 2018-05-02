import fileinput

f = fileinput.input()


def check_jolly(n, a):
    expected = set(range(1, n))
    actual = {abs(a[i] - a[i - 1]) for i in range(1, n)}
    # print(expected, actual)
    return actual == expected

def process_line(l):
    a = list(map(int, l.strip().split()))
    if check_jolly(a[0], a[1:]):
        print("Jolly")
    else:
        print("Not jolly")


for l in f:
    process_line(l)
