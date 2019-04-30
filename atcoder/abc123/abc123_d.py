X, Y, Z, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
C = [int(_) for _ in input().split()]

A = sorted(A)
B = sorted(B)
C = sorted(C)

maxn = A[0] * B[0] * C[0]

from heapq import *

h = []


heappush(h, (-A[-1] - B[-1] - C[-1], len(A) - 1, len(B) - 1, len(C) - 1))

used = {}

for i in range(min(K, X * Y * Z)):
    v, ix, iy, iz = heappop(h)
    print(-v)
    def push(x, y, z):
        if x >= 0 and y >= 0 and z >= 0 and (x, y, z) not in used:
            heappush(h, (-A[x] - B[y] - C[z], x, y, z))
            used[x, y, z] = 1
    push(ix - 1, iy, iz)
    push(ix, iy - 1, iz)
    push(ix, iy, iz - 1)

