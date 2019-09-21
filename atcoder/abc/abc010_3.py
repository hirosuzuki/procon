TXA, TYA, TXB, TYB, T, V = [int(_) for _ in input().split()]
N = int(input())
XY = [[int(_) for _ in input().split()] for i in range(N)]

from math import sqrt

def check(x, y):
    d1 = sqrt((x - TXA) ** 2 + (y - TYA) ** 2)
    d2 = sqrt((x - TXB) ** 2 + (y - TYB) ** 2)
    t = (d1 + d2) / V
    return t <= T

if any(check(x, y) for x, y in XY):
    print("YES")
else:
    print("NO")
