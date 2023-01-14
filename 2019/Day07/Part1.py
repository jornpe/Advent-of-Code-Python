import itertools as it

with open("input.txt") as f:
    inputs = list(map(int, f.read().split(',')))


def get_params(prg: list, opcode: int, pointer: int, number_of_params: int) -> list:
    parameters = []
    for i in range(1, number_of_params + 1):
        value = prg[pointer + i]
        param = value if str(opcode).zfill(2 + number_of_params)[-2 - i] == '1' else prg[value]
        parameters.append(param)
    return parameters


def run_program(prg: list, input: list) -> list:
    out = 0
    pointer = 0
    while pointer < len(prg):
        match prg[pointer] % 100:
            case 1:
                param1, param2 = get_params(prg, prg[pointer], pointer, 2)
                output = prg[pointer + 3]
                prg[output] = param1 + param2
                pointer += 4

            case 2:
                param1, param2 = get_params(prg, prg[pointer], pointer, 2)
                output = prg[pointer + 3]
                prg[output] = param1 * param2
                pointer += 4

            case 3:
                output = prg[pointer + 1]
                prg[output] = input.pop()
                pointer += 2

            case 4:
                out = prg[prg[pointer + 1]]
                pointer += 2

            case 5:
                param1, param2 = get_params(prg, prg[pointer], pointer, 2)
                pointer = param2 if param1 != 0 else pointer + 3

            case 6:
                param1, param2 = get_params(prg, prg[pointer], pointer, 2)
                pointer = param2 if param1 == 0 else pointer + 3

            case 7:
                param1, param2 = get_params(prg, prg[pointer], pointer, 2)
                output = prg[pointer + 3]
                prg[output] = 1 if param1 < param2 else 0
                pointer += 4

            case 8:
                param1, param2 = get_params(prg, prg[pointer], pointer, 2)
                output = prg[pointer + 3]
                prg[output] = 1 if param1 == param2 else 0
                pointer += 4

            case 99:
                return out
    return out


def get_highest_signal(prg: list) -> int:
    maximum = 0
    for sequence in it.permutations(range(5), 5):
        phase_setting = 0
        for s in sequence:
            phase_setting = run_program(list(prg), [phase_setting, s])
        if phase_setting > maximum:
            maximum = phase_setting
    return maximum


print(f'⭐ Part 1: {get_highest_signal(inputs)}')
