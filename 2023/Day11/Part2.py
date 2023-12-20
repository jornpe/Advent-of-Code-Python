from pathlib import Path
from itertools import combinations
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    space = [list(line) for line in f.read().split('\n')]


def expand_space(grid) -> list:
    ids = []
    for row, line in enumerate(grid):
        if '#' not in line:
            ids.append(row)
    return ids


expanded_rows = set(expand_space(space))
expanded_cols = set(expand_space(list(zip(*space[::-1]))))

galaxies = []


for row, line in enumerate(space):
    for col, char in enumerate(line):
        if char == '#':
            galaxies.append((row, col))

answer = 0
combinations = combinations(galaxies, 2)
multiplier = 1000000

for g1, g2 in combinations:
    rows = set(range(min(g1[0], g2[0]) + 1, max(g1[0], g2[0]) + 1))
    cols = set(range(min(g1[1], g2[1]) + 1, max(g1[1], g2[1]) + 1))

    for r in rows:
        answer += multiplier if r in expanded_rows else 1
    for c in cols:
        answer += multiplier if c in expanded_cols else 1


print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
