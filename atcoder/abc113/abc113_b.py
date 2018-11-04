N = int(input())
T, A = [int(_) for _ in input().split()]
H = [int(_) for _ in input().split()]

result = 0
rd = 100000000000000000000000

for i, x in enumerate(H):
    t = T - 0.006 * x
    d = abs(A - t)
    if d < rd:
        rd = d
        result = i + 1

print(result)
