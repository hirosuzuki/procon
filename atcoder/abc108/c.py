N, K = [int(_) for _ in input().split()]

result = 0

if K % 2 == 1:
    c = N // K
    result = c ** 3
else:
    K2 = K // 2
    c1 = N // K
    c2 = N // K2 - c1
    result = c1 ** 3 + c2 ** 3

print(result)
