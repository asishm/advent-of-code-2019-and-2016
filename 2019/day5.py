def parse(inp):
    return list(map(int, inp.split(',')))

def part1a(inp, init=1):
    
    i = 0
    while i < len(inp):
        # print(f"DEBUG: {i}")
        val = inp[i]

        strval = f"{val:05}"
        (a,b,c), opcode = strval[:3], int(strval[3:])
        # print(f"DEBUG: i={i}, a={a}, b={b}, c={c}, opcode={opcode}, val={strval}, arr={inp[:7]}")
        
        if opcode == 99:
            return
        elif opcode == 1:
            a1, a2, a3 = inp[i+1], inp[i+2], inp[i+3]
            s = 0
            if c == '0':
                s += inp[a1]
            elif c == '1':
                s += a1
            if b == '0':
                s += inp[a2]
            elif b == '1':
                s += a2
            # print(s, inp[225], inp[6], inp[a1], inp[a2], a, b, c)
            inp[a3] = s
            i += 4
            # break
        elif opcode == 2:
            a1, a2, a3 = inp[i+1], inp[i+2], inp[i+3]
            s = 1
            if c == '0':
                s *= inp[a1]
            elif c == '1':
                s *= a1
            if b == '0':
                s *= inp[a2]
            elif b == '1':
                s *= a2
            inp[a3] = s
            i += 4
        elif opcode == 3:
            a1 = inp[i+1]
            inp[a1] = init
            i += 2
        elif opcode == 4:
            a1 = inp[i+1]
            print('aah', inp[a1])
            i += 2
        else:
            i += 1

def part2(inp, init=5):
    
    i = 0
    while i < len(inp):
        # print(f"DEBUG: {i}")
        val = inp[i]

        strval = f"{val:04}"
        (b,c), opcode = strval[:2], int(strval[2:])
        print(f"DEBUG: i={i}, b={b}, c={c}, opcode={opcode}, val={strval}, arr={inp[:7]}")
        try:
            a1, a2, a3 = inp[i+1:i+4]
            val1 = inp[a1] if c == '0' else a1
            val2 = inp[a2] if b == '0' else a2
        except ValueError:
            assert opcode == 99
        
        if opcode == 99:
            return
        elif opcode == 1:
            inp[a3] = val1 + val2
            i += 4
            # break
        elif opcode == 2:
            inp[a3] = val1 * val2
            i += 4
        elif opcode == 3:
            inp[a1] = init
            i += 2
        elif opcode == 4:
            print('aah', inp[a1])
            i += 2
        elif opcode == 7:
            inp[a3] = int(val1 < val2)
            i += 4
        elif opcode == 8:
            inp[a3] = int(val1 == val2)
            i += 4
        elif opcode == 6:
            if val1 == 0:
                i = val2
            else:
                i += 3
        elif opcode == 5:
            if val1 != 0:
                i = val2
            else:
                i += 3
    
if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1a(inp.copy()))
    print('=====')
    print(part2(inp.copy()))