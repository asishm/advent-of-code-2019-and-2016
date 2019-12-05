def parse(inp):
    return list(map(int, inp.split(',')))

def part1(inp, init=1):
    
    i = 0
    while i < len(inp):
        val = inp[i]
        strval = f"{val:04}"
        (b,c), opcode = strval[:2], int(strval[2:])
        
        if opcode == 99:
            return

        a1, a2, a3 = inp[i+1:i+4]
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
            inp[a1] = init
            i += 2
        elif opcode == 4:
            print('OUTPUT', val1)
            i += 2

def part2(inp, init=5):
    
    i = 0
    while i < len(inp):
        val = inp[i]
        strval = f"{val:04}"
        (b,c), opcode = strval[:2], int(strval[2:])
        
        if opcode == 99:
            return

        a1, a2, a3 = inp[i+1:i+4]
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
            inp[a1] = init
            i += 2
        elif opcode == 4:
            print('OUTPUT', inp[a1])
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