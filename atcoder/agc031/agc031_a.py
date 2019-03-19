N = int(input())
S = input()

from collections import Counter

cs = Counter(S)

M = 10**9 + 7

result = 1
for c in cs:
    result = result * (cs[c] + 1)

result = (result - 1) % M

print(result)

