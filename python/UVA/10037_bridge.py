import fileinput

f = fileinput.input()

cases = int(next(f))
next(f)

def solve(speeds):
    t = []
    p = []

    for l in range(len(speeds)):
        if l == 0:
            t.append(speeds[0])
            p.append((speeds[:1],))
        elif l == 1:
            t.append(max(speeds[:2]))
            p.append((speeds[:2],))
        elif l == 2:
            t.append(sum(speeds[:3]))
            p.append(((speeds[0], speeds[l]), (speeds[0],), speeds[:2]))
        else:
            t1, p1 = t[l - 1], p[l - 1]
            total1 = t1 + speeds[0] + speeds[l]

            t2, p2 = t[l - 2], p[l - 2]
            total2 = t2 + speeds[0] + speeds[l] + 2*speeds[1]

            if total1 < total2:
                t.append(total1)
                p.append(((speeds[0], speeds[l]), (speeds[0],)) + p1)
            else:
                t.append(total2)
                p.append((speeds[:2], (speeds[0],), speeds[l-1:l+1], (speeds[1],)) + p2)

    return t[-1], p[-1]


def solve_case(f):
    n = int(next(f))
    speeds = tuple(sorted(int(next(f)) for i in range(n)))

    total, plan = solve(speeds)
    assert total == sum(max(p) for p in plan)
    print(total)
    for p in plan:
        print(*p)


for i in range(cases):
    if i > 0:
        print()
        next(f)
    solve_case(f)
