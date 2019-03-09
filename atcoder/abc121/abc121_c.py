N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N)]

AB = sorted(AB)

result = 0
c = M
for a, b in AB:
    t = min(c, b)
    c -= t
    result += a * t

print(result)

