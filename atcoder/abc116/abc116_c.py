N = int(input())
H = [int(_) for _ in input().split()]

result = 0
for i in range(1, 101):
    for j in range(N):
        if H[j] >= i:
            if j == 0 or H[j - 1] < i:
                result += 1

print(result)