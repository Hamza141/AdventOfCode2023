from functools import cmp_to_key
from os.path import dirname, abspath, join
from collections import Counter


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0

fives = {}
fours = {}
fulls = {}
threes = {}
twos = {}
ones = {}
highs = {}


def handle_J(count):
    if 'J' in count:
        j = count.pop('J')
        highest = 0
        highest_c = ''
        for c in count:
            if count[c] > highest:
                highest = count[c]
                highest_c = c
        count[highest_c] += j

    return count


def check_five(hand):
    count = Counter(hand)
    handle_J(count)
    if len(count.keys()) == 1:
        return True
    return len(hand) == hand.count(hand[0])


def check_four(hand):
    count = Counter(hand)
    handle_J(count)
    if len(count.keys()) == 2:
        for k in count:
            if count[k] != len(hand) - 1 and count[k] != 1:
                return False
        return True
    return False


def check_full(hand):
    count = Counter(hand)
    handle_J(count)
    if len(count.keys()) == 2:
        for k in count:
            if count[k] != len(hand) - 2 and count[k] != 2:
                return False
        return True
    return False


def check_three(hand):
    count = Counter(hand)
    handle_J(count)
    if len(count.keys()) == 3:
        for k in count:
            if count[k] != len(hand) - 2 and count[k] != 1:
                return False
        return True
    return False


def check_two(hand):
    count = Counter(hand)
    handle_J(count)
    if len(count.keys()) == 3:
        for k in count:
            if count[k] != 2 and count[k] != 1:
                return False
        return True
    return False


def check_one(hand):
    count = Counter(hand)
    handle_J(count)
    if len(count.keys()) == 4:
        for k in count:
            if count[k] != 2 and count[k] != 1:
                return False
        return True
    return False


def check_high(hand):
    count = Counter(hand)
    handle_J(count)
    if len(count.keys()) == len(hand):
        return True
    return False


for row, l in enumerate(lines):
    hand, bid = l.split()
    if check_five(hand):
        fives[hand] = bid
    elif check_four(hand):
        fours[hand] = bid
    elif check_full(hand):
        fulls[hand] = bid
    elif check_three(hand):
        threes[hand] = bid
    elif check_two(hand):
        twos[hand] = bid
    elif check_one(hand):
        ones[hand] = bid
    elif check_high(hand):
        highs[hand] = bid
    else:
        print("ERROR")

strength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def rank(hand1, hand2):
    for i in range(len(hand1)):
        h1 = hand1[i]
        h2 = hand2[i]
        s1 = strength.index(h1)
        s2 = strength.index(h2)
        if s1 < s2:
            return 1
        elif s2 < s1:
            return -1
    print("EXACTLY THE SAME")
    return 0


sorted_fives = sorted(list(fives.keys()), key=cmp_to_key(rank))
sorted_fours = sorted(list(fours.keys()), key=cmp_to_key(rank))
sorted_fulls = sorted(list(fulls.keys()), key=cmp_to_key(rank))
sorted_threes = sorted(list(threes.keys()), key=cmp_to_key(rank))
sorted_twos = sorted(list(twos.keys()), key=cmp_to_key(rank))
sorted_ones = sorted(list(ones.keys()), key=cmp_to_key(rank))
sorted_highs = sorted(list(highs.keys()), key=cmp_to_key(rank))

rank = 1


def calc(hands, mapping):
    global ans, rank
    for h in hands:
        ans += (int(mapping[h]) * rank)
        print((int(mapping[h]),  rank))
        rank += 1


calc(sorted_highs, highs)
calc(sorted_ones, ones)
calc(sorted_twos, twos)
calc(sorted_threes, threes)
calc(sorted_fulls, fulls)
calc(sorted_fours, fours)
calc(sorted_fives, fives)

print(ans)
