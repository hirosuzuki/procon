N1, N2, N3, N4 = [int(_) for _ in input().split()]

ns = (N1, N2, N3, N4)

if (1 in ns) and (9 in ns) and (7 in ns) and (4 in ns):
    print("YES")
else:
    print("NO")