N = int(input())
A = [int(_) for _ in input().split()]

result = 0

for i in range(1, N):
    if A[i-1] == A[i]:
        result += 1
        A[i] = None

print(result)
