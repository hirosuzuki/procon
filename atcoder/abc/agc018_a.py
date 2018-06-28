N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

from functools import reduce

a = sorted(A)
d = reduce(gcd, a)

if (a[-1] >= K) and (a[-1] - K) % d == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

