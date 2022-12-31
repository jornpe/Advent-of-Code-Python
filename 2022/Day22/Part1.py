import re

with open("input.txt") as f:
    input, command = f.read().split('\n\n')
    map = [list(l) for l in input.split('\n')]
    path = re.findall(r'\d+|[A-Za-z]', command)


position = (0, map[0].index('.'))
direction = 'R'

for p in path:
    if p.isnumeric():
        for _ in range(int(p)):
            match direction:
                case 'R':
                    row = position[0]
                    if position[1] + 1 < len(map[row]):
                        col = position[1] + 1
                    else:
                        if '#' in map[row]:
                            col = min(map[row].index('.'), map[row].index('#'))
                        else:
                            col = map[row].index('.')
                    new_pos = (row, col)
                case 'L':
                    row = position[0]
                    if position[1] - 1 >= 0 and map[row][position[1] - 1] != ' ':
                        col = position[1] - 1
                    else:
                        col = len(map[row]) - 1
                    new_pos = (row, col)
                case 'D':
                    row = position[0]
                    col = position[1]
                    if row + 1 < len(map) and len(map[row + 1]) > col and map[row + 1][col] in ('.', '#'):
                        row += 1
                    else:
                        for i, r in enumerate(map):
                            if len(r) > col and r[col] in ('.', '#'):
                                row = i
                                break
                    new_pos = (row, col)
                case _:
                    row = position[0]
                    col = position[1]
                    if row - 1 > 0 and len(map[row - 1]) > col and map[row - 1][col] in ('.', '#'):
                        row -= 1
                    else:
                        for i in range(len(map) - 1, -1, -1):
                            if len(map[i]) > col and map[i][col] in ('.', '#'):
                                row = i
                                break
                    new_pos = (row, col)

            if map[new_pos[0]][new_pos[1]] != '#':
                position = new_pos
            else:
                break

    else:
        match p:
            case 'R' if direction == 'U': direction = 'R'
            case 'R' if direction == 'R': direction = 'D'
            case 'R' if direction == 'D': direction = 'L'
            case 'R' if direction == 'L': direction = 'U'
            case 'L' if direction == 'U': direction = 'L'
            case 'L' if direction == 'L': direction = 'D'
            case 'L' if direction == 'D': direction = 'R'
            case 'L' if direction == 'R': direction = 'U'


match direction:
    case 'R': facing_value = 0
    case 'D': facing_value = 1
    case 'L': facing_value = 2
    case _: facing_value = 3

print((1000 * (position[0] + 1)) + (4 * (position[1] + 1)) + facing_value)

# 104056 is too high
