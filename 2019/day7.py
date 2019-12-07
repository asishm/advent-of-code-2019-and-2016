import itertools
import collections
import re
import string
import networkx as nx

def parse(inp):
    return [int(k) for k in inp.strip().split(',')]

def part1(inp, *args, **kwargs):
    
    max_thrust = float('-inf')
    for phase_list in itertools.permutations([0,1,2,3,4], 5):
        init = 0
        for amp_idx in range(5):
            amp = compute(inp.copy(), phase_list[amp_idx])
            next(amp)
            while True:
                try:
                    val = amp.send(init)
                except StopIteration:
                    break
                if val is not None:
                    init = val
                    break
        if init >= max_thrust:
            max_thrust = max(max_thrust, init)

    return max_thrust

def part2(inp, *args, **kwargs):
    max_thrust = float('-inf')
    for phase_list in itertools.permutations([5,6,7,8,9],5):
        amps = [compute(inp.copy(), phase) for phase in phase_list]
        [next(amp) for amp in amps]
        init = [0]
        for amp_idx in itertools.cycle(range(5)):
            # amp, cp = amps[amp_idx]
            amp = amps[amp_idx]
            # print(instructions)
            val = init[-1]
            # print(f"PHASE: {phase} AMP: {amp_idx} == SENDING {val}")
            try:
                val2 = amp.send(val)
            except StopIteration:
                break
                # print(f"PHASE: {phase} AMP: {amp_idx} == STOPITERATION")
            # print(f"PHASE: {phase} AMP: {amp_idx} == RECEIVED {val2} INP: {cp}")
            if val2 is not None:
                init.append(val2)
            # print(init, phase_list[amp])
        if init[-1] >= max_thrust:
            max_thrust = max(max_thrust, init[-1])
            # print(max_thrust, phase)

    return max_thrust

def compute(inp, phase=0):
    
    i = 0
    inp_count = 0
    while i < len(inp):
        val = inp[i]
        strval = f"{val:04}"
        (b,c), opcode = strval[:2], int(strval[2:])
        
        if opcode == 99:
            return

        a1, a2, *a3 = inp[i+1:i+4]
        if a3:
            a3 = a3[0]
        # print(inp, a1, a2, a3, b, c, opcode)
        val1 = inp[a1] if c == '0' else a1
        try:
            val2 = inp[a2] if b == '0' else a2
        except IndexError:
            assert opcode in (3,4)

        if opcode == 1:
            inp[a3] = val1 + val2
            i += 4
        elif opcode == 2:
            inp[a3] = val1 * val2
            i += 4
        elif opcode == 3:
            if inp_count == 0:
                inp[a1] = phase
                inp_count += 1
            else:
                k = yield
                inp[a1] = k
            i += 2
        elif opcode == 4:
            yield val1 
            i += 2
        elif opcode == 7:
            inp[a3] = int(val1 < val2)
            i += 4
        elif opcode == 8:
            inp[a3] = int(val1 == val2)
            i += 4
        elif opcode == 6:
            i = val2 if val1 == 0 else i + 3
        elif opcode == 5:
            i = val2 if val1 != 0 else i + 3

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print('=====')
    print(part2(inp.copy()))
