from collections import defaultdict
from email.policy import default
from operator import mul
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0

cards = defaultdict(int)

for row, l in enumerate(lines):
    l = l.split(':')
    card = int(l[0].split()[1])
    cards[card] += 1
    winning = set(l[1].split('|')[0].split())
    yours = l[1].split('|')[1].split()

    num_matches = 0
    for n in yours:
        if n in winning:
            num_matches += 1

    if num_matches != 0:
        for j in range(cards[card]):
            for i in range(num_matches):
                cards[i + 1 + card] += 1

    ans += cards[card]

print(ans)
