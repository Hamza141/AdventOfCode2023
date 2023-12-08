from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0
adj_list = {}

instructions = lines[0]

for row, l in enumerate(lines[2:]):
    l = l.split('=')
    cur = l[0].strip()
    left, right = l[1][2:-1].split(', ')
    adj_list[cur] = (left, right)

step = 0

cur = 'AAA'
while True:
    dir = instructions[step % len(instructions)]

    if cur == 'ZZZ':
        print(step)
        break
    elif dir == 'L':
        cur = adj_list[cur][0]
    elif dir == 'R':
        cur = adj_list[cur][1]

    step += 1
