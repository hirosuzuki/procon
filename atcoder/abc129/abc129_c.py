N, M = [int(_) for _ in input().split()]
A = set([int(input()) for i in range(M)])

cs = [0] * (N + 1)

cs[0] = 1

M = 10**9+7

for i in range(1, N + 1):
    if not i in A:
        cs[i] = (cs[i - 2] + cs[i - 1]) % M

result = cs[N]

print(result)
