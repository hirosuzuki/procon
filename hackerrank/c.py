X1, Y1 = [int(_) for _ in input().split()]
X2, Y2 = [int(_) for _ in input().split()]
N = int(input())
AB = [tuple([int(_) for _ in input().split()]) for i in range(N)]

import heapq

def check(SX, SY, EX, EY, AB):
    h = []
    heapq.heappush(h, (0, SX, SY))
    pcell = {}
    pcell[SX, SY] = 0
    while h:
        n, bx, by = heapq.heappop(h)
        # print("-", n, bx, by)
        if bx == EX and by == EY:
            return 2
        if n >= 25:
            return 1
        for dx, dy in ((0, -1), (1, 0), (-1, 0), (0, 1)):
            x, y = bx + dx, by + dy
            if (x, y) in AB:
                continue
            if not (x, y) in pcell:
                heapq.heappush(h, (n + 1, x, y))
                pcell[x, y] = n + 1
    return 0
    

#print(AB)

r1 = check(X1, Y1, X2, Y2, AB)
r2 = check(X2, Y2, X1, Y1, AB)

if r1 == 2 or r2 == 2:
    print("Yes")
elif r1 == 0 or r2 == 0:
    print("No")
else:
    print("Yes")
