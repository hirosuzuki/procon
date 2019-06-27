H, W = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for i in range(H)]

A = [row + [0] for row in A] + [[0] * (W + 1)]

cs = [[0] * (W + 1) for i in range(H + 1)]

cells = [
    (A[y][x], x, y)
    for y in range(H)
    for x in range(W)
]

cells.sort(reverse=True)

result = 0

M = 10**9+7

for v, x, y in cells:
    r = 1
    if A[y+1][x] > v:
        r += cs[y+1][x]
    if A[y-1][x] > v:
        r += cs[y-1][x]
    if A[y][x+1] > v:
        r += cs[y][x+1]
    if A[y][x-1] > v:
        r += cs[y][x-1]
    cs[y][x] = r % M
    result = (result + r) % M

print(result)
