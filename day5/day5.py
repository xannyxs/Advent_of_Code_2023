import re
from typing import Tuple


def sol1(seeds: str, blocks: list[str]) -> int:
    inputs = list(map(int, re.findall(r'\d+', seeds)))

    for block in blocks:
        ranges = [list(map(int, line.split()))
                  for line in block.splitlines()[1:]]
        new_inputs = []
        for x in inputs:
            for a, b, c in ranges:
                if b <= x < b + c:
                    new_inputs.append(x - b + a)
                    break
            else:
                new_inputs.append(x)
        inputs = new_inputs

    return min(inputs)


def sol2(temp: str, blocks: list[str]) -> int:
    inputs = list(map(int, temp.split(":")[1].split()))
    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in ranges:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                new.append((s, e))
        seeds = new

    return min(seeds)[0]


def day5(lines: list[str]) -> Tuple[int, int]:
    seeds, *blocks = open('./day5/input.txt').read().split('\n\n')
    return sol1(seeds, blocks), sol2(seeds, blocks)
