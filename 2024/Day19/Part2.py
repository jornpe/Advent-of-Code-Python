from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = [input for input in f.read().split('\n\n')]

towels = [t.strip() for t in input[0].split(',')]
designs = input[1].split('\n')


def getpossibilities(design: str, seltowel: str, cache: dict) -> int:
    if seltowel == design:
        return 1
    if (design, seltowel) in cache:
        return cache[(design, seltowel)]

    dr = design.removeprefix(seltowel)
    p = 0
    for nt in [seltowel + t for t in towels if dr.startswith(t)]:
        p += getpossibilities(design, nt, cache)
        cache[(design, seltowel)] = p
    return p


answer = sum(getpossibilities(d, '', {}) for d in designs)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
