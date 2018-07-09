N, C, K = [int(_) for _ in input().split()]
T = [int(input()) for i in range(N)]

T.sort()

result = 0
i = 0
j = 0
while i < N:
    if j == N or T[j] - T[i] > K:
        n = max(min(C, j - i), 1)
        if n == 0: raise
        # print(T[i:i+n], i, j)
        i += n
        result += 1
        continue
    if j >= i + C:
        # print(T[i:i+C])
        i += C
        result += 1
        continue
    j += 1

print(result)
