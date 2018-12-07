X, A, B = [int(_) for _ in input().split()]

if abs(X - A) > abs(X - B):
    print("B")
else:
    print("A")