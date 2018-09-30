import sys

N = int(input())
XY = [[int(_) for _ in input().split()] for i in range(N)]

mc = [0, 0]
maxl = 0

for x, y in XY:
    l = abs(x) + abs(y)
    maxl = max(maxl, l)
    mc[l % 2] += 1

if mc[0] > 0 and mc[1] > 0:
    print(-1)
    sys.exit()

#if maxl > 20:
#    raise

def calc(sx, sy, dx, dy, d):
    #print("#", sx, sy, dx, dy)
    x = dx - sx
    y = dy - sy
    tx = x + 3 * d - y
    ty = x + 3 * d + y
    dirs = ("LL", "LD", "DD"), ("LU", "UD", "RD"), ("UU", "RU", "RR")
    ds = {"R": (+d, 0), "L": (-d, 0), "U": (0, +d), "D": (0, -d)}
    dir = dirs[ty // (2 * d)][tx // (2 * d)]
    ex, ey = sx, sy
    for d in dir:
        ex += ds[d][0]
        ey += ds[d][1]
    #print("*", dir, ex, ey)
    return dir, ex, ey


ds = []
ds0 = []

DM = 19

for i in range(DM):
    d = 3 ** (DM - i - 1)
    ds.append(d)
    ds0.append(d)
    ds0.append(d)

w0 = ""
x0, y0 = 0, 0

if mc[1] > 0:
    ds0 = [1] + ds0
    w0 += "R"
    x0 += 1

print(len(ds0))
print(*ds0)

for i in range(N):
    w = w0
    x, y = x0, y0
    for j, d in enumerate(ds):
        wc, x, y = calc(x, y, XY[i][0], XY[i][1], d)
        w += wc
    print(w)



