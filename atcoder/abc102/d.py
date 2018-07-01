N = int(input())
A = [int(_) for _ in input().split()]

from itertools import accumulate
from bisect import bisect_left, bisect_right

ts = list(accumulate(A)) + [0]

r = 0

def calc(st, ed):
    t0 = ts[ed-1] - ts[st-1]
    i1 = bisect_left(ts, (ts[ed-1] + ts[st-1]) / 2, st + 1, ed - 1)
    t11 = ts[i1-1] - ts[st-1]
    t12 = t0 - t11
    t21 = ts[i1] - ts[st-1]
    t22 = t0 - t21
    #print("*", st, ed, t0, i1, t11, t12, t21, t22)
    if abs(t22-t21) > abs(t12-t11):
        return t11, t12
    else:
        return t21, t22

result = 999999999999999999999999
for i in range(2, N-1):
    r1, r2 = calc(0, i)
    r3, r4 = calc(i, N)
    #print(r1, r2, r3, r4)
    r = max(r1, r2, r3, r4) - min(r1, r2, r3, r4)
    result = min(result, r)

print(result)
