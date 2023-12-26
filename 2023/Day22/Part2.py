from pathlib import Path
import time
import re
from itertools import product

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

bricksinput = [list(map(int, re.findall(r'\d+', b))) for b in lines]
bricksinput.sort(key=lambda x: x[2])
bricks = []
fallenBricks = []
brickset = set()
brickgrid = {}
abovebricks = {}

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


def get_above_bricks(brick: tuple, grid: dict) -> tuple:
    zover = max(z for x, y, z in brick) + 1
    return tuple(grid[(x, y, zover)] for x, y, z in brick if (x, y, zover) in grid)


# let the bricks fall
for brick in bricks:
    while canmovedown(brick, brickset):
        brick = tuple((x, y, z - 1) for x, y, z in brick)
    fallenBricks.append(brick)
    for coord in brick:
        brickgrid[coord] = brick
        brickset.add(coord)

# map all above bricks
for brick in fallenBricks:
    abovebricks[brick] = get_above_bricks(brick, brickgrid)

# pull out bricks
count = 0
for brick in fallenBricks:
    queue = [brick]
    grid = brickset.copy()
    while queue:
        grid = grid.difference(set(c for b in queue for c in b))
        above = [b for ab in queue for b in abovebricks[ab]]
        queue.clear()
        for br in set(above):
            if canmovedown(br, grid):
                queue.append(br)
                count += 1


print(f'⭐⭐ Part 2: {count}, run time: {int((time.time() - start_time) * 1000)}ms')
