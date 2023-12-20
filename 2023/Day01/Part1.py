from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]
answer = 0

for line in lines:
    digits = [s for s in list(line) if s.isdigit()]
    answer += int(digits[0] + digits[-1])

print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
