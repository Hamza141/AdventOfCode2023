from heapq import heapify, heappop, heappush
import sys
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = sys.maxsize

COLS = len(lines[0])
ROWS = len(lines)
grid = [[0 for j in range(COLS)] for i in range(ROWS)]
# visited = [[False for j in range(COLS)] for i in range(ROWS)]
# distance = [[sys.maxsize for j in range(COLS)] for i in range(ROWS)]


for i in range(ROWS):
    for j in range(COLS):
        grid[i][j] = int(lines[i][j])


up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)
dirs = {up: '^', down: 'v', left: '<', right: '>'}
r_dirs = {'^': up, 'v': down, '<': left, '>': right}
other_dirs = {'>': [up, down],
              '<': [up, down],
              '^': [left, right],
              'v': [left, right],
              }

h = []
heapify(h)
for d in [down, right]:
    di = d[0]
    dj = d[1]
    heappush(h, (0, di, dj, 1, dirs[d]))
seen = set()
while len(h):
    heatLoss, i, j, consecutive, heading = heappop(h)
    if i < 0 or j < 0 or i >= ROWS or j >= COLS:
        continue
    if i == ROWS - 1 and j == COLS - 1:
        if consecutive < 4:
            continue
        print(ans, heatLoss)
        heatLoss += grid[i][j]
        ans = min(ans, heatLoss)
        break
    if (i, j, consecutive, heading) in seen:
        continue
    seen.add((i, j, consecutive, heading))

    if consecutive < 10:
        same_dir = r_dirs[heading]
        di = same_dir[0] + i
        dj = same_dir[1] + j
        heappush(h, (grid[i][j] + heatLoss, di, dj,
                     consecutive+1, heading))

    if consecutive >= 4:
        current_dirs = other_dirs[heading]
        for d in current_dirs:
            di = d[0] + i
            dj = d[1] + j
            heappush(h, (grid[i][j] + heatLoss, di, dj, 1, dirs[d]))


print(ans)
