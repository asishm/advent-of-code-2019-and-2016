import math
import collections
import itertools
import string
import re

def compute(inp, phase=0):
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
            # print(f"SETTING MEMORY: a1={a1}, mode={c} relative={relative_base} input={val}")
            if c == '2':
                memory[a1 + relative_base] = val
            else:
                memory[a1] = val
            # if inp_count == 0:
            #     memory[a1] = phase
            #     inp_count += 1
            # else:
            #     memory[a1] = 1
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
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    grid_color = collections.defaultdict(int)
    grid_count = collections.defaultdict(int)
    x, y = 0, 0
    start_dir = 0
    out_count = 0
    machine = compute(inp.copy())
    next(machine)
    while True:
        try:
            # print(f"SENDING {grid_color[(x,y)]} or 0")
            out = machine.send(grid_color[(x,y)] or 0)
            # print(f'RECEIVED {out}')
        except StopIteration:
            break
        if out is None:
            continue
        if out_count % 2 == 0:
            grid_color[(x,y)] = out
            grid_count[(x,y)] += 1
        else:
            assert out in (0,1)
            if out == 0:
                start_dir = (start_dir - 1) % len(dirs)
            else:
                start_dir = (start_dir + 1) % len(dirs)

            direction = dirs[start_dir]
            x, y = x + direction[0], y + direction[1]
            # print(f"NEW (x,y) = ({x}, {y})")
        out_count += 1
    # print(grid_count)
    # print(grid_color)
    # print(len([(k,v) for k,v in grid_count.items() if v is not None and v > 0]))
    return len([(k,v) for k,v in grid_count.items() if v is not None and v > 0])

def part2(inp):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    grid_color = collections.defaultdict(int)
    grid_count = collections.defaultdict(int)
    grid_color[(0,0)] = 1
    x, y = 0, 0
    start_dir = 0
    out_count = 0
    machine = compute(inp.copy())
    next(machine)
    while True:
        try:
            # print(f"SENDING {grid_color[(x,y)]} or 0")
            out = machine.send(grid_color[(x,y)] or 0)
            # print(f'RECEIVED {out}')
        except StopIteration:
            break
        if out is None:
            continue
        if out_count % 2 == 0:
            grid_color[(x,y)] = out
            grid_count[(x,y)] += 1
        else:
            assert out in (0,1)
            if out == 0:
                start_dir = (start_dir - 1) % len(dirs)
            else:
                start_dir = (start_dir + 1) % len(dirs)

            direction = dirs[start_dir]
            x, y = x + direction[0], y + direction[1]
            # print(f"NEW (x,y) = ({x}, {y})")
        out_count += 1
    # print(grid_count)
    # print(grid_color)
    # print(len([(k,v) for k,v in grid_count.items() if v is not None and v > 0]))
    grid_x = [k[0] for k in grid_color]
    grid_y = [k[1] for k in grid_color]
    for x in range(min(grid_x), max(grid_x) + 1):
        for y in range(min(grid_y), max(grid_y) + 1):
            if grid_color[(x,y)] == 1:
                print('\u2588', end='')
            else:
                print(' ', end='')
        print()

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))