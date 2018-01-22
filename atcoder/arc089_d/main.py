from collections import defaultdict

def calc(K, xyc):
    K2 = K * 2
    N = len(xyc)

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

    ms = [[0] * (K2 + 1) for i in range(K2 + 1)]
    for y in range(0, K2):
        ms0 = ms[y]
        ms1 = ms[y - 1]
        for x in range(0, K2):
            ms0[x] = m[x, y] + ms0[x-1] + ms1[x] - ms1[x-1]
    
    rmax = 0
    for y in range(K, K2):
        for x in range(K, K2):
            rcount = ms[y][x]
            rmax = max(rmax, rcount, N - rcount)

    return rmax

if __name__ == '__main__':
    N, K = [int(e) for e in input().split()]
    xyc = [(int(x), int(y), c == "W") for x, y, c in [input().split() for i in range(N)]]
    print(calc(K, xyc))
