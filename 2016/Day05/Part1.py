from pathlib import Path
import time
import hashlib

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read()

index = 0
password = []

while len(password) < 8:
    h = hashlib.md5(''.join([input, str(index)]).encode()).hexdigest()
    if h.startswith('00000'):
        password.append(h[5])
    index += 1

answer = ''.join(password)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
