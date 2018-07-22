N = int(input())
AB = [[int(_) for _ in input().split()] for i in range(N)]

result = 0
for a, b in AB[::-1]:
    d = (b - a - result) % b
    result += d

print(result)
