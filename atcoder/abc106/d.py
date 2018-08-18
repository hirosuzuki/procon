N, M, Q = [int(_) for _ in input().split()]
LR = [[int(_) for _ in input().split()] for i in range(M)]
PQ = [[int(_) for _ in input().split()] for i in range(Q)]

from collections import defaultdict
from itertools import accumulate

C = [[0]*(N+1) for i in range(N+2)]

for l, r in LR:
    C[1][r] += 1
    C[l + 1][r] -= 1

#print(C)

T = [list(accumulate(row)) for row in C]
T = [list(accumulate(row)) for row in zip(*T)]

#print(T)

for p, q in PQ:
    print(T[q][p])
