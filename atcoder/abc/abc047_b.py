W, H, N = [int(_) for _ in input().split()]
XYA = [[int(_) for _ in input().split()] for i in range(N)]

sx, sy, ex, ey = 0, 0, W, H

for x, y, a in XYA:
    if a == 1:
        sx = max(sx, x)
    elif a == 2:
        ex = min(ex, x)
    elif a == 3:
        sy = max(sy, y)
    elif a == 4:
        ey = min(ey, y)
    
result = max(ex - sx, 0) * max(ey - sy, 0)
print(result)
