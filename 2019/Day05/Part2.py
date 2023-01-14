with open("input.txt") as f:
    inputs = list(map(int, f.read().split(',')))


def get_params(opcode: int, program: list, pointer: int, number_of_params: int) -> list:
    parameters = []
    for i in range(1, number_of_params + 1):
        value = program[pointer + i]
        param = value if str(opcode).zfill(2 + number_of_params)[-2 - i] == '1' else program[value]
        parameters.append(param)
    return parameters


def run_program(prg: list, input: int) -> list:
    out = []
    pointer = 0
    while pointer < len(prg):
        match prg[pointer] % 100:
            case 1:
                param1, param2 = get_params(prg[pointer], prg, pointer, 2)
                output = prg[pointer + 3]
                prg[output] = param1 + param2
                pointer += 4

            case 2:
                param1, param2 = get_params(prg[pointer], prg, pointer, 2)
                output = prg[pointer + 3]
                prg[output] = param1 * param2
                pointer += 4

            case 3:
                output = prg[pointer + 1]
                prg[output] = input
                pointer += 2

            case 4:
                out.append(prg[prg[pointer + 1]])
                pointer += 2

            case 5:
                param1, param2 = get_params(prg[pointer], prg, pointer, 2)
                pointer = param2 if param1 != 0 else pointer + 3

            case 6:
                param1, param2 = get_params(prg[pointer], prg, pointer, 2)
                pointer = param2 if param1 == 0 else pointer + 3

            case 7:
                param1, param2 = get_params(prg[pointer], prg, pointer, 2)
                output = prg[pointer + 3]
                prg[output] = 1 if param1 < param2 else 0
                pointer += 4

            case 8:
                param1, param2 = get_params(prg[pointer], prg, pointer, 2)
                output = prg[pointer + 3]
                prg[output] = 1 if param1 == param2 else 0
                pointer += 4

            case 99:
                return out
    return out


answer = run_program(inputs, 5)
print(f'⭐⭐ Part 2: {answer[-1]}')
