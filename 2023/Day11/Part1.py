from pathlib import Path
from itertools import combinations

with open(Path(__file__).with_name('input.txt')) as f:
    space = [list(line) for line in f.read().split('\n')]


def expand_space(grid: list) -> list:
    expandedspace = []
    for row in grid:
        if '#' in row:
            expandedspace.append(row)
        else:
            expandedspace.append(row)
            expandedspace.append(row)
    return expandedspace


space = expand_space(space)
space = expand_space(list(zip(*space[::-1])))

galaxies = []

for row, line in enumerate(space):
    for col, char in enumerate(line):
        if char == '#':
            galaxies.append((row, col))

answer = 0

combinations = combinations(galaxies, 2)

for g1, g2 in combinations:
    answer += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])

print(f'⭐ Part 1: {answer}')
