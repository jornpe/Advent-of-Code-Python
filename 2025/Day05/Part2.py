from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    ranges = [(int(range.split('-')[0]), int(range.split('-')[1])) for range in f.read().split('\n\n')[0].split('\n')]

included = []


def get_range(n_min: int, n_max: int, included: list) -> list:
    for inc_min, inc_max in included:

        if n_min >= inc_min and n_max <= inc_max:
            return []

        if n_min < inc_min and n_max > inc_max:
            right = get_range(n_min, inc_max - 1, included)
            left = get_range(inc_max + 1, n_max, included)
            return [*right, *left]

        if  inc_min <= n_min <= inc_max:
            n_min = inc_max + 1

        if inc_min <= n_max <= inc_max:
            n_max = inc_min - 1

    return [(n_min, n_max)]


for new_min, new_max in ranges:
    included += get_range(new_min, new_max, included)

answer = sum(inc_max - inc_min + 1 for inc_min, inc_max in included)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')