from pathlib import Path
import time
from sympy import Point2D

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    grid = [list(line) for line in f.read().split('\n')]

visited = set()
neigbohurs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
price = 0

for row, line in enumerate(grid):
    for col, plant in enumerate(line):
        if (row, col) in visited:
            continue
        fences = 0
        area = 0
        queue = [Point2D(row, col)]
        while queue:
            pos = queue.pop()
            visited.add(pos.args)
            area += 1
            for nr, nc in [pos + n for n in neigbohurs]:
                if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]) or grid[nr][nc] != plant:
                    fences += 1
                elif (nr, nc) not in visited and Point2D(nr, nc) not in queue:
                    queue.append(Point2D(nr, nc))
        price += area * fences
        pass

answer = price
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
