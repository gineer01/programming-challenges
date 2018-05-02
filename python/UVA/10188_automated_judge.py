import fileinput

f = fileinput.input()

count = 0

def numeric_version(lines):
    r = "".join(["".join(c for c in l if c.isdigit()) for l in lines])
    return r


def check(solution, submission):
    if solution == submission:
        return "Accepted"
    elif numeric_version(solution) == numeric_version(submission):
        return "Presentation Error"
    else:
        return "Wrong Answer"


for l in f:
    n = int(l)
    if (n == 0):
        break
    solution = [next(f) for i in range(n)]
    m = int(next(f))
    submission = [next(f) for i in range(m)]

    count += 1
    print("Run #{}: {}".format(count, check(solution, submission)))
