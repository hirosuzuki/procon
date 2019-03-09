N, M, C = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for i in range(N)]

result = 0

for row in A:
    t = C + sum([x * y for x, y in zip(row, B)])
    if t > 0:
        result += 1

print(result)

