import fileinput

f = fileinput.input()

count = 0


def format(l):
    def transform(x):
        global count
        if x == '"':
            count = (count + 1) % 2
            return "''" if count == 0 else "``"
        else:
            return x
    return "".join(transform(x) for x in l)

for l in f:
    print(format(l), end='')


