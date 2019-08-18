N = int(input())
A = [int(input()) for i in range(N)]

from collections import defaultdict

cs = defaultdict(int)

for a in A:
    cs[a] += 1

result = 0
for v in cs.values():
    result += v - 1

print(result)
