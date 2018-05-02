import fileinput

f = fileinput.input()

cases = int(next(f))


def process_case(a, b):
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')


for i in range(cases):
    l = next(f)
    a, b = list(map(int, l.strip().split()))
    process_case(a, b)


