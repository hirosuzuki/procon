x1, y1, x2, y2 = [int(_) for _ in input().split()]

dx, dy = x2 - x1, y2 - y1

dx, dy = -dy, dx
x3, y3 = x2 + dx, y2 + dy

dx, dy = -dy, dx
x4, y4 = x3 + dx, y3 + dy

print(x3, y3, x4, y4)
