N = int(input())
lr = [[int(_) for _ in input().split()] for i in range(N)]

result = sum(r - l + 1 for l, r in lr)

print(result)
