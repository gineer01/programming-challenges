file = open("A-large.in")
no_test = int(file.readline())


def get_last_number(n):
    current = n
    digits = set()

    while True:
        new_digits = set(str(current))
        digits |= new_digits
        # print(digits, new_digits)
        if len(digits) == 10:
            return current
        current += n

def get_output(n):
    n = int(n)

    if n == 0:
        return 'INSOMNIA'

    return get_last_number(n)


for i in range(0, no_test):
    print("Case #%s: %s" % (i + 1, get_output(file.readline())))
