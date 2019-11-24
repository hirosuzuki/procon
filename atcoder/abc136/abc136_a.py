A, B, C = [int(_) for _ in input().split()]

d = min((A - B), C)
result = C - d

print(result)
