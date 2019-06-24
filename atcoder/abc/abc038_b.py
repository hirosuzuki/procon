H1, W1 = [int(_) for _ in input().split()]
H2, W2 = [int(_) for _ in input().split()]

result = (H1 == H2 or H1 == W2) or (W1 == H2 or W1 == W2)

if result:
    print("YES")
else:
    print("NO")

