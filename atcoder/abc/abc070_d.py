N = int(input())
abc = [[int(_) for _ in input().split()] for i in range(N - 1)]
Q, K = [int(_) for _ in input().split()]
xy = [[int(_) for _ in input().split()] for i in range(Q)]

from collections import defaultdict
from heapq import *

V = list(range(1, N + 1))
E = defaultdict(lambda:{})
for a, b, c in abc:
    E[a][b] = c
    E[b][a] = c

def Dijkstra(s, V, E):
    # https://ja.wikipedia.org/wiki/%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95
    d = defaultdict(lambda:10**20)
    prev = defaultdict(lambda:None)
    d[s] = 0
    Q = []
    for v in V:
        heappush(Q, (d[v], v))
    while Q:
        x, u = heappop(Q)
        for v, y in E[u].items():
            alt = d[u] + y
            if d[v] > alt:
                d[v] = alt
                prev[v] = u
                heappush(Q, (alt, v))
    return d, prev

d, prev = Dijkstra(K, V, E)

for x, y in xy:
    print(d[x] + d[y])
