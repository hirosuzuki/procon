N, M = [int(_) for _ in input().split()]
ab = [tuple(int(_) for _ in input().split()) for _ in range(M)]

xs = {}

for a, b in ab:
    if a == 1:
        xs[b] = 1

result = 0

for a, b in ab:
    if b == N and a in xs:
        result = 1
        break

if result:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
