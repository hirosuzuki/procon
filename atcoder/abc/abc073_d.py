N, M, R = [int(_) for _ in input().split()]
r = [int(_) - 1 for _ in input().split()]

from collections import defaultdict
from itertools import permutations

INF = 10**10

D = [[INF] * N for _ in range(N)]

for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    D[a-1][b-1] = c
    D[b-1][a-1] = c

result = INF

# warshall_floyd
for i in range(N):
    for j in range(N):
        for k in range(N):
            D[j][k] = min(D[j][k], D[j][i] + D[i][k])

for xs in permutations(r):
    r = 0
    for i in range(R - 1):
        st, ed = xs[i], xs[i + 1]
        r += D[st][ed]
    result = min(result, r)

print(result)
