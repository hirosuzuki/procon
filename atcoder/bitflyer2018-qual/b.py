A, B, N = [int(_) for _ in input().split()]
X = input()

for c in X:
    if c == 'S':
        if A > 0:
            A -= 1
    if c == 'C':
        if B > 0:
            B -= 1
    if c == 'E':
        if A == 0 and B == 0:
            pass
        elif A >= B:
            A -= 1
        else:
            B -= 1

print(A)
print(B)
