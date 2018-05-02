import fileinput

f = fileinput.input()

cases = int(next(f))

WIN = 1
LOSS = 2
TIE = 3


def check_score(goal1, goal2):
    if goal1 > goal2:
        return WIN, LOSS
    elif goal1 == goal2:
        return TIE, TIE
    else:
        return LOSS, WIN


def update_team(result, team, match_result, goal1, goal2):
    goal_diff = goal1 - goal2
    r = result[team]
    if match_result == WIN:
        r[0] += 3
        r[1] += 1
    elif match_result == TIE:
        r[0] += 1
        r[6] += 1
    else:
        r[7] += 1

    r[2] += goal_diff
    r[3] += goal1
    r[4] -= 1
    r[8] += goal2


def solve(team_names, games):
    result = {t:[0, 0, 0, 0, 0, t.lower(), 0, 0, 0] for t in team_names}

    for g in games:
        team1, score, team2 = g.split('#')
        goal1, goal2 = map(int, score.split('@'))
        a1, a2 = check_score(goal1, goal2)

        update_team(result, team1, a1, goal1, goal2)
        update_team(result, team2, a2, goal2, goal1)

    for i in range(5):
        for k in result:
            result[k][i] = -result[k][i]

    team_names.sort(key=lambda x: result[x])

    for i, t in enumerate(team_names, start=1):
        r = result[t]
        print("{}) {} {}p, {}g ({}-{}-{}), {}gd ({}-{})".format(i, t, -r[0], r[4], -r[1], r[6], r[7], -r[2], -r[3], r[8]))


def solve_case(f):
    tnmt_name = next(f).strip()
    n = int(next(f))
    team_names = [next(f).strip() for i in range(n)]

    g = int(next(f))
    games = [next(f).strip() for i in range(g)]

    print(tnmt_name)
    solve(team_names, games)


for i in range(cases):
    if i > 0:
        print()
    solve_case(f)

