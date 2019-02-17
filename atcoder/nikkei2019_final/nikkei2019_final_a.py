N = int(input())
A = [int(_) for _ in input().split()]

from itertools import accumulate

ts = list(accumulate(A)) + [0]

for k in range(N):
    r = max(ts[i + k] - ts[i - 1] for i in range(N - k))
    print(r)
