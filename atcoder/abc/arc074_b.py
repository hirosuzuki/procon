N = int(input())
A = [int(_) for _ in input().split()]

from heapq import *

L = [0] * (N + 1)

t = 0
h = []
for a in A[:N]:
    heappush(h, a)
    t += a

L[0] = t
for i in range(N):
    x = A[N + i]
    heappush(h, x)
    y = heappop(h)
    t += x - y
    L[i + 1] = t

R = [0] * (N + 1)

t = 0
h = []
for a in A[N * 2:]:
    heappush(h, -a)
    t -= a

R[N] = t
for i in range(N - 1, -1, -1):
    x = A[N + i]
    heappush(h, -x)
    y = heappop(h)
    t += -x - y
    R[i] = t

result = max(l + r for l, r in zip(L, R))

print(result)