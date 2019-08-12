N, T = [int(_) for _ in input().split()]
A = [int(input()) for i in range(N)]

result = 0

s = A[0]
t = s + T
result = T

for a in A[1:]:
    if a < t:
        result += a - s
        s = a
        t = s + T
    else:
        result += T
        s = a
        t = s + T
    # print("*", a, s, t, result)

print(result)
