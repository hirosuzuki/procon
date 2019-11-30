N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N)]

from heapq import *

h = []

AB = sorted(AB)

result = 0
p = 0
for i in range(1, M + 1):
    while p < len(AB) and AB[p][0] <= i:
        heappush(h, -AB[p][1])
        p += 1
    if h:
        result -= heappop(h)
    
print(result)
