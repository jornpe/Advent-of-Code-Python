from collections import Counter
from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

pos = ()
grid = {}
gridsize = (len(lines), len(lines[0]))
pathlength = 0

for row, r in enumerate(lines):
    for col, c in enumerate(r):
        if c == 'S':
            pos = (row, col)
        grid[(row, col)] = c
        if c != '#':
            pathlength += 1


def getPath(p: tuple, gridsize: tuple, grid: dict) -> dict:
    path = {}
    idx = 1
    path[p] = pathlength - idx
    while True:
        idx += 1
        if grid[p] == 'E':
            return path
        for n in [(p[0] + x, p[1] + y) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
            if n in path or grid[n] == '#':
                continue
            if 0 < n[0] < gridsize[0] and 0 < n[1] < gridsize[1]:
                path[n] = pathlength - idx
                p = n


def getcheats(p: tuple, grid: dict, gridsize: tuple) -> list:
    cheats = []
    queue = [(p)]
    idx = 0
    visited = set()
    while idx < 20 and queue:
        idx += 1
        for _ in range(len(queue)):
            p = queue.pop(0)
            for n in [(p[0] + x, p[1] + y) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
                if 0 < n[0] < gridsize[0] - 1 and 0 < n[1] < gridsize[1] - 1:
                    if n in visited:
                        continue
                    if grid[n] != '#':
                        cheats.append((idx, n))
                    visited.add(n)
                    queue.append(n)
    return cheats


def getpathwithcheat(p: tuple, grid: dict, gridsize: tuple, path: dict) -> list:
    lengths = []
    cheats = getcheats(p, grid, gridsize)
    for v, n in cheats:
        if path[p] > path[n]:
            lengths.append(len(path) - path[p] + v + path[n])
    return lengths


path = getPath(pos, gridsize, grid)
cheats = []
for p in path:
    cheats += getpathwithcheat(p, grid, gridsize, path)

answer = sum(1 for v in cheats if v <= len(path) - 100)

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
