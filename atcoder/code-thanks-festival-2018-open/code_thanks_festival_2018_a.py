T, A, B, C, D = [int(_) for _ in input().split()]

result = 0

if T >= A + C:
    result = B + D
elif T >= C:
    result = D
elif T >= A:
    result = B

print(result)
