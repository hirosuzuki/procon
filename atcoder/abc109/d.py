H, W = [int(_) for _ in input().split()]
a = [[int(_) for _ in input().split()] for i in range(H)]

x, y = 0, 0

result = []

while 1:
    if y % 2 == 0:
        if x < W - 1:
            dx, dy = 1, 0
        else:
            dx, dy = 0, 1
    else:
        if x > 0:
            dx, dy = -1, 0
        else:
            dx, dy = 0, 1
    tx, ty = x + dx, y + dy
    if ty >= H:
        break
    v = a[y][x]
    if v % 2 == 1:
        a[y][x] = 0
        a[ty][tx] += v
        result.append((y+1, x+1, ty+1, tx+1))
    x, y = tx, ty

print(len(result))
for r in result:
    print(*r)
