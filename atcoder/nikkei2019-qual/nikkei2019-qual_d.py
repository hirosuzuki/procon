N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N - 1 + M)]

from collections import defaultdict
from heapq import *

vs = defaultdict(set)
ws = defaultdict(int)

for a, b in AB:
    vs[a].add(b)
    ws[b] += 1

for i in range(1, N + 1):
    if not ws[i]:
        root = i
        break

h = []

heappush(h, (0, root, 0))

rs = [-1] * (N + 1) 
ls = [0] * (N + 1)

rs[root] = 0

#print(vs)

while h:
    l, n, parent = heappop(h)
    #print("*", l, n, parent)
    for m in vs[n]:
        if ls[m] > l - 1:
            #print("+", l -1, m, n)
            ls[m] = l - 1
            prer = rs[m]
            if prer != n:
                rs[m] = n
                heappush(h, (l - 1, m, n))

for i in range(1, N + 1):
    print(rs[i])
