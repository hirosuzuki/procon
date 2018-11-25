A, B = [int(_) for _ in input().split()]

result = 0
for i in range(A, B + 1):
    s = str(i)
    if s == s[::-1]:
        result += 1

print(result)
