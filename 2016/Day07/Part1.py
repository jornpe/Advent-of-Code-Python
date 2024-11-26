from pathlib import Path
import time
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

supported = 0


def hasABBA(input: str) -> bool:
    if len(input) < 4:
        return False
    for a1, b1, b2, a2 in [list(input[idx:idx+4]) for idx in range(0, len(input) - 3)]:
        if a1+b1 == a2+b2 and a1 != b1:
            return True
    return False


def isSupported(input: str) -> bool:
    hypernets = re.findall(r"\[([a-z]+)]", input)
    for hypernet in hypernets:
        input = input.replace(hypernet, '')
        if hasABBA(hypernet):
            return False
    parts = re.findall(r"([a-z]+)", input)
    for part in parts:
        if hasABBA(part) or hasABBA(part):
            return True
    return False


for ip in lines:
    if isSupported(ip):
        supported += 1

answer = supported
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
