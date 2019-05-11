R, G, B, N = [int(_) for _ in input().split()]

result = 0

for left in range(N, -1, -R):
    for x in range(left, -1, -G):
        if x % B == 0:
            result += 1

print(result)
