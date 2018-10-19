N, X = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N)]

AB.sort(key=lambda x:x[1])

AB[-1][0] += X

result = sum(a * b for a, b in AB)

print(result)
