N, M, C = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for i in range(N)]

result = sum(
    C + sum([x * y for x, y in zip(a, B)]) > 0
    for a in A
)

print(result)