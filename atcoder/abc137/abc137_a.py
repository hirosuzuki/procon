A, B = [int(_) for _ in input().split()]

result = max(A + B, A - B, A * B)

print(result)