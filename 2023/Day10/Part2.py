from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rows = [line for line in f.read().split('\n')]


def get_neigbours(pos: tuple):
    row = pos[0]
    col = pos[1]
    return [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]


grid = {}
posdir = ()

for row, line in enumerate(rows):
    for col, char in enumerate(list(line)):
        if char == 'S':
            posdir = (row, col, 'U')
        if char != '.':
            grid[(row, col)] = char

up, right, down, left = get_neigbours(posdir)
if up in grid and grid[up] in ['|', 'F', '7']:
    posdir = (posdir[0], posdir[1], 'U')
elif right in grid and grid[right] in ['-', 'J', '7']:
    posdir = (posdir[0], posdir[1], 'R')
elif down in grid and grid[down] in ['|', 'L', 'J']:
    posdir = (posdir[0], posdir[1], 'D')
elif left in grid and grid[left] in ['-', 'L', 'F']:
    posdir = (posdir[0], posdir[1], 'L')

route = {(posdir[0], posdir[1]): 'S'}
loopclosed = False
while not loopclosed:
    up, right, down, left = get_neigbours(posdir)
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

    route[(posdir[0], posdir[1])] = grid[(posdir[0], posdir[1])]



updatedrows = []
for rix, row in enumerate(rows):
    line = ''
    for cix, col in enumerate(list(row)):
        line += '.' if (rix, cix) not in route else route[(rix, cix)]
    updatedrows.append(line)

expanded = []

for line in updatedrows:
    newline = ''
    addedline = ''
    for char in list(line):
        match char:
            case '.': newline += '..'
            case '|': newline += '|.'
            case '-': newline += '--'
            case 'L': newline += 'L-'
            case 'J': newline += 'J.'
            case '7': newline += '7.'
            case 'F': newline += 'F-'
            case 'S': newline += '--'

    for char in list(newline):
        match char:
            case '.': addedline += '.'
            case '|': addedline += '|'
            case '-': addedline += '.'
            case 'L': addedline += '.'
            case 'J': addedline += '.'
            case '7': addedline += '|'
            case 'F': addedline += '|'
            case 'S': addedline += '.'

    expanded.append(newline)
    expanded.append(addedline)

dots = []
trapped = []

for row, line in enumerate(expanded):
    for col, char in enumerate(list(line)):
        if char == '.':
            dots.append((row, col))


while dots:
    canescape = False
    queue = [dots.pop(0)]
    visited = []

    while queue:
        dot = queue.pop(0)
        visited.append(dot)
        neigbours = [n for n in get_neigbours(dot) if n in dots and n not in visited]

        for row, col in neigbours:
            if row == 0 or row == len(expanded) - 1 or col == 0 or col == len(expanded[0]) - 1:
                canescape = True
            queue.append((row, col))
            dots.remove((row, col))

    if not canescape:
        trapped.extend(visited)

answer = 0
for row in range(0, len(expanded), 2):
    for col in range(0, len(list(expanded[0])), 2):
        if (row, col) in trapped and (row, col + 1) in trapped:
            answer += 1

print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
