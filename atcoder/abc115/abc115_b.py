N = int(input())
p = [int(input()) for i in range(N)]

xs = sorted(p)
result = sum(xs) - xs[-1] // 2
print(result)