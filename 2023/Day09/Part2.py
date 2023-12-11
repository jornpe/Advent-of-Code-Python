from itertools import pairwise
from pathlib import Path

with open(Path(__file__).with_name('input.txt')) as f:
    histories = [line for line in f.read().split('\n')]

answer = 0

for history in histories:
    numbers = [list(map(int, history.split()))]

    while set(numbers[-1]) != {0}:
        nextnumbers = []
        for n1, n2 in pairwise(numbers[-1]):
            nextnumbers.append(n2 - n1)
        numbers.append(nextnumbers)

    extrapolate = 0
    for idx, _ in enumerate(numbers[::-1]):
        extrapolate = numbers[-idx - 1][0] - extrapolate

    answer += extrapolate



print(f'⭐⭐ Part 2: {answer}')
