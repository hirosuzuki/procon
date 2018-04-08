
from heapq import *

def calc(s):
    x = 0
    p = 1
    for c in s:
        if c == "S":
            x += p
        elif c == "C":
            p += p
    return x

def solve(n, D, P):
    h = []
    heappush(h, (0, P))
    while h:
        xn, xs = heappop(h)
        # print(xn, xs)
        xp = calc(xs)
        if xp <= D:
            print("Case #%d:" % n, xn)
            return
        for i in range(len(xs) - 1):
            if xs[i: i + 2] == "CS":
                nxs = xs[:i] + "SC" + xs[i+2:]
                heappush(h, (xn + 1, nxs))
    print("Case #%d:" % n, "IMPOSSIBLE")


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        vs = input().split()
        D = int(vs[0])
        P = vs[1]
        solve(i + 1, D, P)
