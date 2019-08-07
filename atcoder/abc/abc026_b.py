N = int(input())
R = [int(input()) for i in range(N)]

R.sort(reverse=True)

from math import pi

result = sum([r*r*((-1)**i) for i, r in enumerate(R)]) * pi

print(result)
