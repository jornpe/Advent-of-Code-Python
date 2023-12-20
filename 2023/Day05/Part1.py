from pathlib import Path
import re
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    inputs = [line for line in f.read().split('\n\n')]

seeds = list(map(int, re.findall(r'\d+', inputs[0])))
maps = [[list(map(int, re.findall(r'\d+', m_numbers))) for m_numbers in m.split('\n')[1:]] for m in inputs[1:]]


def get_location(number: int) -> int:
    for m in maps:
        for rangechange in m:
            dest_start, source_start, length = rangechange
            if source_start <= number < source_start + length:
                number = number + (dest_start - source_start)
                break
    return number


locations = []
for seed in seeds:
    locations.append(get_location(seed))

answer = min(locations)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
