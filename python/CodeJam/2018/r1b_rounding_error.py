import fileinput
import math


def solve(n, l, survey):
    # print(n, l, survey)
    percentage = [i * 100 /n for i in range(n)]
    round_index = n
    distance = []
    for i in range(n):
        index = n - 1 - i
        a = percentage[index]
        if math.floor(a + 0.5) > a:
            round_index = index

        distance.append(round_index - index)
    distance.reverse()

    total = sum(survey)
    remaining = n - total

    d = [distance[i] for i in survey]
    d.sort()
    survey.sort(key=lambda i: distance[i])

    i = 0
    while remaining > 0:
        if i < len(d):
            if d[i] == 0:
                i += 1
                continue

            if d[i] <= distance[0]:
                to_add = min(remaining, d[i])
                survey[i] += to_add
                remaining -= to_add
                i += 1
                continue

        to_add = min(remaining, distance[0])
        survey.append(to_add)
        remaining -= to_add

    return sum(math.floor(x * 100 /n + 0.5) for x in survey)


assert solve(10, 3, [1, 3, 2]) == 100
assert solve(6, 2, [3, 1]) == 101

def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        n, l = [int(x) for x in next(f).split()]
        survey = [int(x) for x in next(f).split()]
        print("Case #%s: %s" % (i + 1, solve(n, l, survey)))

main()
