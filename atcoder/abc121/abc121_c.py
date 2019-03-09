N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N)]

AB = sorted(AB)

result = 0
c = 0
for a, b in AB:
    d = min(M - c, b)
    c += d
    result += d * a
    if c == M:
        break

print(result)

