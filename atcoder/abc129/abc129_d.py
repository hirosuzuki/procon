H, W = [int(_) for _ in input().split()]
S = [input() + "#" for i in range(H)] + ["#" * (W + 1)]

from itertools import accumulate

rxs = []

for row in S:
    si = -1
    xs = [0] * (W + 1)
    for i in range(W + 1):
        if row[i] == "#":
            xs[si + 1] += (i - si - 1)
            xs[i] -= (i - si - 1)
            si = i
    rxs.append(list(accumulate(xs)))

sxs = []


for row in zip(*S):
    si = -1
    xs = [0] * (H + 1)
    for i in range(H + 1):
        if row[i] == "#":
            xs[si + 1] += (i - si - 1)
            xs[i] -= (i - si - 1)
            si = i
    sxs.append(list(accumulate(xs)))

result = 0

for r1, r2 in zip(rxs, zip(*sxs)):
    r = max(c1 + c2 for c1, c2 in zip(r1, r2)) - 1
    result = max(result, r)

print(result)
