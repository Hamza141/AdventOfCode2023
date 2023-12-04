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

for row, l in enumerate(lines):
    l = l.split(':')
    winning = set(l[1].split('|')[0].split())
    yours = l[1].split('|')[1].split()
    cur = 0
    for n in yours:
        if n in winning:
            # cur = cur << 1 or 1
            if cur == 0:
                cur += 1
            else:
                cur *= 2
    ans += cur

print(ans)
