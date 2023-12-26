from pathlib import Path
import time
from shapely import LineString, intersection
from itertools import combinations
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

xymin = 200000000000000
xymax = 400000000000000
intersections = 0


def get_end(x, y, vx, vy) -> tuple:
    x_mul = abs(x - xymax) / abs(vx) if vx > 0 else abs(x - xymin) / abs(vx)
    y_mul = abs(y - xymax) / abs(vy) if vy > 0 else abs(y - xymin) / abs(vy)
    multiplier = max(x_mul, y_mul)
    return int(x + (vx * multiplier)), int(y + (vy * multiplier))


for l1, l2 in combinations(lines, 2):
    x1, y1, z1, vx1, vy1, vz1 = list(map(int, re.findall(r'(-?\d+)', l1)))
    x2, y2, z2, vx2, vy2, vz2 = list(map(int, re.findall(r'(-?\d+)', l2)))

    line1 = LineString([(x1, y1), get_end(x1, y1, vx1, vy1)])
    line2 = LineString([(x2, y2), get_end(x2, y2, vx2, vy2)])

    ix, iy = intersection(line1, line2).coords.xy

    if ix and iy and xymin <= ix[0] <= xymax and xymin <= iy[0] <= xymax:
        intersections += 1

print(f'⭐ Part 1: {intersections}, run time: {int((time.time() - start_time) * 1000)}ms')
