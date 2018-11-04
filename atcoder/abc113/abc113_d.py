H, W, K = [int(_) for _ in input().split()]

MOD = 1000000007

P = [""]
for i in range(W - 1):
    Q = []
    for p in P:
        Q.append(p + "0")
        if len(p) == 0 or p[-1] == "0":
            Q.append(p + "1")
    P = Q

rs = [1] + [0] * (W - 1)

for j in range(H):
    nrs = [0] * W
    for p in P:
        drs = rs[:]
        for i, c in enumerate(p):
            if c == "1":
                drs[i], drs[i + 1] = drs[i + 1], drs[i]
        for i in range(W):
            nrs[i] = (nrs[i] + drs[i]) % MOD
    rs = nrs

print(rs[K - 1])
