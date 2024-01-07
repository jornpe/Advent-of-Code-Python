from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

start = int(lines[0])
busses = [int(b) for b in lines[1].split(',') if b.isdigit()]
times = []

for buss in busses:
    times.append(((int(start / buss) + 1) * buss, buss))

buss = min(times, key=lambda b: b[0])
answer = (buss[0] - start) * buss[1]
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
