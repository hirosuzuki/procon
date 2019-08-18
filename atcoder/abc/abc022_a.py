N, S, T = [int(_) for _ in input().split()]
W = int(input())
A = [0] + [int(input()) for i in range(1, N)]

result = 0

x = W
for a in A:
    x += a
    if S <= x <= T:
        result += 1

print(result)
