Q = int(input())

def solve(A, B, C):
    if C % 10 % 2 != 0:
        return False
    x = C // 10
    if B % 10 % 2 != 0 and x == 0:
        return False
    y = (B + x) // 10
    if A % 10 % 2 != 0 and y == 0:
        return False
    return True

for i in range(Q):
    A, B, C = [int(_) for _ in input().split()]
    if solve(A, B, C):
        print("Yes")
    else:
        print("No")