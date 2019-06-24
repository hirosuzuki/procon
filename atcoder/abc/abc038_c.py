N = int(input())
A = [int(_) for _ in input().split()]

A.append(-1)

result = 0

s = -1
for i in range(N):
    if A[i + 1] <= A[i]:
        d = i - s
        s = i
        result += d * (d + 1) // 2

print(result)
