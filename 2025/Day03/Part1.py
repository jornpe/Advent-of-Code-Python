from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    banks = [[int(x) for x in line] for line in f.read().split('\n')]

answer = 0

for bank in banks:
    maxTen = max(bank[:-1])
    maxTenI = bank.index(maxTen)
    maxSingle = max(bank[maxTenI + 1:])
    answer += maxSingle + 10 * maxTen

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
