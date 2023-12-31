from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line.split() for line in f.read().splitlines()]

commands = [(cmd, int(v)) for cmd, v in lines]

accumulator = 0
visited = []
index = 0
while True:
    cmd, value = commands[index]
    if index in visited:
        break
    visited.append(index)
    match cmd:
        case 'acc':
            accumulator += value
            index += 1
        case 'jmp':
            index += value
        case 'nop':
            index += 1

answer = accumulator
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
