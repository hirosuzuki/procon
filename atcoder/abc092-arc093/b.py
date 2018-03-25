N = int(input())
D, X = [int(_) for _ in input().split()]
A = [int(input()) for _ in range(N)]

r = X
for a in A:
    b = (D - 1) // a + 1
    r += b

print(r)
