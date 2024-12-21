from pathlib import Path
import time

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


def getPath(p: tuple, grid: list) -> list:
    path = [pos]
    while True:
        if grid[p[0]][p[1]] == 'E':
            return path
        for n in [(p[0] + x, p[1] + y) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
            if n in path or grid[n[0]][n[1]] == '#':
                continue
            if 0 < n[0] < len(grid) and 0 < n[1] < len(grid[0]):
                path.append(n)
                p = n


def getpathwithcheat(path: list, c: tuple) -> list:
    lengths = []
    for n1r, n1c, n2r, n2c  in [(c[0] + x, c[1] + y, c[0] + x + x, c[1] + y + y) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
        if any(x < 0 for x in (n1r, n1c, n2r, n2c)) or any(x > len(grid) - 1 for x in (n1r, n1c, n2r, n2c)):
            continue
        if grid[n1r][n1c] == '#' and grid[n2r][n2c] in ['.', 'E']:
            lengths.append(len(path[:path.index(c) + 1] + path[path.index((n2r, n2c)):]) + 1)
    return lengths


path = getPath(pos, grid)
cheats = []
for p in path:
    cheats += getpathwithcheat(path, p)

answer = sum(1 for v in cheats if v <= len(path) - 100)

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
