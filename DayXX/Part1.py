from pathlib import Path

with open(Path(__file__).with_name('test.txt')) as f:
    input = [line for line in f.read().split('\n')]

answer = 0
print(f'⭐ Part 1: {answer}')
