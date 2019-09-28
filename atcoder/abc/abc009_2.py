N = int(input())
A = [int(input()) for _ in range(N)]

cs = sorted(set(A))
result = cs[-2]

print(result)