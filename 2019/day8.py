from collections import Counter

def parse(inp):
    return [int(k) for k in inp.strip()]

def part1(inp, *args, **kwargs):
    layers = {idx:Counter(inp[i:i+25*6]) for idx,i in enumerate(range(0, len(inp), 25*6))}
    min_layer = min(layers, key=lambda x: layers[x][0])
    return layers[min_layer][1] * layers[min_layer][2]

def part2(inp, *args, **kwargs):
    ## ugly one-liner
    ## return '\n'.join([''.join([next('■■ ' if val == 1 else '   ' for val in inp[i*25+j:len(inp):25*6] if val !=2) for j in range(25)]) for i in range(6)])
    grid = [[inp[i*25+j:len(inp):25*6] for j in range(25)] for i in range(6)]
    out = []
    for row in grid:
        tmp = []
        for vals in row:
            tmp.append(next('■■ ' if val == 1 else '   ' for val in vals if val !=2))
        out.append(''.join(tmp))
    return '\n'.join(out)

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print(part2(inp.copy()))