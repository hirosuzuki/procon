N = int(input())
AB = [[int(_) for _ in input().split()] for i in range(N)]

AB = sorted(AB, key=lambda x:x[0] + x[1], reverse=True)

result = 0
result = sum(a for a, b in AB[0::2]) - sum(b for a, b in AB[1::2])

print(result)
