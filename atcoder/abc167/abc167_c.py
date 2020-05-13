N, M, X = [int(_) for _ in input().split()]
CA = [[int(_) for _ in input().split()] for i in range(N)]

C = [row[0] for row in CA]
A = [row[1:] for row in CA]

def solve(N, M, X, C, A):
    result = -1
    for n in range(2**N):
        xs = [0] * M
        r = 0
        for i in range(N):
            if ((1 << i) & n):
                r += C[i]
                for j in range(M):
                    xs[j] += A[i][j]
        if all(X <= xs[j] for j in range(M)):
            if result == -1 or r < result:
                result = r
    return result

print(solve(N, M, X, C, A))