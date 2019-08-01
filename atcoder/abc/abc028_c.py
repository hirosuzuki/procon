N = [int(_) for _ in input().split()]

from itertools import combinations

print(sorted([sum(xs) for xs in combinations(N, 3)])[-3])

