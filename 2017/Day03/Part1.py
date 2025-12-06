from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('test.txt')) as f:
    square = f.read()



answer = 0
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
