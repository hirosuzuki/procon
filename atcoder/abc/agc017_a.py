N, P = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

Pw = [1]
for i in range(1, 51):
    Pw.append(Pw[-1] * i)

def C(n, m):
    return Pw[n] // Pw[n - m] // Pw[m]

odd = sum(x % 2 for x in A)
even = N - odd

r = 0
for i in range(0, odd + 1, 2):
    r += C(odd, i) * (2**even)

if P == 1:
    r = 2**N - r

print(r)
