def solve(A, B, C, X):
    result = sum(
        a * 500 + b * 100 + c * 50 == X
        for a in range(A + 1)
        for b in range(B + 1)
        for c in range(C + 1)
    )
    return result

A = int(input())
B = int(input())
C = int(input())
X = int(input())

print(solve(A, B, C, X))