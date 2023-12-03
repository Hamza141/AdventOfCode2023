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

potential_gears = defaultdict(list)

for row, l in enumerate(lines):
    col = 0
    while col < len(l):
        potential_gear = None
        start = -1
        while col < len(l) and lines[row][col].isdigit():
            if start == -1:
                start = col
            if potential_gear is None:
                dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                for d in dirs:
                    if 0 <= row + d[0] < len(lines) and 0 <= col + d[1] < len(lines[row]):
                        check = lines[row+d[0]][col+d[1]]
                        if check == '.' or check.isdigit():
                            continue
                        elif check == '*':
                            potential_gear = (row+d[0], col+d[1])
                            break
            col += 1
        if potential_gear:
            potential_gears[potential_gear].append(int(lines[row][start:col]))
        else:
            col += 1
    pass

for p in potential_gears.values():
    if len(p) == 2:
        ans += p[0] * p[1]

print(ans)
