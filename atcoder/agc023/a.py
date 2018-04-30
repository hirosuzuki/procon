N = int(input())
A = [int(_) for _ in input().split()]

import itertools

ts = list(itertools.accumulate(A))

cs = {0: 1}
for t in ts:
    cs[t] = cs.get(t, 0) + 1

r = 0
for c in cs:
    n = cs[c]
    r += n * (n - 1) // 2

print(r)

