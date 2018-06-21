N = int(input())
A = [int(_) for _ in input().split()]

import collections

c = collections.Counter(A)
xs = [x for x, n in c.items() if n >= 2]
xs.sort()

if len(xs) >= 1 and c[xs[-1]] >= 4:
    print(xs[-1] ** 2)
elif len(xs) >= 2:
    print(xs[-1] * xs[-2])
else:
    print(0)
