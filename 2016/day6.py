def parse(inp):
    return [k.strip() for k in inp.splitlines() if k.strip()]

def part1(inp):
    from collections import Counter
    inp = list(zip(*inp))

    return ''.join(Counter(column).most_common(1)[0][0] for column in inp)

def part2(inp):
    from collections import Counter
    inp = list(zip(*inp))

    return ''.join(Counter(column).most_common()[-1][0] for column in inp)

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp))
    print(part2(inp))