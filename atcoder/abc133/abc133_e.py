N, K = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N - 1)]

from collections import defaultdict

v = defaultdict(set)

for a, b in AB:
    v[a].add(b)
    v[b].add(a)

M = 10**9+7

import sys
sys.setrecursionlimit(100001)

result = 1

def check(n, b, p):
    global result
    result = result * max(K - b - p, 0) % M
    #print("check:", n, r[n])
    np = min(p + 1, 2)
    for b, x in enumerate(v[n]):
        v[x].remove(n)
        check(x, b, np)

check(1, 0, 0)

print(result)
