from heapq import *

N = int(input())

result = 100000

ns = [1, 6, 9, 36, 81, 216, 729, 1296, 6561, 7776, 46656, 59049]

h = []

xs = {}

heappush(h, (0, 0))

while 1:
    r, m = heappop(h)
    if m == N:
        result = r
        break
    for n in ns:
        s = r + 1
        x = m + n
        if x <= N and not x in xs:
            xs[x] = s
            heappush(h, (s, x))

print(result)

