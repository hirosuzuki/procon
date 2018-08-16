N, T = [int(_) for _ in input().split()]
t = [int(_) for _ in input().split()]

result = 0

for i in range(N - 1):
    st = t[i]
    ed = t[i + 1]
    result += min(ed - st, T)

result += T

print(result)
