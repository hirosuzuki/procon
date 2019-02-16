N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

#         0 1 2 3 4 5 6 7 8 9
SEGTBL = [6,2,5,5,4,5,6,3,7,6]

maxnum = [None] * (N + 1 + 10)
maxnum[0] = (0, 0)

if 9 in A and 6 in A:
    A.remove(6)

if 5 in A and 2 in A:
    A.remove(2)
if 5 in A and 3 in A:
    A.remove(3)

if 3 in A and 2 in A:
    A.remove(2)

if 1 in A and 4 in A:
    A.remove(4)
if 1 in A and 6 in A:
    A.remove(6)
if 1 in A and 9 in A:
    A.remove(9)

if 7 in A and 6 in A:
    A.remove(6)
if 7 in A and 9 in A:
    A.remove(9)

# print(A)

i = 0
while i < N:
    n = maxnum[i]
    if not n is None:
        for a in A:
            m = (n[0] + 1, 10 ** n[0] * a + n[1])
            j = i + SEGTBL[a]
            prem = maxnum[j]
            maxnum[j] = m if prem is None else max(prem, m)
    i += 1

print(maxnum[N][1])
