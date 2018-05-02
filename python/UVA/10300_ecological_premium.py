import fileinput

f = fileinput.input()

cases = int(next(f))


def process_case(f):
    no_farmers = int(next(f))
    return sum(cal_farmer(f) for j in range(no_farmers))


def cal_farmer(f):
    line = next(f)
    size, no_animals, env_co = [int(x) for x in line.split()]
    return size * env_co


for i in range(cases):
    print(process_case(f))
