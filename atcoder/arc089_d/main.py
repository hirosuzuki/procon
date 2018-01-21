def calc2(K, xyc):
    rmax = 0
    for i in range(K):
        ts = [0 for x in range(K * 2)]
        for x, y, c in xyc:
            a = (x + c * K + (y + i) // K * K) % (2 * K)
            ts[a] += 1
        rcount = sum(ts[0:K])
        for j in range(K):
            rcount += -ts[j] + ts[j+K]
            rmax = max(rmax, rcount, N - rcount)
    return rmax

def calc(K, xyc):
    K2 = K * 2
    xys = [((x + c * K) % K2, y % K2) for x, y, c in xyc]
    m = {}
    for x in range(K2):
        for y in range(K2):
            m[x, y] = 0
    rcount0 = 0
    for x, y in xys:
        x1, y1 = x % K2, y % K2
        x2, y2 = (x + K) % K2, (y + K) % K2
        m[x1, y1] -= 1
        m[x2, y2] -= 1
        m[x1, y2] += 1
        m[x2, y1] += 1
        if (x1 // K + y1 // K) % 2 == 0:
            rcount0 += 1
    print(rcount0)
    rmax = rcount0
    for y in range(K + 1):
        rcount = rcount0
        rmax = max(rmax, rcount, N - rcount)
        for x in range(K):
            rcount += m[x, y]
            rmax = max(rmax, rcount, N - rcount)
        rcount0 += m[0, y]
    return rmax

import random
N = 20
K = 3
xyc = [(random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000) % 2) for i in range(N)]

#N, K = [int(e) for e in input().split()]
#xyc = [input().split() for i in range(N)]
#xyc = [(int(x), int(y), c == "W") for x, y, c in xyc]

print(calc2(K, xyc))
print(calc(K, xyc))

