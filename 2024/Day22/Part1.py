from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [int(line) for line in f.read().split('\n')]


def calculatesecretnumber(number: int) -> int:
    for _ in range(2000):
        number = ((number * 64) ^ number) % 16777216
        number = (int(number / 32) ^ number) % 16777216
        number = ((number * 2048) ^ number) % 16777216
    return number


answer = sum(calculatesecretnumber(n) for n in lines)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
