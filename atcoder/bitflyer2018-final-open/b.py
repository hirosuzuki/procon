N, Q = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]
CD = [[int(_) for _ in input().split()] for i in range(Q)]

from bisect import *
from itertools import accumulate

def solve0():
    for c, d in CD:
        r = 0
        for x in X:
            r += min(d, abs(x - c))
        print(r)

def solve():
    ax = list(accumulate(X)) + [0]
    for c, d in CD:
        i1 = bisect_left(X, c - d)
        i2 = bisect_left(X, c)
        i3 = bisect_left(X, c + d)
        lsum = ax[i2-1] - ax[i1-1]
        rsum = ax[i3-1] - ax[i2-1]
        r = (i2-i1)*c - lsum + rsum - (i3-i2)*c + i1 * d + (N - i3) * d
        print(r)
        
solve()
