H, W, K = [int(_) for _ in input().split()]

MOD = 1000000007

pats = [[0]]

for i in range(1, W):
    pats = [p + [i] for p in pats] + [p[:-1] + [i, i - 1] for p in pats if p[-1] == i - 1]

rs = [1] + [0] * (W - 1)

for j in range(H):
    rs = [sum(rs[p[i]] for p in pats) % MOD for i in range(W)]

print(rs[K - 1])
