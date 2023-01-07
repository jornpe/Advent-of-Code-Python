import re

with open("input.txt") as f:
    input, command = f.read().split('\n\n')
    input = input.split('\n')
    path = re.findall(r'\d+|\w', command)


# creating the cube
cube = []
cube.append([c for c in [i[50:100] for i in input[:50]]])
cube.append([c for c in [i[100:] for i in input[:50]]])
cube.append([c for c in [i[50:] for i in input[50:100]]])
cube.append([c for c in [i[:50] for i in input[100:150]]])
cube.append([c for c in [i[50:] for i in input[100:150]]])
cube.append([i for i in input[150:]])

position = (0, 'R', 1, 49)  # cube face, direction, row, column


def get_cube_face(cur_face: int, dir: str, row: int, col: int) -> tuple:
    match cur_face:
        case 0 if dir == 'U': return 5, 'R', col, row
        case 0 if dir == 'R': return 1, 'R', row, 0
        case 0 if dir == 'D': return 2, 'D', 0, col
        case 0 if dir == 'L': return 3, 'R', 49 - row, 0
        case 1 if dir == 'U': return 5, 'U', col, 49
        case 1 if dir == 'R': return 4, 'L', 49 - row, 49
        case 1 if dir == 'D': return 2, 'L', col, 49
        case 1 if dir == 'L': return 0, 'L', row, 49
        case 2 if dir == 'U': return 0, 'U', 49, col
        case 2 if dir == 'R': return 1, 'U', 49, row
        case 2 if dir == 'D': return 4, 'D', 0, col
        case 2 if dir == 'L': return 3, 'D', 0, row
        case 3 if dir == 'U': return 2, 'R', col, 0
        case 3 if dir == 'R': return 4, 'R', row, 0
        case 3 if dir == 'D': return 5, 'D', 0, col
        case 3 if dir == 'L': return 0, 'R', 49 - col, 0
        case 4 if dir == 'U': return 2, 'U', 49, col
        case 4 if dir == 'R': return 1, 'L', 49 - row, 49
        case 4 if dir == 'D': return 5, 'L', col, 49
        case 4 if dir == 'L': return 3, 'L', row, 49
        case 5 if dir == 'U': return 3, 'U', 49, col
        case 5 if dir == 'R': return 4, 'U', 49, row
        case 5 if dir == 'D': return 1, 'D', 0, col
        case 5 if dir == 'L': return 0, 'D', 0, row


def walk_the_path(pos: tuple, next: str) -> tuple:

    if next.isnumeric():
        next = int(next)
        for _ in range(next):
            face, dir, row, col = pos
            match dir:
                case 'U':
                    if row == 0:
                        face, dir, row, col = get_cube_face(face, dir, row, col)
                    else:
                        row -= 1
                case 'R':
                    if col == 49:
                        face, dir, row, col = get_cube_face(face, dir, row, col)
                    else:
                        col += 1
                case 'D':
                    if row == 49:
                        face, dir, row, col = get_cube_face(face, dir, row, col)
                    else:
                        row += 1
                case 'L':
                    if col == 0:
                        face, dir, row, col = get_cube_face(face, dir, row, col)
                    else:
                        col -= 1

            if cube[face][row][col] == '#':
                return pos
            else:
                pos = (face, dir, row, col)

        return pos

    else:
        face, dir, row, col = pos
        match next:
            case 'R' if dir == 'U': return face, 'R', row, col
            case 'R' if dir == 'R': return face, 'D', row, col
            case 'R' if dir == 'D': return face, 'L', row, col
            case 'R' if dir == 'L': return face, 'U', row, col
            case 'L' if dir == 'U': return face, 'L', row, col
            case 'L' if dir == 'L': return face, 'D', row, col
            case 'L' if dir == 'D': return face, 'R', row, col
            case 'L' if dir == 'R': return face, 'U', row, col


for p in path:
    position = walk_the_path(position, p)

match position[1]:
    case 'R': facing_value = 0
    case 'D': facing_value = 1
    case 'L': facing_value = 2
    case _: facing_value = 3

match position[0]:
    case 0: answer = (1000 * (position[2] + 1)) + (4 * (position[3] + 51)) + facing_value
    case 1: answer = (1000 * (position[2] + 1)) + (4 * (position[3] + 101)) + facing_value
    case 2: answer = (1000 * (position[2] + 51)) + (4 * (position[3] + 51)) + facing_value
    case 3: answer = (1000 * (position[2] + 101)) + (4 * (position[3] + 1)) + facing_value
    case 4: answer = (1000 * (position[2] + 101)) + (4 * (position[3] + 51)) + facing_value
    case _: answer = (1000 * (position[2] + 151)) + (4 * (position[3] + 1)) + facing_value

print(f'⭐⭐ Part 2: {answer}')
