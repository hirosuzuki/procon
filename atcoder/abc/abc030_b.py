N, M = [int(_) for _ in input().split()]

r1 = N * 30 + M * 30 / 60
r2 = M * 6

r = (r1 - r2) % 360

if r > 180:
    r = 360 - r

print(r)
