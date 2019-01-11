A, B, C = [int(_) for _ in input().split()]

def check(A, B, C):
    return any((i * B + C) % A == 0 for i in range(A))

if check(A, B, C):
    print("YES")
else:
    print("NO")