N = int(input())
ab = [[int(_) for _ in input().split()] for n in range(N - 1)]

from collections import defaultdict

ns = defaultdict(list)

for a, b in ab:
    ns[a].append(b)
    ns[b].append(a)

from heapq import *

queue = []
heappush(queue, (0, 1))
heappush(queue, (1, N))

colors = defaultdict(lambda:None)
black_count, white_count = 0, 0

while queue:
    i, index = heappop(queue)
    color = i % 2
    if colors[index] is None:
        colors[index] = color
        if color:
            white_count += 1
        else:
            black_count += 1
        for t in ns[index]:
            if ns[t]:
                heappush(queue, (i + 2, t))

if black_count > white_count:
    print("Fennec")
else:
    print("Snuke")
