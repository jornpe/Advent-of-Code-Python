from pathlib import Path
import time
import sys

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = [[int(x), int(y), int(z)] for x, y, z in [line.split() for line in f.read().split('\n')]]

isvalid = 0
for row in range(0, len(input), 3):
    for col in range(3):
        if input[row][col] + input[row + 1][col] > input[row + 2][col] and input[row + 1][col] + input[row + 2][col] > input[row][col] and input[row + 2][col] + input[row][col] > input[row + 1][col]:
            isvalid += 1


answer = isvalid
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
