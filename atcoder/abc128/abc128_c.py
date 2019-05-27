N, M = [int(_) for _ in input().split()]
KS = [[int(_) for _ in input().split()] for i in range(M)]
p = [int(_) for _ in input().split()]

result = 0

def check(i, j):
    x = sum((i >> (s - 1)) & 1 for s in KS[j][1:])
    return x % 2 == p[j]

for i in range(2**N):
    result += all(check(i, j) for j in range(M))

print(result)
