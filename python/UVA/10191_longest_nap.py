import fileinput
import re

f = fileinput.input()


def format_time(minute):
    if minute < 60:
        return "{} minutes".format(minute)
    else:
        return "{} hours and {} minutes".format(minute // 60, minute % 60)

pattern = re.compile(r'(\d+):(\d+) ((\d+):(\d+))')


def convert(match):
    time = [int(match.group(i)) for i in [1, 2, 4, 5]]
    start = get_time(time[0], time[1])
    end = get_time(time[2], time[3])
    return start, end, match.group(3)


def get_time(hour, minute):
    return hour * 60 + minute


def solve(n, lines):
    schedule = []
    for l in lines:
        match = pattern.match(l)
        if match:
            schedule.append(convert(match))
        else:
            raise Exception("Unexpected line")

    schedule.append((get_time(18, 0), get_time(18, 0), ''))
    schedule.sort()

    max_start = "10:00"
    max_nap = schedule[0][0] - get_time(10, 0)
    for i in range(n):
        nap = schedule[i + 1][0] - schedule[i][1]
        if nap > max_nap:
            max_nap = nap
            max_start = schedule[i][2]
    return max_start, max_nap

count = 1
for l in f:
    n = int(l)
    lines = [next(f) for i in range(n)]
    result = solve(n, lines)
    print('Day #{}: the longest nap starts at {} and will last for {}.'.format(count, result[0], format_time(result[1])))
    count += 1

