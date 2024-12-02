import re
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read()

length = 0

while input:
    if input.startswith('('):
        seq, number, repeats, *_ = re.search(r'(\((\d+)x(\d+)\))', input).groups()
        length += int(number) * int(repeats)
        input = input[int(number) + len(seq):]
    elif '(' in input:
        idx = input.index('(')
        length += idx
        input = input[idx:]
    else:
        length += len(input)
        input = ''

answer = length

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')