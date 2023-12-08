from collections import defaultdict, deque
import math
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

adj_list = {}
instructions = lines[0]
location = deque()

for row, l in enumerate(lines[2:]):
    l = l.split('=')
    cur = l[0].strip()
    left, right = l[1][2:-1].split(', ')
    adj_list[cur] = (left, right)
    if cur[-1] == 'A':
        location.append(cur)

step = 0
finished = {}

while True:
    dir = instructions[step % len(instructions)]

    for i in range(len(location)):
        cur = location.popleft()

        if cur[-1] == 'Z':
            if cur not in finished:
                finished[cur] = step
        if dir == 'L':
            location.append(adj_list[cur][0])
        elif dir == 'R':
            location.append(adj_list[cur][1])

    step += 1

    if len(finished) == len(location):
        print(math.lcm(*finished.values()))
        break
