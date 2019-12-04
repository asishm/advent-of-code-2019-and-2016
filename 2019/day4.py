import itertools
import collections
import re
import string

def parse(inp):
    return [int(k) for k in inp.strip().split('-')]

def part1(inp):
    count = 0
    # print(inp)
    for val in range(inp[0], inp[1] + 1):
        strval = str(val)
        if 100000 <= val <= 999999 and any(str(k)*2 in strval for k in range(10)) and strval == ''.join(sorted(strval)):
            count += 1

    return count

def part2(inp):
    count = 0
    # print(inp)
    for val in range(inp[0], inp[1] + 1):
        strval = str(val)
        if 100000 <= val <= 999999 and strval == ''.join(sorted(strval)) and any(len(list(z)) == 2 for k,z in itertools.groupby(strval)):
            count += 1

    return count

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))

