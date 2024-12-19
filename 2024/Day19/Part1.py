from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = [input for input in f.read().split('\n\n')]

towels = [t.strip() for t in input[0].split(',')]
designs = input[1].split('\n')


def ispossible(design) -> int:
    queue = [t for t in towels if design.startswith(t)]
    while queue:
        p = queue.pop()
        if p == design:
            return 1
        dr = design.removeprefix(p)
        queue += [p + t for t in towels if dr.startswith(t)]
    return 0


answer = sum(ispossible(d) for d in designs)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
