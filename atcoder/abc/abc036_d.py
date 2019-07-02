N = int(input())
AB = [[int(_) for _ in input().split()] for i in range(N - 1)]

import sys
sys.setrecursionlimit(1000000)

from collections import defaultdict

nodes = defaultdict(set)

for a, b in AB:
    nodes[a].add(b)
    nodes[b].add(a)

M = 10**9+7

cache = {}

def calc(x, color, parent=None):
    key = (x, color)
    if key in cache:
        return cache[key]
    result = 1
    for y in nodes[x]:
        if y != parent:
            if color == 0:
                r = calc(y, 0, parent=x) + calc(y, 1, parent=x)
            else:
                r = calc(y, 0, parent=x)
            result = result * r % M
    cache[key] = result
    return result

result = (calc(1, 0) + calc(1, 1)) % M

print(result)

