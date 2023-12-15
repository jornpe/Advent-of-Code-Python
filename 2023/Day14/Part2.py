from pathlib import Path
import numpy as np

with open(Path(__file__).with_name('input.txt')) as f:
    map = [[c for c in list(line)] for line in f.read().splitlines()]


def lets_roll(map: list) -> list:
    continuerolling = True
    while continuerolling:
        continuerolling = False
        for row, line in enumerate(map):
            if row == 0:
                continue
            for col, char in enumerate(line):
                if char == 'O':
                    if map[row - 1][col] == '.':
                        map[row - 1][col] = char
                        map[row][col] = '.'
                        continuerolling = True
    return map


def get_answer(map: list) -> int:
    map = np.array(map)
    cache = {}
    loop = 0
    cycles = 1000000000
    times = 0
    while loop < cycles:
        loop += 1
        times += 1
        for _ in range(4):
            map = lets_roll(map)
            map = np.rot90(map, 3)

        key = tuple(map.flatten())
        if key in cache:
            number = cache[key]
            cycles = (cycles - loop) % (loop - number)
            loop = 0
            cache.clear()
        cache[key] = loop

    return sum(sum([len(map) - row for col, char in enumerate(line) if char == 'O']) for row, line in enumerate(map))


answer = get_answer(map)
print(f'⭐⭐ Part 2: {answer}')
