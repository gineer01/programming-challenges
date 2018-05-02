import fileinput



def solve(l, s):
    duration, down, loan_amount, n = l
    value = down + loan_amount
    payment = loan_amount / duration
    i = 0
    s_i = 0

    def get_loan():
        return loan_amount - (i * payment)

    def get_val():
        nonlocal s_i
        if len(s) > (s_i + 1) and s[s_i + 1][0] == i:
            s_i += 1
        depre = s[s_i][1]
        return value * (1 - depre)

    value = get_val()
    loan = get_loan()
    while value < loan:
        i += 1
        value = get_val()
        loan = get_loan()
    return i




def get_schedule(n, f):
    s = []
    for i in range(n):
        l = next(f).split()
        i = int(l[0])
        d = float(l[1])
        s.append((i, d))
    return s


def main():
    f = fileinput.input()
    loan = get_loan(f)
    while loan:
        s = get_schedule(loan[3], f)
        i = solve(loan, s)
        if i == 1:
            print("1 month")
        else:
            print("{} months".format(i))
        loan = get_loan(f)


def get_loan(f):
    l = next(f).split()
    duration = int(l[0])
    if duration < 0:
        return False
    return duration, float(l[1]), float(l[2]), int(l[3])


main()