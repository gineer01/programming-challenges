import collections

Hand = collections.namedtuple("Hand", ['StraightFlush', # the highest card
                                       'Four', # the value of 4 cards
                                       'FullHouse', # the value of 3 cards
                                       'Flush', # the tuples of 5 cards
                                       'Straight', # the value of highest card
                                       'Three', # the value of 3 cards
                                       'TwoPairs', # the tuples of 5 cards
                                       'Pair', # the tuples of 5 cards,
                                       'HighCard', # the tuples of 5 cards
                                       ])

empty_hand = Hand(0, 0, 0, [], 0, 0, [], [], [])

import fileinput

f = fileinput.input()


def convert_value(card_value):
    if '2' <= card_value <= '9':
        return int(card_value)
    elif card_value == 'T':
        return 10
    elif card_value == 'J':
        return 11
    elif card_value == 'Q':
        return 12
    elif card_value == 'K':
        return 13
    elif card_value == 'A':
        return 14
    else:
        raise Exception("Invalid value")


def is_flush(suits):
    return len(suits) == 1


def is_straight(values):
    return all([values[i] == values[i - 1] - 1 for i in range(1, 5)])


def is_four(counter):
    count = counter.most_common(1)[0][1]
    return count == 4


def is_full_house(counter):
    groups = counter.most_common(2)
    count1 = groups[0][1]
    count2 = groups[1][1]
    return count1 == 3 and count2 == 2


def is_three(counter):
    count = counter.most_common(1)[0][1]
    return count == 3

def is_pair(counter):
    count = counter.most_common(1)[0][1]
    return count == 2


def is_two_pairs(counter):
    groups = counter.most_common(2)
    count1 = groups[0][1]
    count2 = groups[1][1]
    return count1 == 2 and count2 == 2


def get_list(counter):
    sorted_by_count_value = sorted(counter.most_common(), key=lambda t: (t[1], t[0]), reverse=True)
    return [i[0] for i in sorted_by_count_value]


def build_hand(cards):
    values = sorted((convert_value(c[0]) for c in cards), reverse=True)
    suits = set((c[1] for c in cards))
    counter = collections.Counter(values)

    if is_straight(values) and is_flush(suits):
        return empty_hand._replace(StraightFlush = values[0])
    elif is_four(counter):
        return empty_hand._replace(Four=(get_value(counter)))
    elif is_full_house(counter):
        return empty_hand._replace(FullHouse=(get_value(counter)))
    elif is_flush(suits):
        return empty_hand._replace(Flush=values)
    elif is_straight(values):
        return empty_hand._replace(Straight = values[0])
    elif is_three(counter):
        return empty_hand._replace(Three=(get_value(counter)))
    elif is_two_pairs(counter):
        return empty_hand._replace(TwoPairs= get_list(counter))
    elif is_pair(counter):
        return empty_hand._replace(Pair= get_list(counter))
    else:
        return empty_hand._replace(HighCard= values)


def get_value(counter):
    return counter.most_common(1)[0][0]


def compare_hand(black, white):
    b_hand = build_hand(black)
    w_hand = build_hand(white)
    if b_hand == w_hand:
        return "Tie."
    elif b_hand > w_hand:
        return "Black wins."
    else:
        return "White wins."


def process_line(l):
    a = l.strip().split()
    print(compare_hand(a[:5], a[5:]))


for l in f:
    process_line(l)

# print(build_hand(["AH", "KH", "QH", "TH", "JH"]))
# print(build_hand(["AH", "AH", "AH", "AH", "JH"]))
# print(build_hand(["AH", "AH", "AH", "JH", "JH"]))
# print(build_hand(["AH", "3H", "2H", "JH", "TH"]))
# print(build_hand(["AH", "KH", "QH", "TH", "JC"]))
# print(build_hand(["AH", "AH", "AH", "TC", "JH"]))
# print(build_hand(["AH", "AH", "TH", "TC", "JH"]))
# print(build_hand(["3H", "3H", "2H", "TC", "JH"]))
# print(build_hand(["AH", "KH", "2H", "TC", "JH"]))

