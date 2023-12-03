from typing import Set, Tuple


def sol1(grid: list[str]) -> int:
    cs = set()

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == '.':
                continue

            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if cr < 0 or cr > len(grid) or cc < 0 or cc > len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))

    ns: list[int] = []

    for cr, cc in cs:
        s = ''
        while cc < len(grid[cr]) and grid[cr][cc].isdigit():
            s += grid[cr][cc]
            cc += 1
        ns.append(int(s))

    return sum(ns)


def sol2(grid: list[str]) -> int:
    totalAmount2 = 0

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != '*':
                continue

            cs = set()

            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if cr < 0 or cr > len(grid) or cc < 0 or cc > len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))

            if len(cs) != 2:
                continue

            ns: list[int] = []

            for cr, cc in cs:
                s = ''
                while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                    s += grid[cr][cc]
                    cc += 1
                ns.append(int(s))

            totalAmount2 += ns[0] * ns[1]

    return totalAmount2


def day3(lines: list[str]) -> Tuple[int, int]:
    grid = open('./day3/input.txt').read().splitlines()

    return sol1(grid), sol2(grid)
