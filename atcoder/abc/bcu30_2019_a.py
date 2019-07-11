N, K = [int(_) for _ in input().split()]
A = [int(input()) for i in range(N)]

A.sort(reverse=True)

result = sum(A[:K]) + sum(A[K:]) * 2

print(result)
