with open("input.txt") as f:
    inputs = [(index, int(line)) for index, line in enumerate(f.read().split('\n'), 0)]

length = len(inputs) - 1

for idx, number in list(inputs):
    index = inputs.index((idx, number))
    inputs.insert((number + index) % length, inputs.pop(index))

idx = [idx for idx, (i, n) in enumerate(inputs) if n == 0][0]

answer = inputs[(1000 + idx) % (length + 1)][1] + inputs[(2000 + idx) % (length + 1)][1] + inputs[(3000 + idx) % (length + 1)][1]

print(answer)
