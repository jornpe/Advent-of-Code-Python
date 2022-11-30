with open("test.txt") as f:
    inputs = [int(i) for i in f]

for i in inputs:
    for j in inputs:
        if i + j == 2020:
            answer = i * j

print(answer)
