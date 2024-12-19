from math import floor
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = [line for line in f.read().split('\n\n')]

registers = {list(reg.split(':')[0])[-1]: int(reg.split(':')[1]) for reg in input[0].split('\n')}
program = [int(n) for n in input[1].split(':')[1].split(',')]


def combo(op: int) -> int:
    match op:
        case 1 | 2 | 3:
            return op
        case 4:
            return registers['A']
        case 5:
            return registers['B']
        case 6:
            return registers['C']


def runprogram(prog: list, reg: dict, a: int) -> list:
    idx = 0
    output = []
    reg['A'] = a
    while True:
        if idx >= len(prog):
            return output
        opcode, operand = prog[idx], prog[idx + 1]
        idx += 2
        match opcode:
            case 0:
                reg['A'] = floor(reg['A'] / (2 ** combo(operand)))
            case 1:
                reg['B'] = reg['B'] ^ operand
            case 2:
                reg['B'] = combo(operand) % 8
            case 3:
                idx = idx if reg['A'] == 0 else operand
            case 4:
                reg['B'] = reg['B'] ^ reg['C']
            case 5:
                output.append(combo(operand) % 8)
            case 6:
                reg['B'] = floor(reg['A'] / (2 ** combo(operand)))
            case 7:
                reg['C'] = floor(reg['A'] / (2 ** combo(operand)))



def findvalue() -> int:
    value = 0
    for idx, _ in enumerate(program):
        value *= 8
        while True:
            result = runprogram(program, registers, value)
            if result == program:
                return value
            if result == program[- 1 - idx:]:
                break
            value += 1


answer = findvalue()
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
