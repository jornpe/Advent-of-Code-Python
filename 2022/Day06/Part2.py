import os.path

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    input = f.read()

for i in range(14, len(input)):
    if len(set(input[i-14:i])) == 14:
        print(i)
        break