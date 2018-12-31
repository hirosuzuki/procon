N = int(input())
A = [int(input()) for i in range(N)]

x = 0

result = -1

for i in range(N):
    x = A[x] - 1
    if x == 1:
        result = i + 1
        break

print(result)
