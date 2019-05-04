N, A = [int(_) for _ in input().split()]

from math import ceil

result1 = min(ceil(A / 3), N // 3)
result2 = min(A, N // 3)

print(result1, result2)
