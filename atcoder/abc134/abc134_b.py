N, D = [int(_) for _ in input().split()]

from math import ceil

result = ceil(N / (D + D + 1))

print(result)
