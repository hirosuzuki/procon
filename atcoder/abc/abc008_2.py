N = int(input())
S = [input() for i in range(N)]

from collections import Counter

cs = Counter(S)

ss = sorted(cs.keys(), key=lambda x:cs[x])

result = ss[-1]

print(result)
