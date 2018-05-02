import fileinput
import collections

SUIT = 1
RANK = 0

points = {
    'A' : 4,
    'K' : 3,
    'Q' : 2,
    'J' : 1
}


def rule_1_val(cards):
    return sum(points.get(h[RANK], 0) for h in cards)


def rule_2_4_val(suit_rank, suit_counter):
    val = 0
    for s in SUITS:
        if s in suit_rank:
            ranks = suit_rank[s]
            count = suit_counter[s]
            if 'K' in ranks and count == 1:
                val += 1
            if 'Q' in ranks and (count == 1 or count == 2):
                val += 1
            if 'J' in ranks and (count == 1 or count == 2 or count == 3):
                val += 1

    return val


def rule_5_7_val(cards, suit_counter):
    val = 0
    for suit in SUITS:
        count = suit_counter[suit]
        if count == 2:
            val += 1
        elif count == 1 or count == 0:
            val += 2
    return val


def is_stopped(suit, ranks):
    return 'A' in ranks or ('K' in ranks and len(ranks) > 1) or ('Q' in ranks and len(ranks) > 2)


SUITS = "SHDC"
precedence = {k:v for v,k in enumerate(SUITS)}


def get_suit(suit_counter):
    def get_key(item):
        return (-item[1], precedence[item[0]])

    return sorted(suit_counter.items(), key=get_key)[0][0]


def solve(cards):
    suit_counter = collections.Counter(c[SUIT] for c in cards)
    suit_rank = {}
    for r,s in cards:
        suit_rank.setdefault(s, set()).add(r)
    points = rule_1_val(cards)
    points -= rule_2_4_val(suit_rank, suit_counter)

    total = points + rule_5_7_val(cards, suit_counter)

    stopped = {k:False for k in SUITS}
    for k,v in suit_rank.items():
        stopped[k] = is_stopped(k, v)

    if total < 14:
        return 'PASS'
    else:
        if points >= 16 and all(stopped.values()):
            return 'BID NO-TRUMP'
        else:
            return 'BID ' + get_suit(suit_counter)


    return points + extra


def main():
    f = fileinput.input()
    for l in f:
        cards = [tuple(x) for x in l.strip().split()]
        print(solve(cards))

main()
