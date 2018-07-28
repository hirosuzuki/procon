C, D = [int(_) for _ in input().split()]

result = 0

for i in range(44):
    k = 2**i
    n, m = k * 140, k * 170
    if m - 1 >= C and D - 1 >= n:
        x = min(m - 1, D - 1) - max(n, C) + 1
        # print(C, D, n, m, x)
        result += x

print(result)
