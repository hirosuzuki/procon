N = int(input())
A = [int(_) for _ in input().split()]


t = sum(A) 
x = [0] * N

x[0] = t - 2 * sum([A[i] for i in range(1, N, 2)])

for i in range(1, N):
    x[i] = 2 * A[i - 1] - x[i - 1]

print(*x)
