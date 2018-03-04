H, W, D = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for i in range(H)]
Q = int(input())
LR = [[int(_) for _ in input().split()] for i in range(Q)]

pos = {}
for i, row in enumerate(A):
    for j, x in enumerate(row):
        pos[x] = (i, j)

dt = [0] * (H * W + 1)
for x in range(D + 1, H * W + 1):
    y = x - D
    p1, p2 = pos[x], pos[y]
    dt[x] = dt[y] + abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for l, r in LR:
    print(dt[r] - dt[l])
