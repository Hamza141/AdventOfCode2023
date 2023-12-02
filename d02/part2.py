from collections import defaultdict
from os.path import dirname, abspath, join
from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0

for l in lines:
    sets = l.split(':')[1].split(';')
    required = defaultdict(int)
    for s in sets:
        colors = s.split(',')
        for c in colors:
            num, color = c.strip().split()
            required[color] = max(required[color], int(num))
    ans += (required['red'] * required['blue'] * required['green'])

print(ans)
