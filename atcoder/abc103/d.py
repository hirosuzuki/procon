N, M = [int(_) for _ in input().split()]
AB = [tuple(int(_) for _ in input().split()) for i in range(M)]

AB.sort()

result = 1

x1, x2 = 1, N
for a, b in AB:
    # print(x1, x2, a, b)
    if x2 <= a:
        # print("*")
        result += 1
        x1, x2 = a, b
    else:
        x1 = max(x1, a)
        x2 = min(x2, b)

print(result)

