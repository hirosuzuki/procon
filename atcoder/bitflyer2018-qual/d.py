H, W = [int(_) for _ in input().split()]
N, M = [int(_) for _ in input().split()]

A = [input() for i in range(N)]

d = [int(row.replace("#", "1").replace(".", "0"), 2) for row in A]

tN, tM = min(N * 2, H), min(M * 2, W)
for i in range(M, tM):
    d = [x | x << 1 for x in d]

for i in range(N, tN):
    r = 0
    e = []
    for x in d:
        e.append(x | r)
        r = x
    e.append(r)
    d = e

def numbit(x):
    r = 0
    while x:
        r += x & 1
        x >>= 1
    return r

bits = [numbit(x) for x in d]

if W > tM:
    bits = [x + (W - tM) * (x > 0) for x in bits]

r = sum(bits)

if H > tN:
    r += (H - tN) * bits[len(bits)//2]
    
print(r)
