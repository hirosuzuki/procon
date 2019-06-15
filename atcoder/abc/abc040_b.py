N = int(input())

from math import sqrt, floor

s = floor(sqrt(N))

result = N

for i in range(1, s + 1):
    r = N % i + abs(N // i - i)
    result = min(result, r)

print(result)

