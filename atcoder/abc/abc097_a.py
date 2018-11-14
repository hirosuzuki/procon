A, B, C, D = [int(_) for _ in input().split()]

if abs(A - C) <= D or (abs(A - B) <= D and abs(B - C) <= D):
    print("Yes")
else:
    print("No")
    