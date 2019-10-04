R, C = [int(_) for _ in input().split()]
SY, SX = [int(_) for _ in input().split()]
GY, GX = [int(_) for _ in input().split()]
S = [input() for i in range(R)]

cs = [list(row) for row in S]

from collections import deque

result = -1

q = deque([])
q.append((0, SX - 1, SY - 1))
while q:
    d, x, y = q.popleft()
    if x == GX - 1 and y == GY - 1:
        result = d
        break
    for dx, dy in ((0, -1), (0, +1), (-1, 0), (+1, 0)):
        nx, ny = x + dx, y + dy
        if cs[ny][nx] == ".":
            q.append((d + 1, nx, ny))
            cs[ny][nx] = d + 1

print(result)
