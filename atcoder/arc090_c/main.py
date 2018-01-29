def solve(N, A):
    rmax = 0
    for i in range(N):
        r = sum(A[0][0:i + 1]) + sum(A[1][i:])
        rmax = max(rmax, r)
    return rmax

N = int(input())
A = [[int(x) for x in input().split()] for i in range(2)]
print(solve(N, A))
