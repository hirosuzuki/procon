K, S = [int(_) for _ in input().split()]

result = 0

for x in range(K + 1):
    c = max(K - abs(S - K - x) + 1, 0)
    # print("*", x, c)
    result += c

print(result)