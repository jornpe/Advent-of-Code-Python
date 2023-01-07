with open("input.txt") as f:
    input = [int(line) for line in f.read().split(',')]

input[1] = 12
input[2] = 2

for i in range(0, len(input), 4):
    if input[i] == 99:
        break
    input[input[i+3]] = input[input[i+1]] + input[input[i + 2]] if input[i] == 1 else input[input[i+1]] * input[input[i + 2]]

print(f'⭐ Part 1: {input[0]}')
