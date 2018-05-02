import fileinput

f = fileinput.input()

cases = int(next(f))


def process_case(i, a, b):
    print("Case %d: %d"%(i + 1, sum(i for i in range(a, b+1) if i % 2 == 1)))


for i in range(cases):
    a = int(next(f))
    b = int(next(f))
    process_case(i, a, b)

