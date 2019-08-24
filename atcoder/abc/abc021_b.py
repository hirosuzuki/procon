N = int(input())
A, B = [int(_) for _ in input().split()]
K = int(input())
P = [int(_) for _ in input().split()]

from collections import defaultdict

cs = defaultdict(int)

cs[A] += 1
cs[B] += 1

result = True

for x in P:
    cs[x] += 1
    if cs[x] >= 2:
        result = False

if result:
    print("YES")
else:
    print("NO")
