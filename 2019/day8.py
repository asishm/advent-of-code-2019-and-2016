from collections import Counter
from PIL import Image
import subprocess as sp
import os

def parse(inp):
    return [int(k) for k in inp.strip()]

def part1(inp, *args, **kwargs):
    layers = [Counter(inp[i:i+25*6]) for idx,i in enumerate(range(0, len(inp), 25*6))]
    min_layer = min(layers, key=lambda x: x[0])
    return min_layer[1] * min_layer[2]

letters = {
  'A' : [[0,1,1,1,1,1],[1,0,0,1,0,0],[1,0,0,1,0,0],[0,1,1,1,1,1],[0,0,0,0,0,0]],
  'B' : [[1,1,1,1,1,1],[1,0,1,0,0,1],[1,0,1,0,0,1],[0,1,0,1,1,0],[0,0,0,0,0,0]],
  'C' : [[0,1,1,1,1,0],[1,0,0,0,0,1],[1,0,0,0,0,1],[0,1,0,0,1,0],[0,0,0,0,0,0]],
  'E' : [[1,1,1,1,1,1],[1,0,1,0,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,0,0,0,0,0]],
  'F' : [[1,1,1,1,1,1],[1,0,1,0,0,0],[1,0,1,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0]],
  'G' : [[0,1,1,1,1,0],[1,0,0,0,0,1],[1,0,0,1,0,1],[0,1,0,1,1,1],[0,0,0,0,0,0]],
  'H' : [[1,1,1,1,1,1],[0,0,1,0,0,0],[0,0,1,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0]],
  'J' : [[0,0,0,0,1,0],[0,0,0,0,0,1],[1,0,0,0,0,1],[1,1,1,1,1,0],[0,0,0,0,0,0]],
  'K' : [[1,1,1,1,1,1],[0,0,1,0,0,0],[0,1,0,1,1,0],[1,0,0,0,0,1],[0,0,0,0,0,0]],
  'L' : [[1,1,1,1,1,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,0]],
  'P' : [[1,1,1,1,1,1],[1,0,0,1,0,0],[1,0,0,1,0,0],[0,1,1,0,0,0],[0,0,0,0,0,0]],
  'R' : [[1,1,1,1,1,1],[1,0,0,1,0,0],[1,0,0,1,1,0],[0,1,1,0,0,1],[0,0,0,0,0,0]],
  'U' : [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,0,0,0,0,1],[1,1,1,1,1,0],[0,0,0,0,0,0]],
  'Y' : [[1,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,1,1],[0,0,1,0,0,0],[1,1,0,0,0,0]],
  'Z' : [[1,0,0,0,1,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,1,0,0,0,1],[0,0,0,0,0,0]],
}

def part2_oneline(inp, *args, **kwargs):
    ## ugly one-liner
    return '\n'.join(''.join(next('\u2588' if val == 1 else ' ' for val in inp[i*25+j:len(inp):25*6] if val !=2) for j in range(25)) for i in range(6))

def part2_ocr(inp, *args, **kwargs):
    grid = [[inp[i*25+j:len(inp):25*6] for j in range(25)] for i in range(6)]
    out = []
    width = 50
    height = 12
    margin_width = 3
    margins = [(255,255,255)] * (margin_width * 2 + width)
    for _ in range(margin_width):
        out.append(margins)
    for row in grid:
        tmp = [(255,255,255)] * margin_width
        for vals in row:
            val = next((0,0,0) if val == 1 else (255,255,255) for val in vals if val != 2)
            tmp.extend([val] * (width // 25))
        tmp.extend([(255,255,255)] * margin_width)
        out.append(tmp * (height // 6))
    # print(out)
    for _ in range(margin_width):
        out.append(margins)
    # print(len(out), len(out[0]))
    im = Image.new('RGB', (width + 2 * margin_width, height + 2 * margin_width))
    im.putdata([k for row in out for k in row])
    im.convert('1').save("day8.png")
    proc = sp.Popen("tesseract day8.png stdout -l eng --oem 0 --psm 6", stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc.communicate()

def part2_letter(inp, *args, **kwargs):
    grid = [[inp[i*25+j:len(inp):25*6] for j in range(25)] for i in range(6)]
    out = [[] for _ in range(5)]
    for row in grid:
        tmp = []
        for i, vals in enumerate(row):
            val = next(val for val in vals if val != 2)
            tmp.append(val)
            if (i + 1) % 5 == 0:
                out[i // 5].append(tmp)
                tmp = []
    out_str = []
    for letter in out:
        letter = [list(k) for k in zip(*letter)]
        # print(letter)
        for k,v in letters.items():
            if letter == v:
                out_str.append(k)

    return ''.join(out_str)

if __name__ == "__main__":
    import sys
    inp = parse(sys.stdin.read())
    print(part1(inp.copy()))
    print("=========")
    print(part2(inp.copy()))