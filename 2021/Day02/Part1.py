with open("input.txt") as f:
    input = [(cmd, int(arg)) for cmd, arg in [line.split(' ') for line in f]]

forward = 0
up = 0
down = 0

for move in input:
    if move[0].startswith('forward'):   forward += move[1]
    if move[0].startswith('up'):        up += move[1]
    if move[0].startswith('down'):      down += move[1]

print(forward * (down - up))