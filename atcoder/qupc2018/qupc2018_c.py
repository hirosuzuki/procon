H, W, X = [int(_) for _ in input().split()]
S = [input() for i in range(H)]

M = [[0] * W + [-1] for j in range(H)]
M.append([-1] * (W + 1))

from heapq import *

h = []

for y, r in enumerate(S):
    for x, c in enumerate(r):
        if c == "#":
            M[y][x] = 1
        elif c == "@":
            heappush(h, (-X - 1, x, y))
            M[y][x] = 1
        elif c == "S":
            sx, sy = x, y
        elif c == "G":
            gx, gy = x, y

dlist = (0, -1), (+1, 0), (0, +1), (-1, 0)

while h:
    w, x, y = heappop(h)
    M[y][x] = w
    if w < -1:
        for dx, dy in dlist:
            nx, ny = x + dx, y + dy
            if M[ny][nx] == 0:
                heappush(h, (w + 1, nx, ny))

h = []
heappush(h, (0, sx, sy))

result = -1

while h:
    w, x, y = heappop(h)
    M[y][x] = w + 1
    if x == gx and y == gy:
        result = w
        break
    for dx, dy in dlist:
        nx, ny = x + dx, y + dy
        if M[ny][nx] == 0:
            heappush(h, (w + 1, nx, ny))

print(result)


