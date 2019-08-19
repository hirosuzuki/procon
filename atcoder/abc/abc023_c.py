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

def solve():
    rs = [0] * (R + 1)
    cs = [0] * (C + 1)

    for r, c in RC:
        rs[r] += 1
        cs[c] += 1

    return

print(solve_small())
