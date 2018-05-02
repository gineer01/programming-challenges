import fileinput
import itertools
from collections import Counter

f = fileinput.input()

cases = int(next(f))
next(f)


def all_good(lines, group_by_length, content):
    # print("Trying " + content)
    for l in lines:
        if not (content.startswith(l) or content.endswith(l)):
            return False
    return True


def find_content(lines, group_by_length, possibilities):
    for p in possibilities:
        content = p[0] + p[1]
        if all_good(lines, group_by_length, content):
            return content

        content = p[1] + p[0]
        if all_good(lines, group_by_length, content):
            return content

def solve(lines):
    assert len(lines) % 2 == 0
    n = len(lines) // 2
    length_list = list(map(len, lines))
    expected_length = sum(length_list) // n

    lines.sort(key=len)
    group_by_length = {k:list(g) for k,g in itertools.groupby(lines, key=len)}

    c = Counter(length_list)
    least_common = c.most_common()[-1]

    one_half = least_common[0]
    other_half = expected_length - least_common[0]
    if one_half == other_half:
        possibilities = set(itertools.combinations(group_by_length[one_half], 2))
    else:
        possibilities = set(itertools.product(group_by_length[one_half], group_by_length[other_half]))

    print(find_content(lines, group_by_length, possibilities))



def process_case(f):
    lines = []

    for l in f:
        if l.strip():
            lines.append(l.strip())
        else:
            break

    solve(lines)


for i in range(cases):
    if i > 0:
        print()
    process_case(f)

