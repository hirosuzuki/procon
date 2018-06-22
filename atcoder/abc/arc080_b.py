H, W = [int(_) for _ in input().split()]
N = int(input())
A = [int(_) for _ in input().split()]

rows = [[0] * W for i in range(H)]

x, y, d = 0, 0, 1
for c, a in enumerate(A):
    for i in range(a):
        rows[y][x] = c + 1
        x += d
        if x < 0 or x >= W:
            d = -d
            x += d
            y += 1

for row in rows:
    print(*row)