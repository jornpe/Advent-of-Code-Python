from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    start = [int(i) for i in f.read().split(',')]


def game(start_seq: list, turns: int) -> int:
    numbers = {n: i for i, n in enumerate(start[:-1], 1)}
    spoken_number = start_seq[-1]
    turn = len(start_seq)
    while True:

        if spoken_number not in numbers:
            numbers[spoken_number] = turn
            spoken_number = 0
        else:
            i = numbers[spoken_number]
            numbers[spoken_number] = turn
            spoken_number = turn - i

        turn += 1

        if turn == turns:
            return spoken_number


answer1 = game(start, 2020)
answer2 = game(start, 30000000)

print(f'⭐ Part 1: {answer1}, run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer2}, run time: {int((time.time() - start_time) * 1000)}ms')
