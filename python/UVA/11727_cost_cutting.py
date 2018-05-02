import fileinput

f = fileinput.input()

cases = int(next(f))


def process_case(i, f):
    l = next(f)
    salaries = [int(x) for x in l.split()]
    salaries.sort()
    print("Case {}: {}".format(i+ 1, salaries[1]))


for i in range(cases):
    process_case(i, f)

