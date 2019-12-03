def parse(inp):
    import re
    pat = re.compile(r'(.*?)-(\d+)\[(.*?)\]')
    return [(k[0], int(k[1]), k[2]) for line in inp.splitlines() for k in pat.findall(line)]

def part1(inp):
    from collections import Counter
    tot = 0
    for letters, secid, checksum in inp:
        c = Counter(letters.replace('-', ''))
        checksum_verify = ''.join(k[0] for k in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:5])
        if checksum == checksum_verify:
            tot += secid
    return tot

def part2(inp):
    from string import ascii_lowercase
    for letters, secid, _ in inp:
        transf = ''.join([ascii_lowercase[(ord(k) - ord('a') + secid) % 26] if 'a' <= k <= 'z' else ' ' for k in letters])
        if 'north' in transf and 'pole' in transf:
            return secid


if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp))
    print(part2(inp))