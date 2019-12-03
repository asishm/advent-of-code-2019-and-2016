import hashlib

def parse(inp):
    return inp.strip()

def part1(inp):
    idx = 1
    pwd = []
    for _ in range(8):
        while True:
            s = f"{inp}{idx}".encode()
            hashed = hashlib.md5(s).hexdigest()
            if hashed[:5] == '00000':
                pwd.append(hashed[5])
                break
            idx += 1
        idx += 1
    return ''.join(pwd)

def part2(inp):
    idx = 1
    pwd = [None] * 8
    while not all(pwd):
        s = f"{inp}{idx}".encode()
        hashed = hashlib.md5(s).hexdigest()
        if hashed[:5] == '00000':
            pos, char = hashed[5:7]
            if '0' <= pos <= '7' and pwd[int(pos)] is None:
                pwd[int(pos)] = char
                # print(pos, char, pwd)
        idx += 1
    return ''.join(pwd)

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp))
    print(part2(inp))