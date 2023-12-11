from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0

COLS = len(lines[0])
ROWS = len(lines)
grid = [[0 for j in range(COLS)] for i in range(ROWS)]
emptyRows = []
emptyCols = []
galaxies = []

for i in range(ROWS):
    isEmpty = True
    for j in range(COLS):
        grid[i][j] = lines[i][j]
        if grid[i][j] == '#':
            galaxies.append((i, j))
            isEmpty = False
    if isEmpty:
        emptyRows.append(i)

for j in range(COLS):
    isEmpty = True
    for i in range(ROWS):
        if grid[i][j] == '#':
            isEmpty = False
            break
    if isEmpty:
        emptyCols.append(j)

distances = {}


for i, g0 in enumerate(galaxies):
    for j, g1 in enumerate(galaxies):
        if g0 == g1:
            continue
        if (i, j) in distances or (j, i) in distances:
            continue
        d = abs(g0[0] - g1[0]) + abs(g0[1] - g1[1])
        for r in emptyRows:
            if min(g0[0], g1[0]) <= r <= max(g1[0], g0[0]):
                d += 1
        for c in emptyCols:
            if min(g0[1], g1[1]) <= c <= max(g1[1], g0[1]):
                d += 1
        distances[(i, j)] = d

ans = sum(distances.values())
print(ans)
