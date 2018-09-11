N = int(input())
A = [int(_) for _ in input().split()]

p = dict((x, i + 1) for i, x in enumerate(A))

t = [0, N + 1]

import bisect

result = 0
for x in range(1, N+1):
    n = p[x]
    i = bisect.bisect_left(t, n)
    t.insert(i, n)
    result += x * (n - t[i-1]) * (t[i+1] - n)
    # print(n, i, t)

print(result)
