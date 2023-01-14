with open("input.txt") as f:
    input = list(map(int, list(f.read())))

layers = [input[i:i+150] for i in range(0, len(input), 150)]

minimum = 150
answer = 0
for layer in layers:
    zeros = len([x for x in list(layer) if x == 0])
    if zeros < minimum:
        minimum = zeros
        ones = len([x for x in list(layer) if x == 1])
        twos = len([x for x in list(layer) if x == 2])
        answer = ones * twos

print(f'⭐ Part 1: {answer}')
