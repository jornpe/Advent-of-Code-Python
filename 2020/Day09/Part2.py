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


def get_encryption_key(numbers: list, value: int) -> int:
    for start_idx in range(len(numbers)):
        end_idx = start_idx + 1
        while True:
            s = sum(numbers[start_idx:end_idx])
            if s > value:
                break
            if s == value:
                return min(numbers[start_idx:end_idx]) + max(numbers[start_idx:end_idx])
            end_idx += 1


no_match = get_no_match(numbers, 25)
answer = get_encryption_key(numbers, no_match)

print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
