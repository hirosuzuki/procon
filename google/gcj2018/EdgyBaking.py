import math

T = int(input())

def solve():
    N, P = [int(_) for _ in input().split()]
    WH = []
    for i in range(N):
        wh = [int(_) for _ in input().split()]
        WH.append(wh)
    r = 0
    ml = []
    dl = 0
    for w, h in WH:
        w, h = WH[0]
        r += w + h + w + h
        minl = min([w, h]) * 2
        maxl = math.sqrt(w*w+h*h) * 2
        ml.append(minl)
        dl += maxl - minl
    if r > P:
        return r
    ml.sort(reverse=True)
    print
    for x in ml:
        r = min(r, r + x)
    return min(P, r + dl)

for i in range(T):
    r = solve()
    print("Case #%d: %f" % (i + 1, r))