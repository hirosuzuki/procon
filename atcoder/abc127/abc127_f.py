Q = int(input())

from heapq import *

lows = []
highs = []

a = []
b = 0
r = 0

for i in range(Q):
    vs = [int(_) for _ in input().split()]
    if vs[0] == 1:
        b += vs[2]
        if not lows:
            x = vs[1]
            heappush(lows, -x)
        else:
            r += abs(vs[1] + lows[0])
            if vs[1] <= -lows[0]:
                heappush(lows, -vs[1])
            else:
                heappush(highs, vs[1])

        if len(lows) < len(highs):
            x = heappop(highs)
            y = -lows[0]
            r += y - x
            heappush(lows, -x)
        elif len(lows) > len(highs) + 1:
            x = -heappop(lows)
            y = highs[0] if len(highs) else 0
            heappush(highs, x)
            # r += x - y

        # print("center", -lows[0], r, lows, highs)

    else:
        print(-lows[0], r + b)
