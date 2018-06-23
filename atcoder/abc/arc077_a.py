N = int(input())
A = [int(_) for _ in input().split()]

r = [0] * N
x = 0
for i in range(N):
    r[x] = A[-i-1]
    x = N - 1 - x
    if x * 2 < N:
        x += 1

print(*r)

