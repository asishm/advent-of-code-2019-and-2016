import itertools

def parse(inp):
    # print(inp)
    return [list(map(int, k.strip().split())) for k in inp.splitlines() if k.strip()]

def part1(inp):
    inp = [sorted(k) for k in inp]
    return sum(k[0] + k[1] > k[2] for k in inp)

def part2(inp):
    inp = itertools.chain.from_iterable(zip(*inp))
    count = 0
    while True:
        try:
            lens = sorted([next(inp) for _ in range(3)])
        except StopIteration:
            break
        if lens[0] + lens[1] > lens[2]:
            count += 1
    return count


if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp))
    print(part2(inp))