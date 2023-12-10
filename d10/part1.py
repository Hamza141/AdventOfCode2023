from collections import deque
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0

rows = lines

grid = [[0 for i in range(len(rows[0]))] for j in range(len(rows))]
start = (0, 0, 0)
for j in range(len(rows)):
    for i in range(len(rows[0])):
        grid[i][j] = rows[i][j]
        if rows[i][j] == 'S':
            start = (i, j, 0)

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)
valid = {'|': [up, down],
         '-': [left, right],
         'L': [up, right],
         'J': [up, left],
         '7': [left, down],
         'F': [down, right],
         'S': [up, down, left, right]}

q = deque([start])
seen = {}
opp = {up: down, down: up, left: right, right: left}


def isValid(cur_d, new_char):
    if new_char not in valid:
        return False
    opp_cur = opp[cur_d]
    if opp_cur in valid[new_char]:
        return True
    return False


while q:
    i, j, count = q.popleft()
    seen[(i, j)] = count
    cur = grid[i][j]
    dirs = valid[cur]
    ans = max(count, ans)
    for d in dirs:
        di = i + d[0]
        dj = j + d[1]
        if (di, dj) in seen:
            continue
        if di < 0 or di >= len(rows) or dj < 0 or dj >= len(rows[0]):
            continue
        if not isValid(d, grid[di][dj]):
            continue
        q.append((di, dj, count + 1))


print(ans)
