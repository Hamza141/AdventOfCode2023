from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0


def findNext(nums: [int]):
    diffs = []
    zeroes = True
    for i in range(1, len(nums)):
        diff = int(nums[i]) - int(nums[i-1])
        diffs.append(diff)
        if diff != 0:
            zeroes = False
    if zeroes:
        return 0
    return findNext(diffs) + diffs[-1]


for row, l in enumerate(lines):
    nums = l.split()
    num = findNext(nums) + int(nums[-1])
    ans += num

print(ans)
