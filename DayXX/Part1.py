from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('test.txt')) as f:
    lines = [line for line in f.read().split('\n')]

answer = 0
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
