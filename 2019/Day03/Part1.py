import re

with open("input.txt") as f:
    wires = [line for line in f.read().split('\n')]


def get_positions(wire: str) -> set:
    path = set()
    p = [0, 0]
    for dir, amount in re.findall(r'([\w])(\d+)', wire):
        amount = int(amount)
        for _ in range(amount):
            match dir:
                case 'U': p[0] += 1
                case 'R': p[1] += 1
                case 'D': p[0] -= 1
                case 'L': p[1] -= 1
            path.add((p[0], p[1]))
    return path


intersections = get_positions(wires[0]) & get_positions(wires[1])

answer = 100000
for intersect in intersections:
    if abs(intersect[0]) + abs(intersect[1]) < answer:
        answer = abs(intersect[0]) + abs(intersect[1])

print(f'⭐ Part 1: {answer}')
