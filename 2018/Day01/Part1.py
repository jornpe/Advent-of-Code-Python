import os.path
from pathlib import Path

with open(Path(__file__).with_name('input.txt')) as f:
    sum = sum([int(x) for x in f])


print(f'⭐ Part 1: {sum}')