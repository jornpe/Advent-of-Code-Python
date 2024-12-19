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


def runprogram(program: list, registers: dict) -> list:
    idx = 0
    output = []
    while True:
        if idx >= len(program):
            return output
        opcode, operand = program[idx], program[idx + 1]
        idx += 2
        match opcode:
            case 0:
                registers['A'] = floor(registers['A'] / (2 ** combo(operand)))
            case 1:
                registers['B'] = registers['B'] ^ operand
            case 2:
                registers['B'] = combo(operand) % 8
            case 3:
                idx = idx if registers['A'] == 0 else operand
            case 4:
                registers['B'] = registers['B'] ^ registers['C']
            case 5:
                output.append(combo(operand) % 8)
            case 6:
                registers['B'] = floor(registers['A'] / (2 ** combo(operand)))
            case 7:
                registers['C'] = floor(registers['A'] / (2 ** combo(operand)))



answer = ','.join(str(n) for n in runprogram(program, registers))
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
