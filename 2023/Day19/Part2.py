from pathlib import Path
import time
import re
import operator
import math

start_time = time.time()
operations = {'<': operator.lt, '>': operator.gt}
valueindex = {'x': 0, 'm': 1, 'a': 2, 's': 3}

with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read().split('\n\n')

workflows = {}

for workflow in input[0].splitlines():
    parsed = re.findall(r'([a-zA-Z]+)(<|>)?(\d+)?:?([a-zA-Z]+)?', workflow)
    id = parsed[0][0]
    ratings = [(w, o, v, d) for w, o, v, d in parsed[1::]]
    workflows[id] = ratings


def get_combinations(ratings: list) -> int:
    flow, ranges = ratings
    if flow == 'A':
        return math.prod(v2 - v1 + 1 for v1, v2 in ranges)
    if flow == 'R':
        return 0

    wf = workflows[flow]
    comb = 0
    for id, op, value, dest in wf:
        if op == '':
            comb += get_combinations([id, ranges])
        else:
            value = int(value)
            v_min, v_max = ranges[valueindex[id]]

            if v_min < value < v_max:
                if op == '<':
                    low_ranges = [r if idx != valueindex[id] else (r[0], value - 1) for idx, r in enumerate(ranges)]
                    ranges = [r if idx != valueindex[id] else (value, r[1]) for idx, r in enumerate(ranges)]

                    comb += get_combinations([dest, low_ranges])
                else:
                    high_ranges = [r if idx != valueindex[id] else (value + 1, r[1]) for idx, r in enumerate(ranges)]
                    ranges = [r if idx != valueindex[id] else (r[0], value) for idx, r in enumerate(ranges)]

                    comb += get_combinations([dest, high_ranges])

    return comb


combinations = get_combinations(['in', [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]])
print(f'⭐⭐ Part 2: {combinations}, run time: {int((time.time() - start_time) * 1000)}ms')
