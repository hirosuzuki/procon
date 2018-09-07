N, M = [int(_) for _ in input().split()]

x = min(N, M // 2)
y = (M - x * 2) // 4

result = x + y

print(result)
