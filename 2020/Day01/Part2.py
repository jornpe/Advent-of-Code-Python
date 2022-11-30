with open("test.txt") as f:
    inputs = [int(i) for i in f]

for i in inputs:
    for j in inputs:
        for x in inputs:
            if x + i + j == 2020:
                answer = x * i * j

print(answer)