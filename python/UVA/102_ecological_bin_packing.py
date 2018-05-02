import fileinput
import itertools

f = fileinput.input()

letter_mapping = {
    'B' : 0,
    'G' : 1,
    'C' : 2
}


def process_case(n, bin):
    total = sum(n)

    # if the type matches the bin type, it stays in the bin.
    # the number of movement = total - number_of_stays
    def number_of_stays(case):
        return sum(bin[bin_no][letter_mapping[type]] for bin_no, type in enumerate(case))

    movement = total
    case = "BCG"
    for c in itertools.permutations("BCG"):
        m = total - number_of_stays(c)
        if m < movement:
            movement = m
            case = c

    print("".join(case), movement)


for l in f:
    n = [int(x) for x in l.split()]
    bin = [[n[3*j + i] for i in range(3)] for j in range(3)]
    process_case(n, bin)

