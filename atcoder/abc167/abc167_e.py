N, M, K = [int(_) for _ in input().split()]

MOD = 998244353
L = 200001

Fm = {}

inverseFm = {}
x = 1
for i in range(L):
    Fm[i] = x
    x = x * (i + 1) % MOD

def inverseFm(x, cache={}):
    if x in cache:
        return cache[x]
    result = pow(Fm[x], MOD - 2, MOD)
    cache[x] = result
    return result

def C(n, r):
    result = Fm[n] * inverseFm(r) * inverseFm(n - r) % MOD
    return result

result = 0


for i in range(K + 1):
    result = (result + C(N - 1, i) * M * pow(M - 1,  N - i - 1,  MOD)) % MOD

print(result)
