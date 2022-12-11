with open("input.txt") as f:
    movement = [i.strip() for i in f]

visited = set()
rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


def move1step(head, tail, isTail):

    offsetRow = head[0] - tail[0]
    offsetCol = head[1] - tail[1]

    if (offsetRow > 1 and offsetCol >= 1) or (offsetRow >= 1 and offsetCol > 1):
        tail[0] += 1
        tail[1] += 1
    elif (offsetRow < -1 and offsetCol >= 1) or (offsetRow <= -1 and offsetCol > 1):
        tail[0] -= 1
        tail[1] += 1
    elif (offsetRow < -1 and offsetCol <= -1) or (offsetRow <= -1 and offsetCol < -1):
        tail[0] -= 1
        tail[1] -= 1
    elif (offsetRow > 1 and offsetCol <= -1) or (offsetRow >= 1 and offsetCol < -1):
        tail[0] += 1
        tail[1] -= 1
    elif offsetRow > 1:
        tail[0] += 1
    elif offsetRow < -1:
        tail[0] -= 1
    elif offsetCol > 1:
        tail[1] += 1
    elif offsetCol < -1:
        tail[1] -= 1

    if isTail:
        visited.add(f'{tail[0]},{tail[1]}')

    return tail


for move in movement:
    dir, steps = move.split()
    steps = int(steps)

    for step in range(steps):
        match dir:
            case 'U':
                rope[0][0] += 1
            case 'D':
                rope[0][0] -= 1
            case 'R':
                rope[0][1] += 1
            case 'L':
                rope[0][1] -= 1

        for knot in range(1, len(rope)):
            isTail = True if knot == len(rope) - 1 else False
            rope[knot] = move1step(rope[knot - 1], rope[knot], isTail)

print(len(visited))
