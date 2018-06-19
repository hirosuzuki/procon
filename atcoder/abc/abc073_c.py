N = int(input())
A = [int(input()) for i in range(N)]

from collections import Counter

print(sum(c % 2 for x, c in Counter(A).items()))
