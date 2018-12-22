N, H, W = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N)]

result = 0

for a, b in AB:
    if a >= H and b >= W:
        result += 1

print(result)

