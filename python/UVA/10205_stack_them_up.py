import fileinput

f = fileinput.input()

t = int(next(f))
next(f)

def shuffle(deck, permutation):
    new_deck = list(range(52))
    for i in range(52):
        new_deck[i] = deck[permutation[i] - 1]
    return new_deck

values = "2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace".split(", ")
suits = "Clubs, Diamonds, Hearts, Spades".split(", ")

def print_deck(deck):
    for i in range(52):
        card = deck[i]
        print("{} of {}".format(values[card % 13], suits[card // 13]))

def solve(shuffles, observed):
    deck = list(range(52))
    for s in observed:
        deck = shuffle(deck, shuffles[s])

    print_deck(deck)

def solve_case(f):
    n = int(next(f))
    shuffles = []
    for i in range(n):
        s = get_line(f)
        while len(s) < 52:
            s.extend(get_line(f))
        shuffles.append(s)
    observed = [int(l) - 1 for l in iter(lambda: next(f), '\n')]

    solve(shuffles, observed)

def get_line(f):
    return list(map(int, next(f).strip().split()))

for i in range(t):
    if i > 0:
        print()
    solve_case(f)
