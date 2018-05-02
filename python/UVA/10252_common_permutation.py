import fileinput
import collections

f = fileinput.input()


def solve(l1, l2):
    result = collections.Counter(l1) & collections.Counter(l2)
    output =[]
    for k in sorted(result):
        output.append(k * result[k])
    print("".join(output))


for l in f:
    l1 = l.strip()
    l2 = next(f).strip()
    solve(l1, l2)
