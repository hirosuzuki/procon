
N, M = [int(_) for _ in input().split()]
S = input()
T = input()

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

L = N * M // gcd(N, M)

cs = {}

for i in range(N):
    cs[L // N * i + 1] = S[i]

result = L

for i in range(M):
    j = L // M * i + 1
    if j in cs and cs[j] != T[i]:
        result = -1
        break

print(result)
