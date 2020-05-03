A, B, N = [int(_) for _ in input().split()]

from math import gcd, floor

g = A * B // gcd(A, B)
if N >= g:
    N = g

if N < B:
    n = N
else:
    n = N // B * B - 1

result = floor(A * n / B) - A * floor(n / B)

print(result)
