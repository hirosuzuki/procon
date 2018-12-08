A, B, C, D = [int(_) for _ in input().split()]

s = max(A, C)
e = min(B, D)

result = max(e - s, 0)

print(result)

