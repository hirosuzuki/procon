N = int(input())
A = [int(_) for _ in input().split()]

cs = [0] * N

for i in range(N):
    j = N - i
    cs[j - 1] = (A[j-1] + sum(cs[j - 1::j])) % 2

rs = []
for i, v in enumerate(cs):
    if v:
        rs.append(i + 1)

print(len(rs))
print(*rs)

