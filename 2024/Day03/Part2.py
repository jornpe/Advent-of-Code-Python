import re
from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

result = 0

do = True
for line in lines:
    commands = re.findall(r'(mul)\((\d+),(\d+)\)|(do)\(\)|(don)\'t\(\)', line)
    for cmd in commands:
        if 'do' in cmd:
            do = True
        elif 'don' in cmd:
            do = False
        elif do:
            result += int(cmd[1]) * int(cmd[2])

answer = result
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')