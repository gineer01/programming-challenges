import fileinput
from collections import Counter

f = fileinput.input()

cases = int(next(f))
next(f)

def find_winner(candidates, ballots):
    total_count = len(ballots)

    tracking = {} # tracking who receives which ballot
    for i in range(total_count):
        tracking.setdefault(ballots[i][0], []).append((i, 0))

    candidates &= set(tracking.keys())

    while len(tracking) > 1:
        counter = Counter({k:len(v) for k,v in tracking.items()})

        ballot_count = counter.most_common()
        top_candidate = ballot_count[0]
        if top_candidate[1] > (total_count / 2):
            return [top_candidate[0]]
        else:
            least_count = ballot_count[-1][1]
            if top_candidate[1] == least_count:#all ties
                return counter.keys()

            i = -1
            while ballot_count[i][1] == least_count:
                remove_candidate(tracking, ballot_count[i][0], candidates, ballots)
                i -= 1

    return tracking


def remove_candidate(tracking, candidate, running, ballots):
    running.remove(candidate)

    for b in tracking[candidate]:
        vote = ballots[b[0]]
        for i in range(b[1] + 1, len(vote)):
            if vote[i] in running:
                tracking.setdefault(vote[i], []).append((b[0], i))
                break

    del tracking[candidate]


def process_case(f):
    n = int(next(f))
    candidates = []
    for i in range(n):
        candidates.append(next(f).strip())

    ballots = []
    for l in f:
        l = l.strip()
        if not l:
            break

        ballots.append(list(map(int, l.split())))

    winners = find_winner(set(range(1, len(candidates) + 1)), ballots)
    for w in sorted(winners):
        print(candidates[w - 1])

process_case(f)
for i in range(1, cases):
    print()
    process_case(f)


