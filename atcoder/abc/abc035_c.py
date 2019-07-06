N, Q = [int(_) for _ in input().split()]
LR = [[int(_) for _ in input().split()] for i in range(Q)]

cs = [0] * (N + 2)

for l, r in LR:
    cs[l] += 1
    cs[r + 1] -= 1

from itertools import accumulate

b = "".join("01"[x % 2] for x in accumulate(cs))

print(b[1:-1])