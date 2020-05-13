A, B, C, K = [int(_) for _ in input().split()]

l = A + B + C - K

def solve(A, B, C, K):
    result = 0
    n = min(A, K)
    result += n
    K -= n
    A -= n
    if K == 0:
        return result
    n = min(B, K)
    K -= n
    B -= n
    if K == 0:
        return result
    n = min(C, K)
    result -= n
    K -= n
    C -= n
    return result

print(solve(A, B, C, K))