from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0
for l in lines:
    digits = []
    for c in l:
        if c.isdigit():
            digits.append(int(c))
    ans += (digits[0] * 10) + digits[-1]


print(ans)
