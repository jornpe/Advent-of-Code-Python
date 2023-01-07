with open("input.txt") as f:
    directions = list(f.read())

visited = set()
santa_position = [0, 0]
robo_position = [0, 0]
visited.add(tuple(santa_position))


def get_position(direction: str, position: list) -> list:
    match direction:
        case '^': position[0] += 1
        case 'v': position[0] -= 1
        case '>': position[1] += 1
        case '<': position[1] -= 1
    return position


for i, d in enumerate(directions):
    if i % 2 == 0:
        santa_position = get_position(d, santa_position)
        visited.add(tuple(santa_position))
    else:
        robo_position = get_position(d, robo_position)
        visited.add(tuple(robo_position))

print(f'⭐ Part 2: {len(visited)}')
