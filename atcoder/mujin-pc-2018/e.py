N, M, K = [int(_) for _ in input().split()]
D = input()
S = [input() + "#" for i in range(N)]
S.append("#" * (M+1))

from heapq import *

h = []

for y, row in enumerate(S):
    for x, c in enumerate(row):
        if c == "S":
            sx, sy = x, y
        if c == "G":
            gx, gy = x, y

INF = 10**12

dts = [(INF,INF,INF,INF)] * K

Ut, Dt, Lt, Rt = INF, INF, INF, INF
for i in range(K - 1, -1, -1):
    c = D[i]
    if c == "U":
        Ut = 0
    if c == "D":
        Dt = 0
    if c == "L":
        Lt = 0
    if c == "R":
        Rt = 0
    Ut += 1
    Dt += 1
    Lt += 1
    Rt += 1
for i in range(K- 1, -1, -1):
    c = D[i]
    if c == "U":
        Ut = 0
    if c == "D":
        Dt = 0
    if c == "L":
        Lt = 0
    if c == "R":
        Rt = 0
    Ut += 1
    Dt += 1
    Lt += 1
    Rt += 1
    dts[i] = (Ut, Dt, Lt, Rt)

#print(dts)

heappush(h, (0, sx, sy))

result = -1

mint = [[INF] * M for i in range(N)]

while h:
    t, x, y = heappop(h)
    if t >= INF:
        break
    mint[y][x] = t
    if x == gx and y == gy:
        result = t
        break
    dt = dts[t % K]
    tt = dt[0]+t
    if S[y-1][x] != "#" and mint[y-1][x] > tt:
        heappush(h, (tt, x, y-1))
    tt = dt[1]+t
    if S[y+1][x] != "#" and mint[y+1][x] > tt:
        heappush(h, (tt, x, y+1))
    tt = dt[2]+t
    if S[y][x-1] != "#" and mint[y][x-1] > tt:
        heappush(h, (tt, x-1, y))
    tt = dt[3]+t
    if S[y][x+1] != "#" and mint[y][x+1] > tt:
        heappush(h, (tt, x+1, y))

print(result)
