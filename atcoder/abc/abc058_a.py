A, B, C = [int(_) for _ in input().split()]

if B - A == C - B:
    print("YES")
else:
    print("NO")