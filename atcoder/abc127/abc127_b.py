r, D, x = [int(_) for _ in input().split()]

result = x

for i in range(10):
    result = result * r - D
    print(result)
