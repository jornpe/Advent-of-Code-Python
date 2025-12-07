from collections import defaultdict
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read().split('\n')

timelines = {col: 1 for col, c in enumerate(input[0]) if c == 'S'}
splitters = set((row, col) for row, line in enumerate(input) for col, c in enumerate(line) if c == '^')

for row in range(len(input)):
    next_timelines = defaultdict(int)
    for col, n  in timelines.items():
        if (row+1, col) in splitters:
            next_timelines[col-1] += n
            next_timelines[col+1] += n
        else:
            next_timelines[col] += n
    timelines = next_timelines

answer = sum(n for n in timelines.values())
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
