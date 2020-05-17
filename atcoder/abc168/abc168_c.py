A, B, H, M = [int(_) for _ in input().split()]

import math

ax = math.sin(2*math.pi * (H * 60 + M) / (12 * 60)) * A
ay = math.cos(2*math.pi * (H * 60 + M) / (12 * 60)) * A

bx = math.sin(2*math.pi * M / 60) * B
by = math.cos(2*math.pi * M / 60) * B

result = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

print(result)