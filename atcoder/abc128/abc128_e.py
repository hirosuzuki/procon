N, Q = [int(_) for _ in input().split()]
STX = [[int(_) for _ in input().split()] for i in range(N)]
D = [int(input()) for i in range(Q)]

from bisect import *

result = {}

STX = sorted(STX, key=lambda x:x[2])
ds = D[:]

for s, t, x in STX:
    t1 = s - .5 - x
    t2 = t - .5 - x
    p1 = bisect_left(ds, t1)
    p2 = bisect_left(ds, t2)
    #print(p1, p2, t1, t2, ds[p1:p2])
    for d in ds[p1:p2]:
        result[d] = x
    ds = ds[:p1] + ds[p2:]

#print(result)

for d in D:
    print(result.get(d, -1))
