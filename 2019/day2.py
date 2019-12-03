import itertools
import collections
import re
import string

def parse(inp):
    return list(map(int, inp.split(',')))

def part1(inp, noun=12, verb=2):
    
    inp[1] = noun
    inp[2] = verb
    i = 0
    while True:
        c = inp[i]
        # print(i, c, inp)
        if c == 99:
            # print(inp)
            return inp[0]
        elif c == 1:
            inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]
            i += 4
        elif c == 2:
            inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]
            i += 4
        else:
            i += 1
    

def part2(inp):

    for i in range(100):
        for j in range(100):
            inp2 = inp.copy()

            val = part1(inp2, i, j)
            if val == 19690720:
                return 100 * i + j


if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))