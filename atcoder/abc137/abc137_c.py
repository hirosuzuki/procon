N = int(input())
S = [input() for i in range(N)]

from collections import Counter

cs = Counter(["".join(sorted(_)) for _ in S])

result = 0
for c, n in cs.items():
    result += n * (n - 1) // 2

print(result)
