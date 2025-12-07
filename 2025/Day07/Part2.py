from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read().split('\n')

timelines = {(0, col): 1 for col, c in enumerate(input[0]) if c == 'S'}
splitters = set((row, col) for row, line in enumerate(input) for col, c in enumerate(line) if c == '^')


def update_timelines(pos: tuple, n: int, timelines: dict):
    if pos in timelines:
        timelines[pos] += n
    else:
        timelines[pos] = n


for _ in range(len(input)):
    tl = timelines
    timelines = {}
    for (row, col), n  in tl.items():
        if (row+1, col) in splitters:
            update_timelines((row+1, col-1), n, timelines)
            update_timelines((row+1, col+1), n, timelines)
        else:
            update_timelines((row + 1, col), n, timelines)

answer = sum(n for n in timelines.values())
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
