def solve0(A, B, C, K):
    for i in range(K):
        A, B, C = B + C, A + C, A + B
    return A - B

def solve(A, B, C, K):
    if K % 2 == 0:
        return A - B
    else:
        return B - A

A, B, C, K = [int(_) for _ in input().split()]

print(solve(A, B, C, K))

