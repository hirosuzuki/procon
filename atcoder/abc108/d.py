L = int(input())

xs = []

for m in range(21):
    if (2 << m) > L:
        break
    xs.append((m+1, m+2, 0))
    xs.append((m+1, m+2, 1 << m))

b = 1 << m

for i in range(m - 1, -1, -1):
    c = 1 << i
    if L - b >= c:
        xs.append((i + 1, m + 1, b))
        b += c

print(m + 1, len(xs))

for x in xs:
    print(*x)
