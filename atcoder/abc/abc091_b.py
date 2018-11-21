N = int(input())
S = [input() for i in range(N)]
M = int(input())
T = [input() for i in range(M)]

from collections import Counter

sc = Counter(S)
tc = Counter(T)

result = max(0, max(sc[k] - tc[k] for k in sc))

print(result)
