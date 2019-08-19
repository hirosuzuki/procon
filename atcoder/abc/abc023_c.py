R, C, K = [int(_) for _ in input().split()]
N = int(input())
RC = [[int(_) for _ in input().split()] for i in range(N)]

def solve_small():
    cell = [[0] * (R + 1) for i in range(C + 1)]
    for r, c in RC:
        for i in range(1, R + 1):
            cell[c][i] += 1
        for i in range(1, C + 1):
            cell[i][r] += 1
        cell[c][r] -= 1
    result = 0
    for c in range(1, C + 1):
        for r in range(1, R + 1):
            if cell[c][r] == K:
                result += 1
    return result

from collections import defaultdict

def solve():
    rs = [0] * (R + 1)
    cs = [0] * (C + 1)

    for r, c in RC:
        rs[r] += 1
        cs[c] += 1

    csc = defaultdict(int)
    for i in range(1, C + 1):
        csc[cs[i]] += 1

    result = 0
    for i in range(1, R + 1):
        result += csc[K - rs[i]]

    for r, c in RC:
        x = rs[r] + cs[c]
        if x == K:
            result -= 1
        if x == K + 1:
            result += 1

    return result

print(solve())
