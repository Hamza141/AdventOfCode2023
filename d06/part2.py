from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 1

# times = [71530]
# distances = [940200]

times = [53897698]
distances = [313109012141201]
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
