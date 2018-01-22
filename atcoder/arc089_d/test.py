from main import calc

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
    K2 = K * 2
    xys = [(x % K2, (y + c * K) % K2) for x, y, c in xyc]

    m = defaultdict(int)
    for x, y in xys:
        for j in range(K):
            for i in range(K):
                m[(x + i) % K2, (y + j) % K2] += 1

    rmax = 0
    for y in range(K2):
        for x in range(K2):
            rcount = m[x, y] + m[(x + K) % K2, (y + K) % K2]
            rmax = max(rmax, rcount)

    return rmax

def calc2(K, xyc):
    K2 = K * 2
    N = len(xyc)
    xys = [(x % K2, (y + c * K) % K2) for x, y, c in xyc]

    m = defaultdict(int)
    for x, y in xys:
        for j in range(K):
            for i in range(K):
                m[(x + i) % K2, (y + j) % K2] += 1
                m[(x + K + i) % K2, (y + K + j) % K2] += 1

    rmax = 0
    for y in range(K):
        for x in range(K):
            rcount = m[x, y]
            rmax = max(rmax, rcount, N - rcount)

    return rmax

def calc3(K, xyc):
    K2 = K * 2
    N = len(xyc)

    print("*1")
    m = defaultdict(int)
    for x, y, c in xyc:
        y += c * K
        x1, y1 = x % K2, y % K2
        x2, y2 = x1 + K, y1 + K
        m[x1, y1] += 1
        m[x2, y2] += 1
        m[x2, y1] -= 1
        m[x1, y2] -= 1
        x1, y1 = (x + K) % K2, (y + K) % K2
        x2, y2 = x1 + K, y1 + K
        m[x1, y1] += 1
        m[x2, y2] += 1
        m[x2, y1] -= 1
        m[x1, y2] -= 1

    print("*2")
    mt = defaultdict(int)
    for y in range(0, K2):
        for x in range(0, K2):
            mt[x, y] = m[x, y] + mt[x - 1, y] + mt[x, y - 1] - mt[x - 1, y - 1]

    print("*3")
    rmax = 0
    for y in range(K, K2):
        for x in range(K, K2):
            rcount = mt[x, y]
            rmax = max(rmax, rcount, N - rcount)

    return rmax

import random
N = 200
K = 10
xyc = [(random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000) % 2) for i in range(N)]

print(calc(K, xyc))
print(calc0(K, xyc))
