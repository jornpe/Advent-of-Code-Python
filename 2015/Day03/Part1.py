with open("input.txt") as f:
    directions = list(f.read())

visited = set()
position = [0, 0]
visited.add((position[0], position[1]))
for d in directions:
    match d:
        case '^': position[0] += 1
        case 'v': position[0] -= 1
        case '>': position[1] += 1
        case '<': position[1] -= 1
    visited.add((position[0], position[1]))

print(f'⭐ Part 1: {len(visited)}')
