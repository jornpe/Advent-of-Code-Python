from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    adapters = [int(n) for n in f.read().split('\n')]


def get_arrangements(value: int, cache: dict, adapters: list) -> int:
    if (value, *adapters) in cache:
        return cache[(value, *adapters)]
    nads = [a for a in adapters if a <= value + 3]
    if not nads:
        return 1
    arrangements = 0
    for nad in nads:
        arrangements += get_arrangements(nad, cache, [a for a in adapters if a > nad])
    cache[(value, *adapters)] = arrangements
    return arrangements


answer = get_arrangements(0, {}, adapters)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
