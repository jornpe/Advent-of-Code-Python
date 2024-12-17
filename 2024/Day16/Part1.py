from pathlib import Path
import time
from queue import PriorityQueue

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

pos = ()
grid = []
for row, r in enumerate(lines):
    line = []
    for col, c in enumerate(r):
        if c == 'S':
            pos = (row, col)
        line.append(c)
    grid.append(line)


def getcheapestpath(pos: tuple, dir: tuple) -> int:
    queue = PriorityQueue()
    queue.put((0, pos, dir))
    visited = set()
    while True:
        v, p, d = queue.get()
        if (p, d) in visited:
            continue
        if grid[p[0]][p[1]] == 'E':
            return v
        if grid[p[0]][p[1]] == '#':
            continue

        visited.add((p, d))
        queue.put((v + 1, (p[0] + d[0], p[1] + d[1]), d))
        queue.put((v + 1000, p, (-d[1], d[0])))
        queue.put((v + 1000, p, (d[1], -d[0])))



answer = getcheapestpath(pos, (0, 1))
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
