from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().splitlines()]

rocks = []
rollingrocks = []

for row, line in enumerate(lines):
    for col, char in enumerate(list(line)):
        if char == '#':
            rocks.append((row, col))
        if char == 'O':
            rollingrocks.append((row, col))

steadyrocks = set()

while rollingrocks:
    (row, col) = rollingrocks.pop(0)
    if (row - 1, col) in rocks or (row - 1, col) in rollingrocks or (row - 1, col) in steadyrocks or row == 0:
        steadyrocks.add((row, col))
    else:
        rollingrocks.append((row - 1, col))

answer = sum(len(lines) - row for row, col in steadyrocks)


print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
