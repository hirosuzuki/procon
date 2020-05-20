N = int(input())
AB = [[int(_) for _ in input().split()] for i in range(N)]

AB.sort()

from heapq import *

m = 0
h = []
result = 0

for k in range(1, N + 1):
    while m < N and AB[m][0] <= k:
        heappush(h, -AB[m][1])
        m += 1
    r = heappop(h)
    result += -r
    print(result)