N = int(input())
WH = [tuple([int(_) for _ in input().split()]) for i in range(N)]

WH.sort(key=lambda x:(x[0],-x[1]))

from bisect import *

L = []

for w, h in WH:
    i = bisect_left(L, h)
    if i >= len(L):
        L.append(h)
    else:
        L[i] = h

print(len(L))
