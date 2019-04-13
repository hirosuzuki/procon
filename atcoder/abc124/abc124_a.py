A, B = [int(_) for _ in input().split()]

result = max(A+(A-1),A+B,B+(B-1))

print(result)
