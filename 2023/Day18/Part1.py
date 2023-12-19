from pathlib import Path
import time
from shapely import Polygon

start_time = time.time()

with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

dirs = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
trenchedge = [(0, 0)]
pos = (0, 0)

for line in lines:
    dir, value, color = line.split()
    value = int(value)
    pos = (pos[0] + dirs[dir][0] * value, pos[1] + dirs[dir][1] * value)
    trenchedge.append(pos)

trench = Polygon(trenchedge)
area = trench.area + (trench.length / 2) + 1

print(f'⭐ Part 1: {int(area)}, run time: {int((time.time() - start_time) * 1000)}ms')
