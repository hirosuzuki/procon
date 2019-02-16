N, M = [int(_) for _ in input().split()]
KA = [[int(_) for _ in input().split()] for i in range(N)]

from collections import defaultdict

cs = defaultdict(int)

for r in KA:
    for n in r[1:]:
        cs[n] += 1

result = sum([cs[k] == N for k in cs])

print(result)
