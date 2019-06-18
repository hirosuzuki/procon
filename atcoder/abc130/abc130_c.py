W, H, x, y = [int(_) for _ in input().split()]

result1 = W * H / 2
result2 = 1 if x == W / 2 and y == H / 2 else 0

print(result1, result2)