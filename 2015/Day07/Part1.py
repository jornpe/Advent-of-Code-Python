from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    operations = {line.split(' -> ')[1].strip(): line.split(' -> ')[0].strip() for line in f.read().split('\n')}


def getsignalfor(wire: str, ops: dict, cache: dict, override: int | None) -> int:

    if override is not None and wire == 'b':
        return override
    if wire.isdigit():
        return int(wire)
    if wire in cache:
        return cache[wire]

    output = None
    op = ops[wire]

    if op.isdigit():
        output = int(op)
    elif op in ops:
        output = getsignalfor(op, ops, cache, override)
    elif 'NOT' in op:
        _, r = op.split()
        r = getsignalfor(r, ops, cache, override)
        output = 65536 + ~r
    else:
        l, _, r = op.split()
        l = getsignalfor(l, ops, cache, override)
        r = getsignalfor(r, ops, cache, override)

        if 'AND' in op:
            output = l & r
        if 'OR' in op:
            output = l | r
        if 'LSHIFT' in op:
            output = l << r
        if 'RSHIFT' in op:
            output = l >> r

    cache[wire] = output
    return output


answer1 = getsignalfor('a', operations, {}, None)
answer2 = getsignalfor('a', operations, {}, answer1)
print(f'⭐ Part 1: {answer1} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer2} ; run time: {int((time.time() - start_time) * 1000)}ms')
