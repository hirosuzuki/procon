A, B, C = [int(_) for _ in input().split()]

xs = sorted([A, B, C])

if xs[0] + xs[1] == xs[2]:
    print("Yes")
else:
    print("No") 