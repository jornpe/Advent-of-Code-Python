from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line.split() for line in f.read().splitlines()]

commands = [(cmd, int(v)) for cmd, v in lines]


def run_program(prg: list) -> tuple:
    accumulator = 0
    visited = []
    index = 0
    while True:
        if index >= len(prg):
            return True, accumulator

        cmd, value = prg[index]
        if index in visited:
            return False, accumulator
        visited.append(index)
        match cmd:
            case 'acc':
                accumulator += value
                index += 1
            case 'jmp':
                index += value
            case 'nop':
                index += 1


programs = [commands]
for idx, (cmd, value) in enumerate(commands):
    if cmd in ['nop', 'jmp']:
        prg = commands.copy()
        prg[idx] = ('nop', value) if cmd == 'jmp' else ('jmp', value)
        programs.append(prg)


for prg in programs:
    completed, answer = run_program(prg)
    if completed:
        break

print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
