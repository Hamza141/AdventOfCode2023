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
    col = 0
    while col < len(l):
        part_num = False
        start = -1
        while col < len(l) and lines[row][col].isdigit():
            if start == -1:
                start = col
            if not part_num:
                dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                for d in dirs:
                    if 0 <= row + d[0] < len(lines) and 0 <= col + d[1] < len(lines[row]):
                        check = lines[row+d[0]][col+d[1]]
                        if check == '.' or check.isdigit():
                            continue
                        else:
                            part_num = True
                            break
            col += 1
        if part_num:
            ans += int(lines[row][start:col])
        else:
            col += 1
    pass

print(ans)
