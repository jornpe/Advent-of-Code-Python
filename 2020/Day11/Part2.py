from collections import defaultdict
from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

seats = {(r, c): v for r, line in enumerate(lines) for c, v in enumerate(line) if v != '.'}


def get_occupied_seat_in_dir(seats: dict,  row: int, col: int, rdir: int, cdir: int) -> bool:
    while 0 <= row < len(lines) and 0 <= col < len(lines[0]):
        row += rdir
        col += cdir
        if (row, col) in seats and seats[row, col] == '#':
            return True
        if (row, col) in seats and seats[row, col] == 'L':
            return False
    return False


def roll_seats(seats: dict) -> int:
    index = 0
    while True:
        index += 1
        changed = False
        updatedseats = {}
        for (r, c), value in list(seats.items()):
            adjocc = sum([get_occupied_seat_in_dir(seats, r, c, nr, nc)
                          for nr, nc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]])
            if value == 'L' and adjocc == 0:
                nvalue = '#'
            elif value == '#' and adjocc >= 5:
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
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
