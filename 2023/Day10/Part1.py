from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rows = [line for line in f.read().split('\n')]


def get_neigbours(row, col, _):
    return [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]


grid = {}
posdir = ()

for row, line in enumerate(rows[::-1]):
    for col, char in enumerate(list(line)):
        if char == 'S':
            posdir = (row, col, 'U')
        if char != '.':
            grid[(row, col)] = char

up, right, down, left = get_neigbours(*posdir)
if up in grid and grid[up] in ['|', 'F', '7']:
    posdir = (posdir[0], posdir[1], 'U')
elif right in grid and grid[right] in ['-', 'J', '7']:
    posdir = (posdir[0], posdir[1], 'R')
elif down in grid and grid[down] in ['|', 'L', 'J']:
    posdir = (posdir[0], posdir[1], 'D')
elif left in grid and grid[left] in ['-', 'L', 'F']:
    posdir = (posdir[0], posdir[1], 'L')

steps = 0
loopclosed = False
while not loopclosed:
    up, right, down, left = get_neigbours(*posdir)
    match posdir[-1]:
        case 'U' if up in grid and grid[up] == '|': posdir = (*up, 'U')
        case 'U' if up in grid and grid[up] == 'F': posdir = (*up, 'R')
        case 'U' if up in grid and grid[up] == '7': posdir = (*up, 'L')
        case 'U' if up in grid and grid[up] == 'S': loopclosed = True
        case 'R' if right in grid and grid[right] == '-': posdir = (*right, 'R')
        case 'R' if right in grid and grid[right] == 'J': posdir = (*right, 'U')
        case 'R' if right in grid and grid[right] == '7': posdir = (*right, 'D')
        case 'R' if right in grid and grid[right] == 'S': loopclosed = True
        case 'D' if down in grid and grid[down] == '|': posdir = (*down, 'D')
        case 'D' if down in grid and grid[down] == 'L': posdir = (*down, 'R')
        case 'D' if down in grid and grid[down] == 'J': posdir = (*down, 'L')
        case 'D' if down in grid and grid[down] == 'S': loopclosed = True
        case 'L' if left in grid and grid[left] == '-': posdir = (*left, 'L')
        case 'L' if left in grid and grid[left] == 'L': posdir = (*left, 'U')
        case 'L' if left in grid and grid[left] == 'F': posdir = (*left, 'D')
        case 'L' if left in grid and grid[left] == 'S': loopclosed = True

    steps += 1


answer = int(steps / 2)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
