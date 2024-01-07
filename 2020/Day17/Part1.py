from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    grid = {(row, col, 0) for row, line in enumerate(f.read().split('\n')) for col, char in enumerate(line) if char == '#'}


def get_neighbors(x, y, z) -> list:
    return [(nx, ny, nz) for nx in range(x-1, x+2) for ny in range(y-1, y+2) for nz in range(z-1, z+2)]


for _ in range(6):
    xs, ys, zs = zip(*grid)
    updatedgrid = set()
    for x in range(min(xs) - 1, max(xs) + 2):
        for y in range(min(ys) - 1, max(ys) + 2):
            for z in range(min(zs) - 1, max(zs) + 2):
                neighbors = get_neighbors(x, y, z)
                active = sum(1 for n in neighbors if n in grid)
                if (x, y, z) in grid and (active == 3 or active == 4):
                    updatedgrid.add((x, y, z))
                elif (x, y, z) not in grid and active == 3:
                    updatedgrid.add((x, y, z))
    grid = updatedgrid

answer = len(grid)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
