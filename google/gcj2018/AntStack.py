def calc1(N, W):
    import sys
    sys.setrecursionlimit(10000)
    counter = 0
    def f(n, maxw, cache={}):
        nonlocal counter
        counter += 1
        if maxw <= 0:
            return 0
        if n == 1:
            if W[0] <= maxw:
                return 1
            else:
                return 0
        key = (n, maxw)
        if key in cache:
            return cache[key]
        r1 = f(n - 1, min(W[n - 1] * 6, maxw - W[n - 1]))
        r2 = f(n - 1, maxw)
        r = max(r1 + 1, r2)
        cache[key] = r
        return r
    r = f(N, 10**20)
    return r

def calc(N, W):
    r = {0: 0}
    for w in W:
        rs = list(r.items())
        for i, x in rs:
            if x <= w * 6:
                if (not (i + 1) in r) or (r[i + 1] > x + w):
                    r[i + 1] = x + w
    return max(r.keys())

def solve():
    N = int(input())
    W = [int(_) for _ in input().split()]
    if N > 100:
        return 0
    return calc(N, W)

"""
import random
N = 100
W = [random.randint(1, 1000) for i in range(N)]
print(calc(N, W))
raise
"""

T = int(input())

for i in range(T):
    r = solve()
    print("Case #%d: %s" % (i + 1, r))