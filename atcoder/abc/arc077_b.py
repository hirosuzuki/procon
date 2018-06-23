N = int(input())
A = [int(_) for _ in input().split()]

M = 10**9 + 7
L = 100001

Fm = {}
inverseFm = {}
x = 1
for i in range(L):
    Fm[i] = x
    x = x * (i + 1) % M

def inverseFm(x, cache={}):
    if x in cache:
        return cache[x]
    result = pow(Fm[x], M - 2, M)
    cache[x] = result
    return result

def C(n, r):
    if r > n or r < 0:
        return 0
    result = Fm[n] * inverseFm(r) * inverseFm(n - r) % M
    return result

xs = [-1] * (N + 1)
x1 = 0
x2 = 0
for i, a in enumerate(A):
    if xs[a] >= 0:
        x1 = xs[a]
        x2 = i
        break
    xs[a] = i

print("*", x1, x2)

w = N - 1
l = x1
m = x2 - x1 - 1
r = N - x2

print("*", w, l, m, r)

for k in range(1, N + 2):
    result = C(w, k - 2), C(m + l, k - 1), C(m + r, k - 1), -C(m, k - 1), C(w, k)
    print(k, sum(result) % M, result)
