def parse(inp):
    return inp.splitlines()

def part1(inp):
    import re
    count = 0
    abba_pat = re.compile(r'(?P<a>.)(?P<b>.)(?P=b)(?P=a)')
    inside_pat = re.compile(r'\[.*?\]')
    for i in inp:
        insides = inside_pat.findall(i)
        outsides = inside_pat.split(i)

        inside_bool = any(abba_pat.search(k) and len(set(abba_pat.search(k).groups())) == 2 for k in insides)
        outside_bool = any(abba_pat.search(k) and len(set(abba_pat.search(k).groups())) == 2 for k in outsides)

        if outside_bool and not inside_bool:
            count += 1
    return count

def part2(inp):
    import re
    count = 0
    inside_pat = re.compile(r'\[.*?\]')

    for i in inp:
        found = False
        insides = inside_pat.findall(i)
        outsides = inside_pat.split(i)
        potentials = set()

        for out in outsides:
            for j in range(len(out)-2):
                a,b,c = out[j:j+3]
                if a == c and b != c:
                    potentials.add((a,b))

        # print(potentials, outsides, insides)
        for ins in insides:
            ins = ins[1:-1]
            for j in range(len(ins)-2):
                a,b,c = ins[j:j+3]
                if a == c and b != c and (b,a) in potentials:
                    count += 1
                    found = True
                    break
            if found:
                break
    return count



if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp))
    print(part2(inp))