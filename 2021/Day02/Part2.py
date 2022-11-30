with open("input.txt") as f:
    input = [(cmd, int(arg)) for cmd, arg in [line.split(' ') for line in f]]


forward = 0
depth = 0
aim = 0

for move in input:
    if move[0].startswith('forward'):   
        forward += move[1]
        depth += aim * move[1]
    if move[0].startswith('up'): aim -= move[1]
    if move[0].startswith('down'): aim += move[1]

print(depth * forward)