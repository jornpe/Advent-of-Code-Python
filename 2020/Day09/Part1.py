from itertools import combinations
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    numbers = [int(n) for n in f.read().split('\n')]


def get_no_match(numbers: list, preamble: int) -> int:
    for idx, number in enumerate(numbers[preamble::], preamble):
        for n1, n2 in combinations(numbers[idx - preamble:idx], 2):
            if n1 + n2 == number:
                break
        else:
            return number


answer = get_no_match(numbers, 25)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
