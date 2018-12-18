N = int(input())
A = [int(_) for _ in input().split()]

total = sum(A)

result = 10**100
x = 0
for a in A[:-1]:
    x += a
    r = abs(total - x - x)
    result = min(result, r)

print(result)
