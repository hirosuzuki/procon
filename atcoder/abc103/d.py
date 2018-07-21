N, M = [int(_) for _ in input().split()]
AB = [tuple(int(_) for _ in input().split()) for i in range(M)]

AB.sort()

result = 1

x1, x2 = 1, N
for a, b in AB:
    if x2 <= a:
        result += 1
        x1, x2 = a, b
    else:
        x1, x2 = a, min(x2, b)

print(result)