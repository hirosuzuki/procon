N, X = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

def solve(N, X, A):
    M = A[:]
    result = sum(M)
    for i in range(1, N):
        M = [min(M[j], A[(j-i)%N]) for j in range(N)]
        r = sum(M) + X * i
        result = min(result, r)
    return result

print(solve(N, X, A))
