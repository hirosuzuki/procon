N, A, B, C, D = [int(_) for _ in input().split()]

dAB = B - A
dCD = (D - C) / 2
m = (C + D) / 2

x = A
v = 0
for i in range(2, N + 1):
    if x < B:
        x += m
    else:
        x -= m
    v += dCD

if x - v <= B <= x + v:
    print("YES")
else:
    print("NO")

