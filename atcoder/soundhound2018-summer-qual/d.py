
from heapq import *
from collections import defaultdict

def Dijkstra(s, N, E):
    # https://ja.wikipedia.org/wiki/%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95
    d = [10**30] * (N + 1)
    d[s] = 0
    Q = []
    for v in range(1, N + 1):
        heappush(Q, (d[v], v))
    while Q:
        x, u = heappop(Q)
        for v, y in E[u].items():
            alt = d[u] + y
            if d[v] > alt:
                d[v] = alt
                heappush(Q, (alt, v))
    return d

N, M, S, T = [int(_) for _ in input().split()]
UVAB = [[int(_) for _ in input().split()] for i in range(M)]

Ea = defaultdict(dict)
Eb = defaultdict(dict)

for u, v, a, b in UVAB:
    Ea[u][v] = a
    Ea[v][u] = a
    Eb[u][v] = b
    Eb[v][u] = b
    
Da = Dijkstra(S, N, Ea)
Db = Dijkstra(T, N, Eb)

T = [None] * (N + 1)
t = 10**30

for i in range(N, 0, -1):
    r = Da[i] + Db[i]
    t = min(t, r)
    T[i] = t

ST = 10**15

for i in range(1, N + 1):
    print(ST-T[i])
