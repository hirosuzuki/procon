A = int(input())
B = int(input())

from math import ceil

n = ceil(A / B)
result = n * B - A

print(result)