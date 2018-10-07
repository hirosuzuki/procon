N = int(input())
XYH = [[int(_) for _ in input().split()] for i in range(N)]

W = 101

cs = [[0] * W for i in range(W)]

XYH.sort(key=lambda e:e[2], reverse=True)

h = XYH[0][2]
sx, sy = XYH[0][0:2]
for x in range(W):
    for y in range(W):
        cs[y][x] = h + abs(x - sx) + abs(y - sy)

#print(cs)

for i in range(1, N):
    h = XYH[i][2]
    sx, sy = XYH[i][0:2]
    for x in range(W):
        for y in range(W):
            h1 = h + abs(x - sx) + abs(y - sy)
            if h > 0:
                if cs[y][x] != h1:
                    cs[y][x] = 0
            else:
                if cs[y][x] > h1:
                    cs[y][x] = 0
    #print(cs)

cx, cy, ch = 0, 0, 0

for x in range(W):
    for y in range(W):
        h = cs[y][x]
        if h > 0:
            cx, cy, ch = x, y, h

print(cx, cy, ch)
