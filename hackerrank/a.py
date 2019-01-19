N, M = [int(_) for _ in input().split()]
S = [input() for i in range(N)]
for y, row in enumerate(S):
    x = row.find("S")
    if x >= 0:
        sx, sy = x, y
    x = row.find("G")
    if x >= 0:
        ex, ey = x, y

# print(sx, sy, ex, ey)
result = abs(ex - sx) + abs(ey - sy)

print(result)