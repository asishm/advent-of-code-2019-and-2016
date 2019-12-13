import math
import collections
import itertools
import string
import re

def compute(inp, phase=0):
    yield
    from collections import defaultdict
    i = 0
    relative_base = 0
    memory = defaultdict(int)
    for idx,point in enumerate(inp):
        memory[idx] = point
    while True:
        val = memory[i]
        strval = f"{val:05}"
        (a,b,c), opcode = strval[:3], int(strval[3:])
        
        if opcode == 99:
            return

        a1, a2, a3 = memory[i+1], memory[i+2], memory[i+3]
        # print(strval, opcode, b, c, a1, a2, a3)
        # print(memory, a1, a2, a3, b, c, opcode)
        val1 = memory[a1] if c == '0' else a1 if c == '1' else memory[a1 + relative_base]
        val2 = memory[a2] if b == '0' else a2 if b == '1' else memory[a2 + relative_base]
        a3 = a3 + relative_base if a == '2' else a3
        # print(f"STRVAL: {strval}, OPCODE: {opcode}, PARAM1: {a1}, VAL1: {val1}, MODE1: {c} PARAM2: {a2}, VAL2: {val2}, MODE2: {b} PARAM3: {a3}, MODE3: {a}")
        if opcode == 1:
            memory[a3] = val1 + val2
            i += 4
        elif opcode == 2:
            memory[a3] = val1 * val2
            i += 4
        elif opcode == 3:
            val = yield
            idx = a1 + relative_base if c == '2' else a1
            memory[idx] = val
            # print(f"SETTING MEMORY: a1={a1}, mode={c} relative={relative_base} input={val}")
            i += 2
        elif opcode == 4:
            # print(f"YIELDING VALUE: {val1}")
            yield val1
            i += 2
        elif opcode == 7:
            memory[a3] = int(val1 < val2)
            i += 4
        elif opcode == 8:
            memory[a3] = int(val1 == val2)
            i += 4
        elif opcode == 6:
            i = val2 if val1 == 0 else i + 3
        elif opcode == 5:
            i = val2 if val1 != 0 else i + 3
        elif opcode == 9:
            relative_base += val1
            # print(f"CHANGE RELATIVE BASE: {relative_base} {val1}")
            i += 2

def parse(inp):
    return [int(k) for k in inp.strip().split(',')]

def part1(inp):
    computer = compute(inp.copy())
    next(computer)
    i = 0
    x, y, val = None, None, None
    items = collections.defaultdict(int)
    while True:
        try:
            out = computer.send(1)
        except StopIteration:
            break
        assert out is not None
        if i % 3 == 0:
            x = out
        elif i % 3 == 1:
            y = out
        else:
            val = out
            items[(x,y)] = val
            x, y, val = None, None, None
        i += 1
    # print(items)
    return sum(k == 2 for k in items.values())

def draw_grid(x, y, val):
    xmax = max(x)
    xmin = min(x)
    ymax = max(y)
    ymin = min(y)
    c = collections.defaultdict(int)
    for a,b,d in zip(x,y,val):
        c[(a,b)] = d
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            v = c[(x,y)]
            if v == 0:
                print(' ', end='')
            else:
                print(v, end='')
        print()

def part2(inp):
    import random
    inp[0] = 2
    computer = compute(inp)
    next(computer)
    ball = None
    paddle = None
    x = y = val = None
    i = 0
    score = None
    while True:
        try:
            # draw_grid(x_arr, y_arr, val_arr)
            if ball and paddle:
                if ball[0] < paddle[0]:
                    player_inp = -1
                elif ball[0] > paddle[0]:
                    player_inp = 1
                else:
                    player_inp = 0
            else:
                player_inp = 0
            out = computer.send(player_inp)
        except StopIteration:
            break
        # print(out, end=',')
        if out is None:
            continue
        if i % 3 == 0:
            x = out
        elif i % 3 == 1:
            y = out
        else:
            if x == -1 and y == 0:
                score = out
                print(score)
            else:
                val = out
                if val == 3:
                    paddle = (x, y)
                elif val == 4:
                    ball = (x, y)
        i += 1
    print(score)


if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))