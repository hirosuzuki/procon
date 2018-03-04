from collections import defaultdict
from itertools import combinations

N = int(input())
S = [input() for i in range(N)]

CHARS = "MARCH"

xs = defaultdict(int)

for s in S:
    xs[s[0]] += 1

def calc(xs):
    return sum(xs[a] * xs[b] * xs[c] for a, b, c in combinations(CHARS, 3))

print(calc(xs))
