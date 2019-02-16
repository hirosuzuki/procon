A, B = [int(_) for _ in input().split()]

if B % A == 0:
    print(A + B)
else:
    print(B - A)
