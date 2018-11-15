A, B, C = [int(_) for _ in input().split()]
K = int(input())

a, b, c = sorted([A, B, C])

result = a + b + c * (2**K)

print(result)
