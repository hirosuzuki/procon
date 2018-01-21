def calc0(K, xyc):
    rmax = 0
    for i in range(K * 2):
        for j in range(K * 2):
            rcount = 0
            for x, y, c in xyc:
                rcount += ((x + j) // K + (y + i) // K) % 2 == c
            rmax = max(rmax, rcount)
    return rmax

def calc1(K, xyc):
    rmax = 0
    for i in range(K * 2):
        xs = [(x + c * K + (y + i) // K * K) % (2 * K) for x, y, c in xyc]
        for j in range(K * 2):
            rcount = 0
            for x in xs:
                rcount += ((x + j) // K)  % 2 == 1
            rmax = max(rmax, rcount)
    return rmax

def calc(K, xyc):
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

#import random
#N = 10000
#K = 20
#xyc = [(random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000) % 2) for i in range(N)]

N, K = [int(e) for e in input().split()]
xyc = [input().split() for i in range(N)]
xyc = [(int(x), int(y), c == "W") for x, y, c in xyc]

#print(calc0(K, xyc))
#print(calc1(K, xyc))
print(calc(K, xyc))

