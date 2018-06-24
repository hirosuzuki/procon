N = int(input())
xy = [[int(_) for _ in input().split()] for i in range(N)]

xsort_n = sorted(range(N), key=lambda n:xy[n][0])
ysort_n = sorted(range(N), key=lambda n:xy[n][1])

from collections import defaultdict

neighbors = defaultdict(list)

for i in range(N - 1):
    x1 = xsort_n[i]
    x2 = xsort_n[i+1]
    xd = xy[x2][0] - xy[x1][0]
    y1 = ysort_n[i]
    y2 = ysort_n[i+1]
    yd = xy[y2][1] - xy[y1][1]
    neighbors[x1].append((x2, xd))
    neighbors[x2].append((x1, xd))
    neighbors[y1].append((y2, yd))
    neighbors[y2].append((y1, yd))

from heapq import *

isused = [0] * N

h = []

heappush(h, (0, 0))

result = 0

while h:
    d, n = heappop(h)
    if isused[n]:
        continue
    result += d
    isused[n] = 1
    for ni, nd in neighbors[n]:
        if not isused[ni]:
            heappush(h, (nd, ni))
    
print(result)
