from pathlib import Path
import time
import hashlib

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read()

index = 0
password = {}

while len(password) < 8:
    h = hashlib.md5(''.join([input, str(index)]).encode()).hexdigest()
    if h.startswith('00000') and h[5].isdigit() and int(h[5]) < 8 and int(h[5]) not in password:
        password[int(h[5])] = h[6]
    index += 1

answer = ''.join([v for c, v in sorted(password.items(), key=lambda x: x[0])])
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
