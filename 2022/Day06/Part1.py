import os.path

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    input = f.read()

for i in range(4, len(input)):
    if len(set(input[i-4:i])) == 4:
        print(i)
        break

