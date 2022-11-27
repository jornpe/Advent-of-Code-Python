with open("input.txt") as f:
    input = [ l.rstrip().split(' ') for l in f]

forward = 0
up = 0
down = 0

for move in input:
    if move[0].startswith('forward'):   forward += int(move[1])
    if move[0].startswith('up'):        up += int(move[1])
    if move[0].startswith('down'):      down += int(move[1])

print(forward * (down - up))