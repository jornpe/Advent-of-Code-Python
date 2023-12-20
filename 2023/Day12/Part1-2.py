from pathlib import Path
import re
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]


def get_value(springs: list, groups: list, in_arrangement: bool, number: int, cache: dict) -> int:
    key = (*springs, *groups, in_arrangement, number)
    if key in cache:
        return cache[key]

    if not springs and not groups:
        return 1

    if springs and not groups:
        return 0 if '#' in springs else 1

    if not springs and len(groups) == 1:
        return 1 if groups[0] == number else 0

    if not springs and groups:
        return 0

    next = springs.pop(0)

    if next == '?':
        value = (get_value(['#'] + springs[::], groups[::], in_arrangement, number, cache) +
                 get_value(['.'] + springs[::], groups[::], in_arrangement, number, cache))

        cache[key] = value
        return value

    if next == '.' and not in_arrangement:
        return get_value(springs[::], groups[::], in_arrangement, number, cache)

    if next == '.' and in_arrangement:
        return 0 if number != groups.pop(0) else get_value(springs[::], groups[::], False, 0, cache)

    if next == '#':
        return get_value(springs[::], groups[::], True, number + 1, cache)


def get_answer(repeated: int) -> int:
    answer = 0
    for line in lines:
        groups = list(map(int, re.findall(r'\d+', ','.join([line.split()[1]] * repeated))))
        springs = list('?'.join([line.split()[0]] * repeated))
        answer += get_value(springs, groups, False, 0, {})
    return answer


part1 = get_answer(1)
part2 = get_answer(5)

print(f'⭐ Part 1: {part1}')
print(f'⭐⭐ Part 2: {part2}, run time: {int((time.time() - start_time) * 1000)}ms')

