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

todo = set()
seed_range = lines[0].split(':')[1].split()

for i in range(0, len(seed_range), 2):
    todo.add((int(seed_range[i]), int(seed_range[i+1])))

current_map = []
done = set()


def process(current_map):
    got_done = set()
    for i in current_map:
        dest, source, range_len = i
        for s in todo:
            start, num = s
            if source <= start < source + range_len:

                move = start - source

                if start + num <= source + range_len:
                    # completely covered
                    done.add((dest+move, num))
                else:
                    # split
                    new_num = source + range_len - start
                    done.add((dest + move, new_num))
                    num_left = start + num - (source + range_len)
                    done.add((source + range_len, num_left))
                got_done.add(s)

            elif source < start+num < source + range_len:
                done.add((dest, start+num-source))
                done.add((start, source - start))
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

ans, _ = min(done)
print(ans)
