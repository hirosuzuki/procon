N, M, Q = [int(_) for _ in input().split()]
LR = [[int(_) for _ in input().split()] for i in range(M)]
PQ = [[int(_) for _ in input().split()] for i in range(Q)]

x = [[0] * (N+1) for i in range(N+1)]
for l, r in LR:
    x[l][r] += 1

from itertools import accumulate

t = [list(accumulate(row)) for row in x]
s = [list(accumulate(row)) for row in zip(*t)]

for p, q in PQ:
    result = s[q][q] -s[q][p-1] - s[p-1][q] + s[p-1][p-1]
    print(result)
