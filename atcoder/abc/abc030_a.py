A, B, C, D = [int(_) for _ in input().split()]

if B / A > D / C:
    print("TAKAHASHI")
elif B / A < D / C:
    print("AOKI")
else:
    print("DRAW")