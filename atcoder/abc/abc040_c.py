N = int(input())
A = [int(_) for _ in input().split()]


c = [0] * N
c[N - 2] = abs(A[N - 1] - A[N - 2])

for i in range(N - 3, -1, -1):
    c1 = abs(A[i] - A[i + 1]) + c[i + 1]
    c2 = abs(A[i] - A[i + 2]) + c[i + 2]
    c[i] = min(c1, c2)

print(c[0])

