A, B, C = [int(_) for _ in input().split()]

if A < C < B or A > C > B:
    print("Yes")
else:
    print("No")
