N, K = [int(_) for _ in input().split()]

result = 0

for i in range(1, N + 1):
    c = 0
    while i < K:
        c += 1
        i *= 2
    result += 1 / (2 ** c) / N

print(result)
