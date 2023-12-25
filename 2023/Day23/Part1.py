from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

grid = {}
paths = [[(0, 1)]]
end = (len(lines) - 2, len(lines[-1]) - 2)
longest = 0
directions = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char != '#': grid[(r, c)] = char

while paths:
    path = paths.pop()
    row, col = path[-1]
    if (row, col) == end:
        if longest < len(path):
            longest = len(path)
    for dr, dc in directions.keys():
        nr = row + dr
        nc = col + dc
        if (nr, nc) in grid and (nr, nc) not in path:
            if grid[(nr, nc)] == '.' or grid[(nr, nc)] == directions[(dr, dc)]:
                paths.append(path + [(nr, nc)])


print(f'⭐ Part 1: {longest}, run time: {int((time.time() - start_time) * 1000)}ms')
