from pathlib import Path
import time
from shapely import Polygon, Point

start_time = time.time()

with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

dirs = {'3': (-1, 0), '0': (0, 1), '1': (1, 0), '2': (0, -1)}
trenchedge = [(0, 0)]
pos = (0, 0)

for line in lines:
    _, _, h = line.split()
    value = int(h[2:-2], 16)
    dir = dirs[h[-2]]
    pos = (pos[0] + dir[0] * value, pos[1] + dir[1] * value)
    trenchedge.append(pos)

trench = Polygon(trenchedge)
area = trench.area + (trench.length / 2) + 1

print(f'⭐ Part 1: {int(area)}, run time: {int((time.time() - start_time) * 1000)}ms')
