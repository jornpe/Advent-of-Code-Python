from pathlib import Path
import time
import re
from itertools import product

from matplotlib import pyplot as plt

start_time = time.time()
with open(Path(__file__).with_name('test.txt')) as f:
    lines = [line for line in f.read().split('\n')]

bricksinput = [list(map(int, re.findall(r'\d+', b))) for b in lines]
bricksinput.sort(key=lambda x: x[2])
bricks = []
fallenBricks = []
brickgrid = set()

# get all coordinates for a brick
for b in bricksinput:
    start = b[0:3]
    end = b[3::]

    min_p = [min(start[i], end[i]) for i in range(3)]
    max_p = [max(start[i], end[i]) for i in range(3)]
    coords = tuple(product(range(min_p[0], max_p[0] + 1), range(min_p[1], max_p[1] + 1), range(min_p[2], max_p[2] + 1)))
    bricks.append(coords)


def canmovedown(brick: tuple, grid: set) -> bool:
    zlow = min(z for x, y, z in brick)
    return zlow > 1 and all((x, y, z - 1) not in grid for x, y, z in brick if z == zlow)


# let the bricks fall
for brick in bricks:
    while canmovedown(brick, brickgrid):
        brick = tuple((x, y, z - 1) for x, y, z in brick)
    fallenBricks.append(brick)
    for coord in brick:
        brickgrid.add(coord)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for b in fallenBricks:
    (sx, sy, sz) = b[0]
    (x, y, z) = b[-1]
    ax.plot([sx, x], [sy, y], [sz, z], linewidth=10)

plt.show()

# count how many can be pulled out
canbepulled = 0
for brick in fallenBricks:
    grid = brickgrid.difference(set(c for c in brick))
    canbepulled += 0 if any(canmovedown(br, grid) for br in fallenBricks if br != brick) else 1


print(f'⭐ Part 1: {canbepulled}, run time: {int((time.time() - start_time) * 1000)}ms')
