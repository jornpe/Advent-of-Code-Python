from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    grid = [list(line) for line in f.read().split('\n')]

pos = ()
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curdir = 0
visited = set()

for row, line in enumerate(grid):
    for col, _ in enumerate(line):
        if grid[row][col] == '^':
            pos = (row, col)
            visited.add(pos)

keepgoing = True
while keepgoing:
    np = (pos[0] + dir[curdir][0], pos[1] + dir[curdir][1])
    if np[0] < 0 or np[0] > len(grid) - 1 or np[1] < 0 or np[1] > len(grid[0]) - 1:
        keepgoing = False
        break
    elif grid[np[0]][np[1]] == '#':
        curdir = (curdir + 1) % 4
    else:
        pos = np
        visited.add(pos)



answer = len(visited)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
