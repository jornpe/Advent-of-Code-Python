from pathlib import Path
import time
from itertools import combinations

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    grid = [list(line) for line in f.read().split('\n')]

antennatypes = {}
antinodes = set()

for row, line in enumerate(grid):
    for col, c in enumerate(line):
        if c != '.':
            if c in antennatypes:
                antennatypes[c] += [(row, col)]
            else:
                antennatypes[c] = [(row, col)]

for at in antennatypes.values():
    for a1, a2 in combinations(at, 2):
        dr = a1[0] - a2[0]
        dc = a1[1] - a2[1]

        insidebounce = True
        nr, nc = a1[0], a1[1]
        while insidebounce:
            nr, nc = nr + dr, nc + dc
            insidebounce = 0 <= nr <= len(grid) - 1 and 0 <= nc <= len(grid[0]) - 1
            if insidebounce:
                antinodes.add((nr, nc))
        insidebounce = True
        nr, nc = a2[0], a2[1]
        while insidebounce:
            nr, nc = nr - dr, nc - dc
            insidebounce = 0 <= nr <= len(grid) - 1 and 0 <= nc <= len(grid[0]) - 1
            if insidebounce:
                antinodes.add((nr, nc))

for antennas in antennatypes.values():
    if len(antennas) > 1:
        for a in antennas:
            antinodes.add(a)


answer = len(antinodes)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
