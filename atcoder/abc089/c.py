from collections import Counter
from itertools import combinations

N = int(input())
S = [input() for i in range(N)]

xs = Counter(s[0] for s in S)

print(sum(xs[a] * xs[b] * xs[c] for a, b, c in combinations("MARCH", 3)))
