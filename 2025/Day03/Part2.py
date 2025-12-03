from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    banks = [[int(x) for x in line] for line in f.read().split('\n')]


def get_next_digit(bank: list[int], joltage: str) -> int:
    if len(joltage) == 12:
        return int(joltage)
    if len(joltage) == 11:
        joltage += str(max(bank))
        return int(joltage)

    remainding = bank[:-11 + len(joltage)]
    mx = max(remainding)
    ixs = [i for i, n in enumerate(remainding) if n == mx]
    joltage += str(mx)
    joltages = []
    for ix in ixs:
        joltages.append(get_next_digit(bank[ix + 1:], joltage))
    return max(joltages)

answer = 0
for bank in banks:
    answer += get_next_digit(bank, '')

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')