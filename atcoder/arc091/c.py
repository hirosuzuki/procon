
def calc0(N, M):
    cell = [[0 for i in range(M)] for j in range(N)]
    for i in range(M):
        for j in range(N):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    xx = i + x
                    yy = j + y
                    if 0 <= xx < M and 0 <= yy < N:
                        cell[yy][xx] ^= 1
    r = 0
    for i in range(M):
        for j in range(N):
            if cell[j][i]:
                r += 1
    return r
    
def calc(N, M):
    if N == 1 and M == 1:
        return 1
    if N >= 2 and M >= 2:
        return (N - 2) * (M - 2)
    if N == 1:
        return M - 2
    return N - 2

N, M = [int(_) for _ in input().split()]

print(calc(N, M))

