from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read().split('\n')

beams = set((0, col) for col, c in enumerate(input[0]) if c == 'S')
splitters = set((row, col) for row, line in enumerate(input) for col, c in enumerate(line) if c == '^')
splits = 0

for _ in range(len(input)):
    beam_roll = beams
    beams = set()
    for row, col in beam_roll:
        if (row+1, col) in splitters:
            beams.add((row+1, col-1))
            beams.add((row+1, col+1))
            splits += 1
        else:
            beams.add((row+1, col))

answer = splits
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
