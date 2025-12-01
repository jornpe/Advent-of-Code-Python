from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rotations = [(line[0], int(line[1:])) for line in f.read().split('\n')]

position = 50
answer = 0

for dir, rot in rotations:
    position = (position + rot) if dir == 'R' else (position - rot)
    position %= 100
    if position == 0:
        answer += 1

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
