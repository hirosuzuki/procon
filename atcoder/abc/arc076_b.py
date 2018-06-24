N = int(input())
xy = [[int(_) for _ in input().split()] for i in range(N)]

xsort_n = sorted(range(N), key=lambda n:xy[n][0])
ysort_n = sorted(range(N), key=lambda n:xy[n][1])

from collections import defaultdict

neighbors = defaultdict(list)

for i in range(N - 1):
    x1 = xsort_n[i]
    x2 = xsort_n[i+1]
    y1 = ysort_n[i]
    y2 = ysort_n[i+1]
    neighbors[x1].append(x2)
    neighbors[x2].append(x1)
    neighbors[y1].append(y2)
    neighbors[y2].append(y1)

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
    for i in neighbors[n]:
        if not isused[i]:
            d1 = min(abs(xy[n][0] - xy[i][0]), abs(xy[n][1] - xy[i][1]))
            heappush(h, (d1, i))
    
print(result)
