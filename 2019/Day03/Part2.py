import re

with open("input.txt") as f:
    wires = [line for line in f.read().split('\n')]


def get_positions(wire: str) -> dict:
    path = {}
    p = [0, 0]
    steps = 0
    for dir, amount in re.findall(r'(\w)(\d+)', wire):
        amount = int(amount)
        for _ in range(amount):
            steps += 1
            match dir:
                case 'U': p[0] += 1
                case 'R': p[1] += 1
                case 'D': p[0] -= 1
                case 'L': p[1] -= 1
            path[(p[0], p[1])] = steps
    return path


wire1 = get_positions(wires[0])
wire2 = get_positions(wires[1])

answer = 100000
for intersection in set(wire1) & set(wire2):
    if wire1[intersection] + wire2[intersection] < answer:
        answer = wire1[intersection] + wire2[intersection]

print(f'⭐⭐ Part 2: {answer}')
