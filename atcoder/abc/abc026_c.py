N = int(input())
B = [int(input()) for i in range(N - 1)]

from collections import defaultdict

cs = defaultdict(set)

for i, x in enumerate(B):
    cs[x].add(i + 2)

def calc(n):
    ss = [calc(i) for i in cs[n]]
    if ss:
        return max(ss) + min(ss) + 1
    else:
        return 1

result = calc(1)

print(result)
