def solve(M, RR, G):
    RR = [(0, 0)] + RR
    G = [0] + G
    def create(n, ds):
        if G[RR[n][0]] <= 0:
            if RR[n][0] in ds: return False
            if not create(RR[n][0], ds + [RR[n][0]]): return False
        if G[RR[n][1]] <= 0:
            if RR[n][1] in ds: return False
            if not create(RR[n][1], ds + [RR[n][1]]): return False
        if G[RR[n][0]] <= 0:
            return False
        if G[RR[n][1]] <= 0:
            return False
        if RR[n][0] in ds: return False
        if RR[n][1] in ds: return False
        G[n] += 1
        G[RR[n][0]] -= 1
        G[RR[n][1]] -= 1
        return True

    while 1:
        if not create(1, [1]):
            break
    return G[1]

T = int(input())
for i in range(T):
    M = int(input())
    RR = [[int(_) for _ in input().split()] for j in range(M)]
    G = [int(_) for _ in input().split()]
    print("Case #%d:" % (i + 1), solve(M, RR, G))
