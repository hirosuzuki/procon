N = int(input())
A = [int(_) for _ in input().split()]

M = 10**9+7

r = 1
for a in A:
    r = r * (a + 2) % M

print(r - 2)
