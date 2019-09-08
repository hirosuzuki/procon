N = int(input())
A = [int(_) for _ in input().split()]

from math import ceil

result = ceil(sum(A) / len([_ for _ in A if _ > 0]))

print(result)