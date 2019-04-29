T = int(input())

from itertools import accumulate

def solve(P, Q, vs):
    xds = [0] * (Q + 2)
    yds = [0] * (Q + 2)
    for x, y, d in vs:
        #print(x, y, d)
        if d == "N":
            yds[y + 1] += 1
            yds[Q + 1] -= 1
        elif d == "S":
            yds[0] += 1
            yds[y] -= 1
        elif d == "E":
            xds[x + 1] += 1
            xds[Q + 1] -= 1
        elif d == "W":
            xds[0] += 1
            xds[x] -= 1
    #print(xds)
    #print(yds)

    resultx = 0
    xvmax = xv = xds[resultx]
    for i in range(1, Q + 1):
        xv += xds[i]
        if xv > xvmax:
            xvmax = xv
            resultx = i

    resulty = 0
    yvmax = yv = xds[resulty]
    for i in range(1, Q + 1):
        yv += yds[i]
        if yv > yvmax:
            yvmax = yv
            resulty = i

    return resultx, resulty

for t in range(1, T + 1):
    P, Q = [int(_) for _ in input().split()]
    vs = []
    for i in range(P):
        x = input().split()
        vs.append((int(x[0]), int(x[1]), x[2]))
    result = solve(P, Q, vs)
    print("Case #%d:" % t, *result)
