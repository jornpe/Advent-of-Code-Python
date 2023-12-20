from pathlib import Path
import re
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    steps = f.read().split(',')

answer = 0
boxes = {}


def get_value(label) -> int:
    s = 0
    for c in list(label):
        s += ord(c)
        s *= 17
        s %= 256
    return s


print(f'⭐ Part 1: {sum(map(get_value, steps))}')

for step in steps:
    label, op, number = re.findall(r'([a-z]+)(=|-)(\d+)?', step)[0]
    boxnumber = int(get_value(label))
    if op == '=':
        if boxnumber in boxes:
            boxes[boxnumber] = boxes[boxnumber] + [(label, number)] if not any(x[0] == label for x in boxes[boxnumber]) else list(x if x[0] != label else (label, number) for x in boxes[boxnumber])
        else:
            boxes[boxnumber] = [(label, number)]
    else:
        if boxnumber in boxes:
            boxes[boxnumber] = list(x for x in boxes[boxnumber] if x[0] != label)

focalpower = 0

for boxnumber, box in boxes.items():
    for slot, (label, length) in enumerate(box, 1):
        focalpower += (boxnumber + 1) * slot * int(length)

print(f'⭐⭐ Part 2: {focalpower}, run time: {int((time.time() - start_time) * 1000)}ms')
