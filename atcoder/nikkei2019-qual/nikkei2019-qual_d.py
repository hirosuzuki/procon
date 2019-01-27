N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N - 1 + M)]

import sys
sys.setrecursionlimit(200000)

from collections import defaultdict

vs = defaultdict(set)
ws = defaultdict(set)

for a, b in AB:
    vs[a].add(b)
    ws[b].add(a)

#print(vs)
#print(ws)

L = []

cs = [0] * (1 + N)

def visit(n):
    if cs[n] == 1:
        return
    elif cs[n] == 0:
        cs[n] = 1
        for m in vs[n]:
            visit(m)
        cs[n] = 2
        L.append(n)

for n in range(1, N + 1):
    if cs[n] == 0:
        visit(n)

#print(L)

nrank = {}

for r, n in enumerate(L):
    nrank[n] = r

#print(nrank)

for n in range(1, N + 1):
    r = 0
    if ws[n]:
        r = sorted(ws[n], key=lambda x:nrank[x])[0]
    print(r)
