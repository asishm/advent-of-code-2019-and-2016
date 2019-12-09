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
            # print(f"SETTING MEMORY: {a1}")
            if c == '2':
                memory[a1 + relative_base] = yield
            else:
                memory[a1] = yield
            # if inp_count == 0:
            #     memory[a1] = phase
            #     inp_count += 1
            # else:
            #     memory[a1] = 1
            i += 2
        elif opcode == 4:
            # print(strval, opcode, b, c, a1, a2, a3, val1, val2)
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
    # print(len(inp))
    a = compute(inp)
    next(a)
    return a.send(1)

def part2(inp):
    # print(len(inp))
    a = compute(inp)
    next(a)
    return a.send(2)

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))
