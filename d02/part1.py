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
    game_id = int(l.split(':')[0].split()[1])
    sets = l.split(':')[1].split(';')
    skip = False
    for s in sets:
        allowed = {'red': 12, 'green': 13, 'blue': 14}
        colors = s.split(',')
        for c in colors:
            num, color = c.strip().split()
            if allowed[color] < int(num):
                skip = True
                break
        if skip:
            break
    if not skip:
        ans += game_id

print(ans)
