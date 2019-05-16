N = int(input())
st = [[int(_) for _ in input().split()] for i in range(N)]

from collections import defaultdict

es = defaultdict(int)

for s, t in st:
    es[s] += 1
    es[t] -= 1

tes = [(t, es[t]) for t in sorted(es)]

x = 0
result = 0
for t, d in tes:
    if x == 0 and d > 0:
        result += 1
    x += d

print(result)
