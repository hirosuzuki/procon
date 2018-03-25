N = int(input())
A = [int(_) for _ in input().split()]
A += [0]

r = 0
for i in range(N + 1):
    r += abs(A[i] - A[i - 1])

for i in range(N):
    print(r - abs(A[i - 1] - A[i]) - abs(A[i] - A[i + 1]) + abs(A[i - 1] - A[i + 1]))
