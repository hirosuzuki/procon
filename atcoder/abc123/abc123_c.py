N = int(input())
T = [int(input()) for i in range(5)]

from math import ceil
m = ceil(N / min(T))

result = m + 4

print(result)
