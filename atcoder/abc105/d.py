N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

from collections import defaultdict

ts = defaultdict(int)

ts[0] = 1

t = 0
for a in A:
    t = (t + a) % M
    ts[t] += 1

result = 0

for k, v in ts.items():
    result += v * (v - 1) // 2

print(result)

