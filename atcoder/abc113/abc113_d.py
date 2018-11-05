H, W, K = [int(_) for _ in input().split()]

MOD = 1000000007

pats = [""]

for i in range(W - 1):
    pats = [p + "0" for p in pats] + [p + "1" for p in pats if not p.endswith("1")]

rs = [1] + [0] * (W - 1)

for j in range(H):
    nrs = [0] * W
    for p in pats:
        drs = rs[:]
        for i, c in enumerate(p):
            if c == "1":
                drs[i], drs[i + 1] = drs[i + 1], drs[i]
        for i in range(W):
            nrs[i] = (nrs[i] + drs[i]) 
    rs = nrs

print(rs[K - 1] % MOD)
