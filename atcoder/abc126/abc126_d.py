N = int(input())
uvw = [[int(_) for _ in input().split()] for i in range(N - 1)]

from collections import defaultdict

uv = defaultdict(dict)

for u, v, w in uvw:
    uv[u][v] = w
    uv[v][u] = w
    
l = {1: 0}

s = [1]

while s:
    ns = []
    for i in s:
        for j in uv[i]:
            if not j in l:
                l[j] = l[i] + uv[i][j]
                ns.append(j)
    s = ns

for i in range(1, N + 1):
    print(l[i] % 2)
