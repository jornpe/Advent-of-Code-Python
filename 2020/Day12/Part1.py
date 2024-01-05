from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    actions = [(line[0], int(line[1::])) for line in f.read().split('\n')]

pos = [0, 0]
dir = 90
dirs = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}

for act, value in actions:
    match act:
        case 'N': pos[0] += value
        case 'S': pos[0] -= value
        case 'E': pos[1] += value
        case 'W': pos[1] -= value
        case 'L': dir = (dir - value) % 360
        case 'R': dir = (dir + value) % 360
        case 'F': pos = [pos[0] + dirs[dir][0] * value, pos[1] + dirs[dir][1] * value]

answer = abs(pos[0]) + abs(pos[1])
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
