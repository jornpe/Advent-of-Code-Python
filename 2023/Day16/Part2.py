from pathlib import Path
from joblib import Parallel, delayed
import time

start_time = time.time()

with open(Path(__file__).with_name('input.txt')) as f:
    grid = [list(line) for line in f.read().splitlines()]


def beam_beams(startpos: tuple) -> int:
    beams = [startpos]
    visited = set()

    while beams:
        pos = beams.pop(0)
        if pos in visited:
            continue

        row, col, dir = pos
        if col < 0 or col >= len(grid[0]) or row < 0 or row >= len(grid):
            continue

        match grid[row][col]:
            case '.' if dir in 'U': beams.append((row - 1, col, dir))
            case '.' if dir in 'R': beams.append((row, col + 1, dir))
            case '.' if dir in 'D': beams.append((row + 1, col, dir))
            case '.' if dir in 'L': beams.append((row, col - 1, dir))

            case '-' if dir in 'UD': beams.extend([(row, col + 1, 'R'), (row, col - 1, 'L')])
            case '-' if dir in 'R': beams.append((row, col + 1, dir))
            case '-' if dir in 'L': beams.append((row, col - 1, dir))

            case '|' if dir in 'U': beams.append((row - 1, col, dir))
            case '|' if dir in 'D': beams.append((row + 1, col, dir))
            case '|' if dir in 'RL': beams.extend([(row - 1, col, 'U'), (row + 1, col, 'D')])

            case '\\' if dir in 'U': beams.append((row, col - 1, 'L'))
            case '\\' if dir in 'R': beams.append((row + 1, col, 'D'))
            case '\\' if dir in 'D': beams.append((row, col + 1, 'R'))
            case '\\' if dir in 'L': beams.append((row - 1, col, 'U'))

            case '/' if dir in 'U': beams.append((row, col + 1, 'R'))
            case '/' if dir in 'R': beams.append((row - 1, col, 'U'))
            case '/' if dir in 'D': beams.append((row, col - 1, 'L'))
            case '/' if dir in 'L': beams.append((row + 1, col, 'D'))

        visited.add((row, col, dir))

    return len(set(((r, c) for r, c, _ in visited)))


startpositions = []

for row, dir in zip([0, len(grid) - 1], ['D', 'U']):
    for col in range(len(grid[0])):
        startpositions.append((row, col, dir))

for col, dir in zip([0, len(grid[0]) - 1], ['R', 'L']):
    for row in range(len(grid)):
        startpositions.append((row, col, dir))


configurations = Parallel(n_jobs=8)(delayed(beam_beams)(x) for x in startpositions)

answer = max(configurations)
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')

