from collections import defaultdict
from email.policy import default
from operator import mul
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

ans = 0

todo = set()
for s in lines[0].split(':')[1].split():
    todo.add(int(s))

current_map = []
done = set()


def process(current_map):
    got_done = set()
    for i in current_map:
        dest, source, range_len = i
        for s in todo:
            if source <= s < source + range_len:
                move = s - source
                done.add(dest+move)
                got_done.add(s)

    for s in todo:
        if s in got_done:
            continue
        done.add(s)


for row, l in enumerate(lines[1:]):
    if len(l.strip()) == 0:
        continue
    if 'map' in l:
        if len(current_map) != 0:
            process(current_map)
            current_map = []
            todo = done
            done = set()
        continue

    dest, source, range_len = l.split()
    dest, source, range_len = int(dest), int(source), int(range_len)
    current_map.append((dest, source, range_len))

process(current_map)

print(min(done))
