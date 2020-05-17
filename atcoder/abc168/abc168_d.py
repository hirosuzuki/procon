N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(M)]

from collections import defaultdict
from heapq import *

def solve(N, M, AB):
    rs = defaultdict(set)
    for a, b in AB:
        rs[a].add(b)
        rs[b].add(a)
    h = []
    t = {1: 0}
    heappush(h, (0, 1))
    while h:
        d, x = heappop(h)
        for dx in rs[x]:
            if dx not in t:
                t[dx] = x
                heappush(h, (d + 1, dx))
    return t

result = solve(N, M, AB)

print("Yes")
for i in range(2, N + 1):
    print(result[i])
