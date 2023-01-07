with open("input.txt") as f:
    inputs = [int(line) for line in f.read().split(',')]


def check(inputs: list) -> int:
    for i in range(0, len(inputs), 4):
        if inputs[i] == 99:
            break
        inputs[inputs[i+3]] = inputs[inputs[i+1]] + inputs[inputs[i + 2]] if inputs[i] == 1 else inputs[inputs[i+1]] * inputs[inputs[i + 2]]
    return inputs[0]


answer = 0
for x in range(100):
    for y in range(100):
        test = inputs[:]
        test[1] = x
        test[2] = y
        if check(test) == 19690720:
            answer = 100 * x + y

print(f'⭐ Part 1: {answer}')
