A, B, C = [int(_) for _ in input().split()]

result = min(A + B, B + C, C + A)
print(result)
