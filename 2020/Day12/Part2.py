from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    actions = [(line[0], int(line[1::])) for line in f.read().split('\n')]

pos = [0, 0]
wp = [1, 10]


def rotate_wp(wp: list, rotation: int) -> list:
    for _ in range(int(rotation / 90)):
        wp = [-wp[1], wp[0]]
    return wp


for act, value in actions:
    match act:
        case 'N': wp[0] += value
        case 'S': wp[0] -= value
        case 'E': wp[1] += value
        case 'W': wp[1] -= value
        case 'L': wp = rotate_wp(wp, 360 - value)
        case 'R': wp = rotate_wp(wp, value)
        case 'F': pos = [pos[0] + wp[0] * value, pos[1] + wp[1] * value]

answer = abs(pos[0]) + abs(pos[1])
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
