from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 1

# times = [7, 15, 30]
# distances = [9, 40, 200]

times = [53,     89,     76,     98]
distances = [313,   1090,   1214,   1201]
ways = []

for i in range(len(times)):
    time = times[i]
    dist = distances[i]
    cur = 0

    for t in range(0, time):
        speed = t
        new_dist = speed * (time - t)
        if new_dist > dist:
            cur += 1
    ways.append(cur)
    ans *= cur


print(ans)
