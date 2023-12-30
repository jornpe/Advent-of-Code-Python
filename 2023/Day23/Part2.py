from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

grid = set()
end = (len(lines) - 2, len(lines[-1]) - 2)
longest = 0
directions = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char != '#': grid.add((r, c))


turns = {(0, 1): {}, end: {}}

# get all the turns in the grid
for r, c in grid:
    if sum([1 for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)] if (r + dr, c + dc) in grid]) > 2:
        turns[(r, c)] = {}

# populate all turns with their connections to other turns, start and end and how many steps are in between.
for r, c in turns:
    neibours = {}
    steps = 0
    paths = [[(r, c)]]
    while paths:
        temppaths = paths.copy()
        paths.clear()
        steps += 1
        while temppaths:
            path = temppaths.pop()
            row, col = path[-1]
            if (row, col) in turns and (row, col) != (r, c):
                neibours[(row, col)] = steps - 1
                continue
            for dr, dc in directions.keys():
                nr = row + dr
                nc = col + dc
                if (nr, nc) in grid and (nr, nc) not in path:
                    paths.append(path + [(nr, nc)])
        turns[r, c] = neibours

# get the longest route
paths = [(1, [(0, 1)])]
while paths:
    cost, path = paths.pop()
    pos = path[-1]
    pos = tuple(pos)
    if pos == end:
        if longest < cost:
            longest = cost
        continue
    for s, d in turns[pos].items():
        if s not in path:
            paths.append((cost + d, path + [s]))


print(f'⭐⭐ Part 2: {longest}, run time: {int((time.time() - start_time) * 1000)}ms')
