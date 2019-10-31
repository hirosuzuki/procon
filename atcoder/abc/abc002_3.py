import math

X1, Y1, X2, Y2, X3, Y3 = [int(_) for _ in input().split()]

dX2 = (X2-X1)
dX3 = (X3-X1)
dY2 = (Y2-Y1)
dY3 = (Y3-Y1)

p = dX2 * dX3 + dY2 * dY3
d2 = math.sqrt(dX2 ** 2 + dY2 ** 2)
d3 = math.sqrt(dX3 ** 2 + dY3 ** 2)
c = p / d2 / d3
s = math.sqrt(1 - c ** 2)

r = s * d2 * d3 / 2

print(r)