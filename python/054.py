# this problem wasn't math at all ):

f = [x.split(' ') for x in open('poker.txt').read().strip().split('\n')]

wins = 0

def score(hand):
    STRAIGHT_FLUSH = 10**45
    QUADS = 10**40
    HOUSE = 10**35
    FLUSH = 10**30
    STRAIGHT = 10**25
    TRIPS = 10**20
    TWOPAIR = 10**15
    PAIR = 10**10

    values = sorted(['!!23456789TJQKA'.index(x[0]) for x in hand])
    suits = [x[1] for x in hand]

    is_straight = sum(values) == 4 * values[0] + 10
    is_flush = len(set(suits)) == 1

    if is_straight and is_flush:
        return STRAIGHT_FLUSH + values[-1]

    if len(set(suits)) == 2:
        if values.count(values[0]) == 1:
            return QUADS * values[-1] + values[0]
        if values.count(values[0]) == 2:
            return HOUSE * values[-1] + values[0]
        if values.count(values[0]) == 3:
            return HOUSE * values[0] + values[-1]
        if values.count(values[0]) == 4:
            return QUADS * values[0] + values[-1]

    if is_flush:
        return FLUSH * values[-1]

    if is_straight:
        return STRAIGHT * values[-1]

    if 3 in [values.count(x) for x in values]:
        c = [x for x in values if values.count(x) == 3][0]
        e = [x for x in values if x != c]
        return TRIPS * c + e[1] * 100 + e[0]

    if [values.count(x) for x in values].count(2) == 4:
        c1, c2 = sorted(list(set([x for x in values if values.count(x) == 2])))
        extra = [x for x in values if values.count(x) == 1][0]
        return TWOPAIR * c2 + c1 * 100 + extra

    if [values.count(x) for x in values].count(2) == 2:
        c = [x for x in values if values.count(x) == 2][0]
        e = [x for x in values if x != c]
        return PAIR * c + 10000 * e[2] + 100 * e[1] + e[2]

    return 100000000 * values[0] + 1000000 * values[1] + 10000 * values[2] + 100 * values[3] + values[4]


for game in f:
    p1, p2 = game[:5], game[5:]
    wins += score(p1) > score(p2)

print wins
