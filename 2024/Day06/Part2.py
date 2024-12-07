from pathlib import Path
import time
import copy

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    grid = [list(line) for line in f.read().split('\n')]

startpos = ()

for row, line in enumerate(grid):
    for col, _ in enumerate(line):
        if grid[row][col] == '^':
            startpos = (row, col)


def getoriginalpath(pos: tuple, testgrid: list) -> set:
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curdir = 0
    visited = set()
    visited.add(pos)
    while True:
        np = (pos[0] + dir[curdir][0], pos[1] + dir[curdir][1])
        if np[0] < 0 or np[0] > len(testgrid) - 1 or np[1] < 0 or np[1] > len(testgrid[0]) - 1:
            return visited
        elif testgrid[np[0]][np[1]] == '#':
            curdir = (curdir + 1) % 4
        else:
            pos = np
            visited.add(np)


def endInCircle(pos: tuple, testgrid: list) -> int:
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curdir = 0
    visited = set(pos)
    while True:
        np = (pos[0] + dir[curdir][0], pos[1] + dir[curdir][1])
        if (np, curdir) in visited:
            return 1
        elif np[0] < 0 or np[0] > len(testgrid) - 1 or np[1] < 0 or np[1] > len(testgrid[0]) - 1:
            return 0
        elif testgrid[np[0]][np[1]] == '#':
            curdir = (curdir + 1) % 4
        else:
            pos = np
            visited.add((np, curdir))


numberofcircles = 0
for row, col in getoriginalpath(startpos, grid):
    newgrid = copy.deepcopy(grid)
    newgrid[row][col] = '#'
    numberofcircles += endInCircle(startpos, newgrid)

answer = numberofcircles
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
