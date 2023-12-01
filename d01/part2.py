from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

ans = 0
for l in lines:
    digits = []
    for i, c in enumerate(l):
        if c.isdigit():
            digits.append(int(c))
        else:
            for n in nums:
                if i+len(n) <= len(l) and l[i:i+len(n)] == n:
                    digits.append(nums[n])

    ans += (digits[0] * 10) + digits[-1]


print(ans)
