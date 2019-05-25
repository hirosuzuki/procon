A, B = [int(_) for _ in input().split()]

if A >= 13:
    result = B
elif A >= 6:
    result = B // 2
else:
    result = 0

print(result)
