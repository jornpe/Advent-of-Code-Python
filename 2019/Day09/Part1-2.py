with open("input.txt") as f:
    program = {x: int(i) for x, i in enumerate(f.read().split(','))}


def get_params(prg: dict, pointer: int, number_of_params: int, relative_base: int, last_is_output_pointer: bool = False) -> list:
    params = []
    param_modes = str(prg[pointer]).zfill(2 + number_of_params)[:-2][::-1]
    for i in range(0, number_of_params):
        output_pointer = last_is_output_pointer and i == number_of_params - 1
        param_pointer = pointer + i + 1
        value = prg[param_pointer]
        param = 0
        match param_modes[i]:
            case '0':
                if output_pointer:
                    param = value
                else:
                    param = prg[value] if value in prg else 0
            case '1':
                param = param_pointer if output_pointer else value
            case '2':
                if output_pointer:
                    param = relative_base + value
                else:
                    param = prg[relative_base + value] if relative_base + value in prg else 0
        params.append(param)
    return params


def run_program(prg: dict, input: int) -> list:
    out = []
    pointer = 0
    relative_base = 0
    while pointer < len(prg):
        match prg[pointer] % 100:
            case 1:  # Opcode 1 adds together numbers read from two positions and stores the result in a third position
                param1, param2, output = get_params(prg, pointer, 3, relative_base, True)
                prg[output] = param1 + param2
                pointer += 4

            case 2:  # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them
                param1, param2, output = get_params(prg, pointer, 3, relative_base, True)
                prg[output] = param1 * param2
                pointer += 4

            case 3:  # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter
                param, = get_params(prg, pointer, 1, relative_base, True)
                prg[param] = input
                pointer += 2

            case 4:  # Opcode 4 outputs the value of its only parameter
                param, = get_params(prg, pointer, 1, relative_base, True)
                out.append(prg[param])
                pointer += 2

            case 5:  # is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing
                param1, param2 = get_params(prg, pointer, 2, relative_base)
                pointer = param2 if param1 != 0 else pointer + 3

            case 6:  # jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing
                param1, param2 = get_params(prg, pointer, 2, relative_base)
                pointer = param2 if param1 == 0 else pointer + 3

            case 7:  # less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
                param1, param2, output = get_params(prg, pointer, 3, relative_base, True)
                prg[output] = 1 if param1 < param2 else 0
                pointer += 4

            case 8:  # equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
                param1, param2, output = get_params(prg, pointer, 3, relative_base, True)
                prg[output] = 1 if param1 == param2 else 0
                pointer += 4

            case 9:  # Opcode 9 adjusts the relative base by the value of its only parameter
                param, = get_params(prg, pointer, 1, relative_base)
                relative_base += param
                pointer += 2

            case 99:
                return out
    return out


answer_part1, = run_program(program, 1)
answer_part2, = run_program(program, 2)

print(f'⭐ Part 1: {answer_part1}')
print(f'⭐ Part 2: {answer_part2}')
