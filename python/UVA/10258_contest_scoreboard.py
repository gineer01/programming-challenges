import fileinput

f = fileinput.input()

t = int(next(f))
next(f)


def get_ranking(submissions):
    submitted = set()
    incorrect = {}
    penalty = {}

    for l in submissions:
        team = int(l[0])
        problem = l[1]
        c_p = (team, problem)
        status = l[3]

        submitted.add(team)

        if status == 'C':
            if c_p not in penalty:
                penalty[c_p] = int(l[2]) + (incorrect.get(c_p, 0) * 20)
        elif status == 'I':
            incorrect[c_p] = incorrect.get(c_p, 0) + 1


    rankings = {}
    for k,v in penalty.items():
        team = k[0]
        rank = rankings.get(team, [0, 0])
        rank[0] += 1
        rank[1] += v

        rankings[team] = rank

    result = []
    for team in submitted:
        v = rankings.get(team, [0, 0])
        result.append((-v[0], v[1], team))

    return sorted(result)


def solve_case(f):
    submissions = [l.strip().split() for l in iter(lambda: next(f), '\n')]

    rankings = get_ranking(submissions)

    for i in rankings:
        print("{} {} {}".format(i[2], -i[0], i[1]))


for i in range(t):
    if i > 0:
        print()
    solve_case(f)

