with open("input.txt") as f:
    input = [ l.rstrip().split(' ') for l in f]

forward = 0
depth = 0
aim = 0

for move in input:
    if move[0].startswith('forward'):   
        forward += int(move[1])
        depth += aim * int(move[1])
    if move[0].startswith('up'): aim -= int(move[1])
    if move[0].startswith('down'): aim += int(move[1])

print(depth * forward)