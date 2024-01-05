from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

seats = {(r, c): v for r, line in enumerate(lines) for c, v in enumerate(line) if v != '.'}


def roll_seats(seats: dict) -> int:
    index = 0
    while True:
        index += 1
        changed = False
        updatedseats = {}
        for (r, c), value in list(seats.items()):
            adjocc = sum([1 for nr, nc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                                 if (r + nr, c + nc) in seats and seats[(r + nr, c + nc)] == '#'])
            if value == 'L' and adjocc == 0:
                nvalue = '#'
            elif value == '#' and adjocc >= 4:
                nvalue = 'L'
            else:
                nvalue = value

            if nvalue != value:
                changed = True
            updatedseats[(r, c)] = nvalue
        if not changed:
            return sum(1 for v in seats.values() if v == '#')
        seats = updatedseats


answer = roll_seats(seats)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
