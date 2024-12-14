from collections import defaultdict
from itertools import pairwise
from pathlib import Path
import time
from sympy import Point2D

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    grid = [list(line) for line in f.read().split('\n')]

visited = set()
price = 0


def calculatesides(area: list) -> int:
    around = []
    for r, c in area:
        for nl, na in zip([(r + n1, c + n2) for n1, n2 in [(-0.1, 0), (0, 0.1), (0.1, 0), (0, -0.1)]],
                          [(r + n1, c + n2) for n1, n2 in [(-1, 0), (0, 1), (1, 0), (0, -1)]]):
            if na not in area:
                around.append(nl)

    rowgroups = defaultdict(list)
    for r, c in [(r, c) for r, c in around if r % 1 != 0]:
        rowgroups[r].append(c)
    colgroups = defaultdict(list)
    for r, c in [(r, c) for r, c in around if c % 1 != 0]:
        colgroups[c].append(r)

    lines = 0
    for line in rowgroups.values():
        lines += 1
        for n1, n2 in pairwise(sorted(line)):
            if n2 - n1 > 1:
                lines += 1
    for line in colgroups.values():
        lines += 1
        for n1, n2 in pairwise(sorted(line)):
            if n2 - n1 > 1:
                lines += 1
    return lines


for row, line in enumerate(grid):
    for col, plant in enumerate(line):
        if (row, col) in visited:
            continue
        fences = 0
        area = set()
        queue = [Point2D(row, col)]
        while queue:
            pos = queue.pop()
            visited.add(pos.args)
            area.add(pos.args)
            for nr, nc in [pos + n for n in [(-1, 0), (0, 1), (1, 0), (0, -1)]]:
                if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]) or grid[nr][nc] != plant:
                    fences += 1
                elif (nr, nc) not in visited and Point2D(nr, nc) not in queue:
                    queue.append(Point2D(nr, nc))
        price += calculatesides(sorted(list(area))) * len(area)

answer = price
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
