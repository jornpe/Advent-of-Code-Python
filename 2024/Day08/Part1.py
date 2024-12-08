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
        antinodes.add((a1[0] + dr, a1[1] + dc))
        antinodes.add((a2[0] - dr, a2[1] - dc))

answer = sum(1 for r, c in antinodes if 0 <= r <= len(grid) - 1 and 0 <= c <= len(grid[0]) - 1)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
