from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    inputs = f.read().split('\n\n')

ranges = sorted([(int(range.split('-')[0]), int(range.split('-')[1])) for range in inputs[0].split('\n')])

answer = 0
for id in inputs[1].split('\n'):
    id = int(id)
    answer += 1 if any(min_r <= id <= max_r for min_r, max_r in ranges) else 0

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
