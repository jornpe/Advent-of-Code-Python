with open("input.txt") as f:
    movement = [i.strip() for i in f]

visited = set()
headrow = headcol = 0
tailrow = tailcol = 0

for move in movement:
    dir, steps = move.split()
    steps = int(steps)

    for step in range(steps):
        match dir:
            case 'U':
                headrow += 1
            case 'D':
                headrow -= 1
            case 'R':
                headcol += 1
            case 'L':
                headcol -= 1

        offsetRow = headrow - tailrow
        offsetCol = headcol - tailcol

        if (offsetRow > 1 and offsetCol == 1) or (offsetRow == 1 and offsetCol > 1):
            tailrow += 1
            tailcol += 1
        elif (offsetRow < -1 and offsetCol == 1) or (offsetRow == -1 and offsetCol > 1):
            tailrow -= 1
            tailcol += 1
        elif (offsetRow < -1 and offsetCol == -1) or (offsetRow == -1 and offsetCol < -1):
            tailrow -= 1
            tailcol -= 1
        elif (offsetRow > 1 and offsetCol == -1) or (offsetRow == 1 and offsetCol < -1):
            tailrow += 1
            tailcol -= 1
        elif offsetRow > 1:
            tailrow += 1
        elif offsetRow < -1:
            tailrow -= 1
        elif offsetCol > 1:
            tailcol += 1
        elif offsetCol < -1:
            tailcol -= 1

        visited.add(f'{tailrow},{tailcol}')

print(len(visited))




