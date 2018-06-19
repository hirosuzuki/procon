N = int(input())
A = [[int(_) for _ in input().split()] for i in range(N)]

def calc(N, A):
    r = 0
    if N == 1:
        return 0
    if N == 2:
        return A[0][1]
    for i in range(0, N):
        for j in range(i + 1, N):
            a = A[i][j]
            d = min(A[i][k] + A[k][j] for k in range(0, N) if k != i and k != j)
            if a > d:
                return -1
            if a < d:
                r += a
    return r

print(calc(N, A))
