from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    sequence = f.read()

for _ in range(40):
    nseq = ''
    cd = ''
    for c in sequence:
        if cd != '' and c not in cd:
            nseq += str(len(cd)) + cd[0]
            cd = c
        else:
            cd += c
    sequence = nseq + str(len(cd)) + cd[0]

answer = len(sequence)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
